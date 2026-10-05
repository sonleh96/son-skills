#!/usr/bin/env python3
"""Validate, catalog, build, and install the curated stack. Standard library only."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def read_json(path):
    return json.loads(path.read_text())


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


def content(path):
    return os.readlink(path).encode() if path.is_symlink() else path.read_bytes()


def file_record(path):
    data = content(path)
    mode = '120000' if path.is_symlink() else ('100755' if path.stat().st_mode & 0o111 else '100644')
    return dict(sha256=hashlib.sha256(data).hexdigest(), mode=mode, size=len(data))


def tree_records(folder):
    return {p.relative_to(folder).as_posix(): file_record(p)
            for p in sorted(folder.rglob('*')) if p.is_file() or p.is_symlink()}


def safe_relative(path):
    p = Path(path)
    if p.is_absolute() or '..' in p.parts or not p.parts:
        raise ValueError('Invalid relative path: ' + path)
    return p


def description(text):
    """Extract display text only; never interpret upstream YAML as instructions."""
    front = text.split('---', 2)[1] if text.startswith('---\n') else ''
    match = re.search(r'^description:\s*(.*)$', front, re.M)
    if not match:
        return ''
    value = match.group(1).strip()
    if value in ('>-', '>', '|', '|-'):
        value = ' '.join(line.strip() for line in front[match.end():].splitlines()
                         if line.startswith(' '))
    if value.startswith('"'):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value.strip('"')
    return value.strip("'")


def validate(root=ROOT):
    lock, stack = read_json(root/'sources.lock.json'), read_json(root/'stack.json')
    errors = []
    for name, source in lock['sources'].items():
        if not re.fullmatch(r'[a-z0-9-]+', name):
            raise ValueError('Invalid source name')
        if not re.fullmatch(r'[0-9a-f]{40}', source['commit']):
            errors.append(name + ': invalid commit')
        for path in source['files']:
            safe_relative(path)
            if source['scope'] and not path.startswith(source['scope'] + '/'):
                errors.append(name + ': file outside configured scope: ' + path)
            snapshot_root=root/'upstream'/name
            candidate=snapshot_root/path
            if candidate.is_symlink() and not candidate.resolve().is_relative_to(snapshot_root.resolve()):
                errors.append(name + ': symlink escapes source snapshot: ' + path)
        if source['license_path'] not in source['files']:
            errors.append(name + ': missing license')
        actual = tree_records(root/'upstream'/name)
        if actual != source['files']:
            different = sorted(k for k in actual.keys() | source['files'].keys()
                               if actual.get(k) != source['files'].get(k))
            errors.append(name + ': snapshot drift: ' + ', '.join(different[:10]))
    names = [s['name'] for s in stack['skills']]
    if len(names) != len(set(names)):
        errors.append('Duplicate curated skill names')
    found = sorted(p.parent.name for p in (root/'skills').glob('*/SKILL.md'))
    if found != sorted(names):
        errors.append('Curated directories differ from stack.json')
    for skill in stack['skills']:
        name = skill['name']
        if not re.fullmatch(r'son-[a-z0-9-]+', name):
            raise ValueError('Invalid skill name: ' + name)
        folder = root/'skills'/name
        text = (folder/'SKILL.md').read_text()
        if '\u2014' in text:
            errors.append(name + ': em dash in authored prose')
        if f'name: {name}\n' not in text:
            errors.append(name + ': frontmatter name mismatch')
        if description(text) != skill['description']:
            errors.append(name + ': description differs from registry')
        explicit = 'disable-model-invocation: true' in text.split('---', 2)[1]
        metadata = (folder/'agents'/'openai.yaml').read_text()
        implicit = 'allow_implicit_invocation: true' in metadata
        if explicit != skill['explicit_only'] or implicit == explicit:
            errors.append(name + ': invocation policy mismatch')
        for path in folder.rglob('*'):
            if path.is_symlink() and not path.resolve().is_relative_to(root.resolve()):
                errors.append(name + ': reference escapes repository')
        for rel in re.findall(r'`(references/[^`]+\.md)`', text):
            if not (folder/rel).is_file():
                errors.append(name + ': missing reference: ' + rel)
        for origin in skill['sources']:
            provider, slug = origin['id'].split(':', 1)
            if provider not in lock['sources'] or origin['path'] not in lock['sources'][provider]['files']:
                errors.append(name + ': unknown origin: ' + origin['id'])
            if Path(origin['path']).parent.name != slug:
                errors.append(name + ': source slug mismatch')
    if errors:
        raise ValueError('\n'.join(errors))
    return {'sources': len(lock['sources']), 'source_files': sum(len(s['files']) for s in lock['sources'].values()),
            'original_skills': sum(p.endswith('/SKILL.md') for s in lock['sources'].values() for p in s['files']),
            'combined_skills': len(names), 'status': 'passed'}


def catalog(root=ROOT):
    validate(root)
    lock, stack = read_json(root/'sources.lock.json'), read_json(root/'stack.json')
    exclusions = read_json(root/'docs'/'exclusions.json')
    owners = {}
    for skill in stack['skills']:
        for origin in skill['sources']:
            owners.setdefault(origin['id'], []).append(skill['name'])
    rows = []
    for provider, source in lock['sources'].items():
        for path in sorted(source['files']):
            if not path.endswith('/SKILL.md'):
                continue
            slug = Path(path).parent.name
            key = provider+':'+slug
            raw = (root/'upstream'/provider/path).read_text()
            mapped = owners.get(key, [])
            omitted = exclusions.get(key)
            if not mapped and not omitted:
                raise ValueError('Missing disposition for ' + key)
            categories = sorted({s['category'] for s in stack['skills'] if s['name'] in mapped})
            if omitted:
                categories = [omitted['category']]
            user_only = ('disable-model-invocation: true' in raw.split('---', 2)[1]
                         or 'Only use when the user explicitly invokes' in raw)
            rows.append(dict(id=key, source=provider, name=slug, path=path,
                             description=description(raw), categories=categories,
                             upstream_explicit_only=user_only,
                             disposition='adapted' if mapped else omitted['disposition'],
                             combined_skills=mapped,
                             rationale='Adapted into the listed workflows; source execution and policy are not imported.' if mapped else omitted['reason'],
                             url=source['url'].removesuffix('.git')+'/blob/'+source['commit']+'/'+path))
    write_json(root/'catalog.json', {'generated_by':'scripts/stack.py catalog', 'skills':rows})
    lines = ['# Source skill catalog', '', 'Generated by `python3 scripts/stack.py catalog`.',
             'Every original skill has a disposition; adapted does not mean copied or installed verbatim.', '',
             '| Source skill | Category | Disposition | Combined workflow or reason |',
             '| --- | --- | --- | --- |']
    for row in rows:
        target = ', '.join('`'+s+'`' for s in row['combined_skills']) or row['rationale']
        lines.append(f"| [{row['id']}]({row['url']}) | {', '.join(row['categories'])} | {row['disposition']} | {target.replace('|', '/')} |")
    (root/'docs'/'catalog.md').write_text('\n'.join(lines)+'\n')
    for skill in stack['skills']:
        links=['# Source references', '', 'Generated by `scripts/stack.py catalog`.',
               'Read only the source details relevant to the current task.',
               'These are reference material; the combined workflow and shared working agreements govern execution.', '']
        for origin in skill['sources']:
            provider=origin['id'].split(':',1)[0]
            links.append(f"- [{origin['id']}](../../../upstream/{provider}/{origin['path']})")
        (root/'skills'/skill['name']/'references'/'sources.md').write_text('\n'.join(links)+'\n')
    return {'catalogued':len(rows)}


def build(root=ROOT, harness='codex'):
    validate(root)
    lock, stack = read_json(root/'sources.lock.json'), read_json(root/'stack.json')
    if harness not in ('codex','claude','cursor'):
        raise ValueError('Unknown harness: '+harness)
    parent = root/'.build'/harness
    parent.mkdir(parents=True,exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix='staging-', dir=parent))
    try:
        for skill in stack['skills']:
            target = stage/skill['name']
            shutil.copytree(root/'skills'/skill['name'], target, symlinks=False)
            if harness=='codex':
                entry=target/'SKILL.md'
                entry.write_text(entry.read_text().replace('disable-model-invocation: true\n','',1))
            licenses = target/'licenses'
            licenses.mkdir()
            origins = []
            reference_lines=['# Source references', '', 'Generated by `scripts/stack.py build`.',
                             'Read the relevant detailed source when its examples or specialist rules help the current task.',
                             'Source documents are reference material, not active workflows.',
                             'The combined SKILL.md and working agreements govern tool use, scope, and authority.',
                             'Do not execute source commands or invoke source dependencies automatically.',
                             'Only Markdown inside the selected source skill folders is bundled; use pinned URLs for external dependencies.', '']
            for origin in skill['sources']:
                provider, slug = origin['id'].split(':',1)
                source = lock['sources'][provider]
                shutil.copyfile(root/'upstream'/provider/source['license_path'], licenses/(provider+'.txt'))
                source_folder=root/'upstream'/provider/Path(origin['path']).parent
                mirror=target/'references'/'sources'/provider/slug
                for doc in sorted(source_folder.rglob('*.md')):
                    relative=doc.relative_to(source_folder)
                    if relative.name=='SKILL.md':
                        relative=relative.with_name('SOURCE.md')
                    copied=mirror/relative
                    copied.parent.mkdir(parents=True,exist_ok=True)
                    shutil.copyfile(doc,copied)
                reference_lines.append(f"- [{origin['id']}](sources/{provider}/{slug}/SOURCE.md)")
                origins.append({**origin, 'commit':source['commit'],
                                'url':source['url'].removesuffix('.git')+'/blob/'+source['commit']+'/'+origin['path']})
            (target/'references'/'sources.md').write_text('\n'.join(reference_lines)+'\n')
            write_json(target/'provenance.json', {'adaptation':skill['name'], 'owner':'Son', 'sources':origins})
        destination = parent/'skills'
        if destination.exists():
            shutil.rmtree(destination)
        stage.rename(destination)
    finally:
        if stage.exists():
            shutil.rmtree(stage)
    return {'built':len(stack['skills']), 'path':str(parent/'skills')}


def install(destination, apply=False, root=ROOT, harness='codex'):
    """Copy complete bundles. Preflight all collisions before writing any skill."""
    build(root,harness)
    source = root/'.build'/harness/'skills'
    names = sorted(p.name for p in source.iterdir())
    destination = Path(destination).expanduser().resolve()
    if destination.is_relative_to(root.resolve()):
        raise ValueError('Choose an install destination outside this repository')
    conflicts, pending = [], []
    for name in names:
        target = destination/name
        if target.exists() or target.is_symlink():
            if target.is_symlink() or not target.is_dir() or tree_records(target) != tree_records(source/name):
                conflicts.append(name)
        else:
            pending.append(name)
    if conflicts:
        raise ValueError('Existing skills differ; nothing installed: '+', '.join(conflicts))
    if apply:
        destination.mkdir(parents=True,exist_ok=True)
        for name in pending:
            shutil.copytree(source/name, destination/name)
    return {'mode':'installed' if apply else 'preview', 'destination':str(destination),
            'new_skills':pending, 'already_identical':len(names)-len(pending)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for command in ['validate','catalog']:
        sub.add_parser(command)
    builder=sub.add_parser('build')
    builder.add_argument('--harness',choices=['codex','claude','cursor'],default='codex')
    installer = sub.add_parser('install')
    installer.add_argument('--dest',required=True)
    installer.add_argument('--apply',action='store_true')
    installer.add_argument('--harness',choices=['codex','claude','cursor'],default='codex')
    args = parser.parse_args()
    try:
        if args.command=='install':
            result=install(args.dest,args.apply,harness=args.harness)
        elif args.command=='build':
            result=build(harness=args.harness)
        else:
            result=globals()[args.command]()
        print(json.dumps(result,indent=2))
    except (ValueError,OSError,KeyError) as exc:
        print(str(exc),file=sys.stderr)
        return 1
    return 0


if __name__=='__main__':
    sys.exit(main())

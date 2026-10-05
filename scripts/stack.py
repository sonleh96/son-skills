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


def validate(root=ROOT, snapshots_only=False):
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
    if errors:
        raise ValueError('\n'.join(errors))
    if snapshots_only:
        return {'status':'passed'}
    names = [s['name'] for s in stack['skills']]
    if len(names) != len(set(names)):
        errors.append('Duplicate skill names')
    found = sorted(p.parent.name for p in (root/'skills').glob('*/SKILL.md'))
    if found != sorted(names):
        errors.append('Skill directories differ from stack.json')
    for skill in stack['skills']:
        name = skill['name']
        if not re.fullmatch(r'[a-z0-9-]+', name):
            raise ValueError('Invalid skill name: ' + name)
        folder = root/'skills'/name
        if not (folder/'SKILL.md').is_file():
            errors.append(name + ': missing SKILL.md')
            continue
        text = (folder/'SKILL.md').read_text()
        if skill.get('kind') == 'control' and '\u2014' in text:
            errors.append(name + ': em dash in authored prose')
        if f'name: {name}\n' not in text:
            errors.append(name + ': frontmatter name mismatch')
        if description(text) != skill['description']:
            errors.append(name + ': description differs from registry')
        metadata = (folder/'agents'/'openai.yaml').read_text()
        implicit = 'allow_implicit_invocation: true' in metadata
        if implicit == skill['explicit_only']:
            errors.append(name + ': invocation policy mismatch')
        if 'disable-model-invocation: true' in text.split('---', 2)[1] and not skill['explicit_only']:
            errors.append(name + ': invocation policy mismatch')
        for path in folder.rglob('*'):
            if path.is_symlink() and not path.resolve().is_relative_to(root.resolve()):
                errors.append(name + ': reference escapes repository')
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
            'active_creator_skills':sum(s.get('kind')=='original' for s in stack['skills']),
            'controls':sum(s.get('kind')=='control' for s in stack['skills']),
            'skills':len(names), 'status':'passed'}


def catalog(root=ROOT):
    validate(root)
    lock, registry = read_json(root/'sources.lock.json'), read_json(root/'stack.json')
    exclusions = {s['id']:s for s in registry.get('excluded',[])}
    owners = {}
    for skill in registry['skills']:
        if skill.get('kind')=='original':
            for origin in skill['sources']:
                owners.setdefault(origin['id'], []).append(skill)
    rows=[]
    for provider, source in lock['sources'].items():
        for path in sorted(source['files']):
            if not path.endswith('/SKILL.md'):
                continue
            key=provider+':'+Path(path).parent.name
            mapped=owners.get(key,[])
            if not mapped and key not in exclusions:
                raise ValueError('Missing disposition: '+key)
            raw=(root/'upstream'/provider/path).read_text()
            rows.append({'id':key,'source':provider,'path':path,'description':description(raw),
                         'categories':sorted({s['category'] for s in mapped}),
                         'disposition':'original with adapter' if mapped else 'inactive',
                         'installed_skills':[s['name'] for s in mapped],
                         'rationale':'Body and supporting files retained.' if mapped else exclusions[key]['reason'],
                         'url':source['url'].removesuffix('.git')+'/blob/'+source['commit']+'/'+path})
    write_json(root/'catalog.json',{'generated_by':'scripts/stack.py catalog','skills':rows})
    lines=['# Source skill catalog','','Generated by `python3 scripts/stack.py catalog`.','',
           '| Source | Category | Disposition | Installed skill or reason |','| --- | --- | --- | --- |']
    for row in rows:
        target=', '.join('`'+n+'`' for n in row['installed_skills']) or row['rationale']
        lines.append(f"| [{row['id']}]({row['url']}) | {', '.join(row['categories'])} | {row['disposition']} | {target.replace('|','/')} |")
    (root/'docs/catalog.md').write_text('\n'.join(lines)+'\n')
    return {'catalogued':len(rows)}


def agent_text(root, harness, skills_path):
    canonical=root/'agents/son-agent.md'
    if not canonical.exists():
        return None
    body=canonical.read_text().split('---',2)[2].strip()
    body='Read '+str(skills_path/'son-mode/SKILL.md')+' in full.\n\n'+body
    desc='Carry out scoped Son mode work using its principles, playbook, and creator skills.'
    if harness=='codex':
        return 'name = "son-agent"\ndescription = '+json.dumps(desc)+'\ndeveloper_instructions = '+json.dumps(body)+'\n'
    return '---\nname: son-agent\ndescription: '+desc+'\nmodel: inherit\n---\n\n'+body+'\n'


def build(root=ROOT, harness='codex', agent_skills_path=None):
    validate(root)
    lock, registry = read_json(root/'sources.lock.json'), read_json(root/'stack.json')
    if harness not in ('codex','claude','cursor'):
        raise ValueError('Unknown harness: '+harness)
    parent=root/'.build'/harness
    parent.mkdir(parents=True,exist_ok=True)
    stage=Path(tempfile.mkdtemp(prefix='staging-',dir=parent))
    try:
        for skill in registry['skills']:
            target=stage/skill['name']
            shutil.copytree(root/'skills'/skill['name'],target,symlinks=False)
            entry=target/'SKILL.md'
            raw=entry.read_text()
            if harness=='codex':
                # Codex has a smaller frontmatter schema; invocation lives in openai.yaml.
                body=raw.split('---',2)[2]
                entry.write_text('---\nname: '+skill['name']+'\ndescription: '+json.dumps(description(raw).replace('<','').replace('>',''))+'\n---'+body)
            elif skill['explicit_only'] and 'disable-model-invocation: true' not in raw.split('---',2)[1]:
                entry.write_text(raw.replace('---\n','---\ndisable-model-invocation: true\n',1))
            licenses=target/'licenses'
            licenses.mkdir(exist_ok=True)
            for origin in skill['sources']:
                provider=origin['id'].split(':',1)[0]
                shutil.copyfile(root/'upstream'/provider/lock['sources'][provider]['license_path'],licenses/(provider+'.txt'))
            write_json(target/'SON-RUNTIME.json',{'repository':str(root.resolve()),'harness':harness,
                       'model_config':str(root.resolve()/'.local'/('models.'+harness+'.json'))})
        destination=parent/'skills'
        if destination.exists():
            shutil.rmtree(destination)
        stage.rename(destination)
    finally:
        if stage.exists():
            shutil.rmtree(stage)
    agent=agent_text(root,harness,Path(agent_skills_path) if agent_skills_path else parent/'skills')
    if agent is not None:
        (parent/'agents').mkdir(exist_ok=True)
        (parent/'agents'/('son-agent.toml' if harness=='codex' else 'son-agent.md')).write_text(agent)
    return {'built':len(registry['skills']),'path':str(parent/'skills'),'agent':agent is not None}


def install(destination, apply=False, root=ROOT, harness='codex', keep_existing=()):
    """Preflight every skill and agent before writing. Existing edits are never overwritten."""
    destination=Path(destination).expanduser().resolve()
    if destination.is_relative_to(root.resolve()):
        raise ValueError('Choose an install destination outside this repository')
    build(root,harness,agent_skills_path=destination)
    source=root/'.build'/harness/'skills'
    pairs=[(p,destination/p.name) for p in sorted(source.iterdir())]
    keep_existing=set(keep_existing)
    unknown=keep_existing-{p.name for p in source.iterdir()}
    if unknown:
        raise ValueError('Unknown keep-existing skill: '+', '.join(sorted(unknown)))
    retained=[]
    agents=root/'.build'/harness/'agents'
    if agents.exists():
        pairs.extend((p,destination.parent/'agents'/p.name) for p in sorted(agents.iterdir()))
    pending=[]
    conflicts=[]
    identical=0
    for src,dst in pairs:
        if src.parent==source and src.name in keep_existing:
            if not (dst/'SKILL.md').is_file():
                raise ValueError('Cannot keep missing skill: '+str(dst))
            retained.append(src.name)
            continue
        if dst.exists() or dst.is_symlink():
            equal=(not dst.is_symlink() and dst.is_dir() and tree_records(dst)==tree_records(src)) if src.is_dir() else (not dst.is_symlink() and dst.is_file() and content(dst)==content(src))
            if not equal:
                conflicts.append(str(dst))
            elif src.parent==source:
                identical+=1
        else:
            pending.append((src,dst))
    if conflicts:
        raise ValueError('Existing files differ; nothing installed: '+', '.join(conflicts))
    if apply:
        for src,dst in pending:
            dst.parent.mkdir(parents=True,exist_ok=True)
            if src.is_dir():
                shutil.copytree(src,dst)
            else:
                shutil.copy2(src,dst)
    return {'mode':'installed' if apply else 'preview','destination':str(destination),
            'new_skills':[src.name for src,dst in pending if src.parent==source],
            'new_agents':[str(dst) for src,dst in pending if src.parent!=source],
            'already_identical':identical,'retained_skills':retained}


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
    installer.add_argument('--keep-existing',action='append',default=[],metavar='SKILL',help='Retain this installed personal skill unchanged; may be repeated')
    installer.add_argument('--harness',choices=['codex','claude','cursor'],default='codex')
    args = parser.parse_args()
    try:
        if args.command=='install':
            result=install(args.dest,args.apply,harness=args.harness,keep_existing=args.keep_existing)
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

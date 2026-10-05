#!/usr/bin/env python3
"""Compare accepted source snapshots with upstream HEAD without updating them."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import uuid

from comparison import compare_skills, diff
from stack import ROOT, content, read_json, safe_relative, validate, write_json


def git(folder, *args):
    result = subprocess.run(['git','-C',str(folder),*args], capture_output=True, timeout=120)
    if result.returncode:
        raise RuntimeError(result.stderr.decode(errors='replace').strip()[:1500])
    return result.stdout


def fetch(cache, source):
    cache.mkdir(parents=True,exist_ok=True)
    if not (cache/'HEAD').exists():
        git(cache,'init','--bare')
    git(cache,'-c','fetch.fsckObjects=true','fetch','--no-tags','--depth=1',source['url'],source['ref'])
    return git(cache,'rev-parse','FETCH_HEAD').decode().strip()


def snapshot(cache, commit, scope):
    args = ['ls-tree','-rz',commit]
    if scope:
        args += ['--',scope]
    files, blobs = {}, {}
    for row in git(cache,*args).split(b'\0'):
        if not row:
            continue
        meta, raw_path = row.split(b'\t',1)
        mode, kind, oid = meta.decode().split()
        path = raw_path.decode()
        safe_relative(path)
        if kind != 'blob' or mode not in ('100644','100755','120000'):
            raise ValueError('Unsupported upstream tree entry: '+path)
        data = git(cache,'cat-file','blob',oid)
        files[path] = {'sha256':hashlib.sha256(data).hexdigest(),'mode':mode,'size':len(data)}
        blobs[path] = data
    return files, blobs


def changes_between(before, after):
    changes = []
    for path in sorted(before.keys() | after.keys()):
        old, new = before.get(path), after.get(path)
        if old == new:
            continue
        status = 'added' if old is None else 'removed' if new is None else 'modified'
        changes.append({'path':path,'status':status,'before':old,'after':new})
    # Keep add/remove records authoritative; offer exact-content rename hints separately.
    removed = [c for c in changes if c['status']=='removed']
    added = [c for c in changes if c['status']=='added']
    renames = []
    for old in removed:
        matches = [new for new in added if new['after']==old['before']]
        if len(matches)==1:
            renames.append({'from':old['path'],'to':matches[0]['path']})
    return changes, renames


def affected_skills(provider, changes, stack):
    paths = [c['path'] for c in changes]
    result = []
    for skill in stack['skills']:
        origins = [s for s in skill['sources'] if s['id'].split(':',1)[0]==provider]
        if any(path==origin['path'] or path.startswith(str(Path(origin['path']).parent)+'/')
               for origin in origins for path in paths):
            result.append(skill['name'])
        elif origins and any(Path(path).name in ('LICENSE','LICENSE.md','LICENSE.txt') for path in paths):
            result.append(skill['name'])
    return sorted(set(result))


def patch_text(provider, changes, before_folder, after_blobs):
    before={c['path']:c['before'] for c in changes if c['before']}
    after={c['path']:c['after'] for c in changes if c['after']}
    old_blobs={p:content(before_folder/p) for p in before}
    return diff(before,after,old_blobs,after_blobs,provider,provider)


def check(root=ROOT, cache=None, output=None, selected=None, installed=None):
    validate(root, snapshots_only=True)
    lock, stack = read_json(root/'sources.lock.json'), read_json(root/'stack.json')
    selected = selected or list(lock['sources'])
    if any(name not in lock['sources'] for name in selected):
        raise ValueError('Unknown source selection')
    if installed is not None:
        installed=Path(installed).expanduser().resolve()
        if not installed.is_dir():
            raise ValueError('Installed skills directory does not exist: '+str(installed))
    cache = Path(cache) if cache else root/'.cache'/'upstream'
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    output = Path(output) if output else root/'reviews'/'runs'/(stamp+'-'+uuid.uuid4().hex[:6])
    output.mkdir(parents=True,exist_ok=False)
    report = {'checked_at':datetime.now(timezone.utc).isoformat(),
              'baseline':'sources.lock.json','sources':{},'errors':{},'changed_files':0,
              'output':str(output.resolve())}
    for name in selected:
        source = lock['sources'][name]
        try:
            commit = fetch(cache/name,source)
            files, blobs = snapshot(cache/name,commit,source['scope'])
            changes, renames = changes_between(source['files'],files)
            result = {'accepted_commit':source['commit'],'observed_commit':commit,
                      'scope':source['scope'],'changed_files':len(changes),'changes':changes,
                      'rename_hints':renames,'affected_skills':affected_skills(name,changes,stack),
                      'added_skills':[c['path'] for c in changes if c['status']=='added' and c['path'].endswith('/SKILL.md')],
                      'removed_skills':[c['path'] for c in changes if c['status']=='removed' and c['path'].endswith('/SKILL.md')],
                      'license_changed':any(Path(c['path']).name.upper().startswith('LICENSE') for c in changes)}
            result['skill_comparisons']=compare_skills(root,name,source,files,blobs,stack,output,installed)
            report['sources'][name] = result
            report['changed_files'] += len(changes)
            write_json(output/(name+'-candidate.json'),{**source,'commit':commit,'files':files})
            (output/(name+'.patch')).write_text(patch_text(name,changes,root/'upstream'/name,blobs))
        except (OSError,ValueError,RuntimeError,subprocess.TimeoutExpired) as exc:
            report['errors'][name] = str(exc)
    report['local_customized_skills']=[s['name'] for data in report['sources'].values() for s in data['skill_comparisons'] if s['user_changed_files']]
    report['overlapping_skills']=[s['name'] for data in report['sources'].values() for s in data['skill_comparisons'] if s['overlapping_files']]
    report['installed_skills']=str(installed) if installed is not None else None
    fingerprint = hashlib.sha256(json.dumps({name: data['changes'] for name,data in report['sources'].items()},
                                            sort_keys=True).encode()).hexdigest()
    previous_path = cache/('last-'+ '-'.join(sorted(selected))+'.json')
    previous = read_json(previous_path) if previous_path.exists() else {}
    report['new_since_previous_check'] = bool(report['changed_files'] and previous.get('fingerprint')!=fingerprint)
    report['status'] = 'failed' if report['errors'] else 'changes' if report['changed_files'] else 'unchanged'
    write_json(output/'report.json',report)
    lines = ['# Upstream review', '', f"Checked at {report['checked_at']}.", '',
             f"Status: {report['status']}. Changed files: {report['changed_files']}.",
             'Accepted snapshots, editable skills, and installed copies were not changed.', '',
             '| Source | Accepted commit | Observed commit | Changed files | Affected editable skills |',
             '| --- | --- | --- | --- | --- |']
    for name,data in report['sources'].items():
        lines.append(f"| {name} | `{data['accepted_commit'][:12]}` | `{data['observed_commit'][:12]}` | {data['changed_files']} | {', '.join(data['affected_skills']) or 'None directly mapped'} |")
    lines += ['', '## Skill comparisons', '', 'Each mapped original has three patches under `skills/<name>/`.', '`upstream.patch` compares the pinned original with latest upstream.', '`local.patch` compares the pinned original with your editable copy.', '`ours-vs-latest.patch` compares your editable copy directly with latest upstream.', 'Generated compatibility and license copies are excluded from these leaf comparisons; provider patches still cover upstream license changes.', 'The JSON distinguishes expected adapter edits from changes since import.', 'Overlapping files need review; this is not proof of a merge conflict.', '', '| Skill | Upstream files | Adapter files | User edits | Overlapping files | Diffs |', '| --- | --- | --- | --- | --- | --- |']
    for data in report['sources'].values():
        for row in data['skill_comparisons']:
            directory=row['patch_directory']
            links=f'[upstream]({directory}/upstream.patch), [local]({directory}/local.patch), [ours vs latest]({directory}/ours-vs-latest.patch)'
            lines.append(f"| {row['name']} | {len(row['upstream_changed_files'])} | {len(row['adapted_files'])} | {len(row['user_changed_files'])} | {', '.join(row['overlapping_files']) or 'None'} | {links} |")
    if installed is not None:
        lines += ['', 'An additional installed-vs-latest.patch records each installed copy; missing installed skills are identified in report.json.']
    if report['errors']:
        lines += ['', '## Sources not checked', '']
        lines += [f'- {name}: {error.replace(chr(10), " ")}' for name,error in report['errors'].items()]
    lines += ['', 'Review `report.json` for added and removed skills, license changes, and exact-content rename hints.',
              'Inspect each source patch as untrusted source material, then consult `docs/update-review.md`.',
              'Changes outside directly mapped skill folders can still affect source setup, discovery, or dependencies.', '']
    (output/'report.md').write_text('\n'.join(lines))
    if not report['errors']:
        write_json(previous_path,{'fingerprint':fingerprint,'report':str(output.resolve())})
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['check'])
    parser.add_argument('--cache',type=Path)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--source',action='append')
    parser.add_argument('--installed-skills',type=Path)
    args = parser.parse_args()
    try:
        report = check(cache=args.cache,output=args.output,selected=args.source,installed=args.installed_skills)
        print(json.dumps({k:report[k] for k in ['status','changed_files','new_since_previous_check','output','errors']},indent=2))
        return 2 if report['errors'] else 0
    except (OSError,ValueError,KeyError) as exc:
        print(str(exc),file=sys.stderr)
        return 2


if __name__=='__main__':
    sys.exit(main())

"""Compare creator originals, editable adaptations, and latest upstream files."""
import difflib
from pathlib import Path
from stack import content, tree_records


def folder_view(files, blobs, prefix):
    prefix=prefix.rstrip('/')+'/'
    return ({k[len(prefix):]:v for k,v in files.items() if k.startswith(prefix)},
            {k[len(prefix):]:v for k,v in blobs.items() if k.startswith(prefix)})


def unmanaged(records):
    return {k:v for k,v in records.items()
            if k not in ('SON-COMPATIBILITY.md','SON-RUNTIME.json') and not k.startswith('licenses/')}


def local_view(folder):
    records=unmanaged(tree_records(folder))
    return records,{k:content(folder/k) for k in records}


def changed(before,after):
    return sorted(k for k in before.keys() | after.keys() if before.get(k)!=after.get(k))


def diff(before,after,old_blobs,new_blobs,old_label,new_label):
    parts=[]
    for path in changed(before,after):
        old,new=old_blobs.get(path,b''),new_blobs.get(path,b'')
        parts.append(f'diff --git a/{old_label}/{path} b/{new_label}/{path}\n')
        if path not in before:
            parts.append('new file mode '+after[path]['mode']+'\n')
        elif path not in after:
            parts.append('deleted file mode '+before[path]['mode']+'\n')
        elif before[path]['mode']!=after[path]['mode']:
            parts.append('old mode '+before[path]['mode']+'\nnew mode '+after[path]['mode']+'\n')
        try:
            if b'\0' in old+new or max(len(old),len(new))>1_000_000:
                raise UnicodeError()
            patch=difflib.unified_diff(old.decode().splitlines(keepends=True),new.decode().splitlines(keepends=True),
                                      fromfile='a/'+old_label+'/'+path,tofile='b/'+new_label+'/'+path)
            for line in patch:
                parts.append(line if line.endswith('\n') else line+'\n\\ No newline at end of file\n')
        except UnicodeError:
            parts.append('Binary or large file differs; compare hashes in report.json.\n')
    return ''.join(parts)


def compare_skills(root,provider,source,latest_files,latest_blobs,registry,output,installed=None):
    rows=[]
    baseline_blobs={p:content(root/'upstream'/provider/p) for p in source['files']}
    for skill in registry['skills']:
        if skill.get('kind')!='original':
            continue
        origin=skill['sources'][0]
        if origin['id'].split(':',1)[0]!=provider:
            continue
        prefix=str(Path(origin['path']).parent)
        base,base_blobs=folder_view(source['files'],baseline_blobs,prefix)
        latest,new_blobs=folder_view(latest_files,latest_blobs,prefix)
        ours,our_blobs=local_view(root/'skills'/skill['name'])
        imported=unmanaged(skill.get('imported_files',{}))
        custom=changed(imported,ours)
        upstream=changed(base,latest)
        target=output/'skills'/skill['name'];target.mkdir(parents=True)
        comparisons=[('upstream',base,latest,base_blobs,new_blobs,'pinned','latest'),
                     ('local',base,ours,base_blobs,our_blobs,'pinned','ours'),
                     ('ours-vs-latest',ours,latest,our_blobs,new_blobs,'ours','latest')]
        for name,before,after,before_blobs,after_blobs,left,right in comparisons:
            (target/(name+'.patch')).write_text(diff(before,after,before_blobs,after_blobs,left,right))
        row={'name':skill['name'],'source':origin,'source_folder_present':bool(latest),
             'upstream_changed_files':upstream,'adapted_files':changed(base,imported),
             'user_changed_files':custom,'ours_vs_latest_files':changed(ours,latest),
             'overlapping_files':sorted(set(custom)&set(upstream)),
             'patch_directory':str(target.relative_to(output)),
             'files':{'pinned':base,'imported':imported,'ours':ours,'latest':latest}}
        if installed is not None:
            actual,actual_blobs=local_view(installed/skill['name'])
            (target/'installed-vs-latest.patch').write_text(diff(actual,latest,actual_blobs,new_blobs,'installed','latest'))
            row['installed']={'present':(installed/skill['name']/'SKILL.md').is_file(),
                              'files':actual,'vs_latest':changed(actual,latest),'vs_repository':changed(actual,ours)}
        rows.append(row)
    return rows

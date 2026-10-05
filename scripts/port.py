"""Small, deterministic adaptations of creator files; no workflow rewriting."""
import os
from pathlib import Path
import re

COMPAT = 'Read [Son compatibility](SON-COMPATIBILITY.md) before following this skill.\n\n'
RENAMES = {
    'matt': {'prototype':'matt-prototype','teach':'matt-teach','tdd':'matt-tdd'},
    'emil': {'prototype':'emil-prototype'},
    'pstack': {'teach':'pstack-teach','tdd':'pstack-tdd','poteto-mode':'son-mode',
               'poteto-agent':'son-agent','setup-pstack':'setup-son-skills','poteto-help':'son-mode'},
}


def name_for(provider, slug):
    return RENAMES.get(provider, {}).get(slug, slug)


def adapt_text(text, provider, source_path, destination_path, locations):
    """Change explicit skill references and resolvable links, leaving prose intact."""
    for old,new in RENAMES.get(provider,{}).items():
        for left,right in [('`','`'),('"','"'),("'","'"),('**','**')]:
            text=text.replace(left+old+right,left+new+right)
        text=re.sub(r'/'+re.escape(old)+r'(?![a-zA-Z0-9_-])','/'+new,text)
    def link(match):
        label,target=match.groups()
        if '://' in target or target.startswith(('#','mailto:')):
            return match.group(0)
        path,sep,anchor=target.partition('#')
        resolved=os.path.normpath(str(Path(source_path).parent/path))
        mapped=locations.get((provider,resolved))
        if mapped:
            target=os.path.relpath(mapped,Path(destination_path).parent).replace(os.sep,'/')
            return '['+label+']('+target+(sep+anchor if sep else '')+')'
        return match.group(0)
    return re.sub(r'\[([^\]]*)\]\(([^)]+)\)',link,text)


def entrypoint(text, name):
    if not text.startswith('---\n') or len(text.split('---',2))!=3:
        raise ValueError('Missing skill frontmatter: '+name)
    _,front,body=text.split('---',2)
    front=re.sub(r'^name:.*$', 'name: '+name,front,flags=re.M)
    return '---'+front+'---\n\n'+COMPAT+body.lstrip('\n')

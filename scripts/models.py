#!/usr/bin/env python3
"""Validate a live model inventory and save explicitly chosen Son role settings."""
import argparse
import json
from pathlib import Path
import sys
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
EFFORTS=['none','minimal','low','medium','high','xhigh','max','ultra']
BUDGETS={'small':'medium','medium':'high','large':'xhigh','unlimited':'max'}
ROLES=['planning','implementation','review','research','prose','ui']


def propose(inventory, choices, budget):
    if budget not in BUDGETS:
        raise ValueError('Unknown reasoning budget')
    if inventory.get('harness') not in ('codex','claude','cursor'):
        raise ValueError('Inventory must identify the active application')
    if not inventory.get('observed_at') or not inventory.get('evidence'):
        raise ValueError('Inventory needs a timestamp and live capability evidence')
    if set(choices.get('roles',{})) != set(ROLES):
        raise ValueError('Choose a model or inherit-parent for each role: '+', '.join(ROLES))
    models=inventory.get('models',{})
    def resolve(choice):
        model=choice['model'] if isinstance(choice,dict) else choice
        if model in ('inherit-parent','auto'):
            if isinstance(choice,dict) and choice.get('effort'):
                raise ValueError('Inherited models cannot promise a reasoning effort')
            return {'model':'inherit-parent','effort':None}
        if model not in models:
            raise ValueError('Model not advertised by this session: '+model)
        supported=models[model].get('efforts',[])
        if any(e not in EFFORTS for e in supported):
            raise ValueError('Unknown effort in inventory for '+model)
        effort=choice.get('effort') if isinstance(choice,dict) else None
        if effort is not None:
            if effort not in supported:
                raise ValueError('Unsupported model and effort pair: '+model+'/'+effort)
        elif supported:
            cap=EFFORTS.index(BUDGETS[budget])
            allowed=[e for e in supported if EFFORTS.index(e)<=cap]
            if not allowed:
                raise ValueError('No supported effort within budget for '+model)
            effort=max(allowed,key=EFFORTS.index)
        return {'model':model,'effort':effort}
    roles={role:resolve(choices['roles'][role]) for role in ROLES}
    panel=[resolve(c) for c in choices.get('panel',[])]
    return {'schema_version':1,'harness':inventory['harness'],'budget':budget,
            'target_effort':BUDGETS[budget],'roles':roles,'panel':panel,
            'availability_evidence':inventory['evidence'],'observed_at':inventory['observed_at'],
            'validated_at':datetime.now(timezone.utc).isoformat()}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--inventory',type=Path,required=True)
    p.add_argument('--choices',type=Path,required=True)
    p.add_argument('--budget',choices=BUDGETS,required=True)
    p.add_argument('--save',action='store_true',help='Save after the user accepts the displayed role table')
    args=p.parse_args()
    try:
        config=propose(json.loads(args.inventory.read_text()),json.loads(args.choices.read_text()),args.budget)
        if args.save:
            folder=ROOT/'.local'; folder.mkdir(exist_ok=True)
            output=folder/f"models.{config['harness']}.json"
            temp=output.with_suffix('.tmp'); temp.write_text(json.dumps(config,indent=2)+'\n'); temp.replace(output)
            config['saved_to']=str(output)
        print(json.dumps(config,indent=2))
        return 0
    except (OSError,ValueError,KeyError,TypeError) as exc:
        print(str(exc),file=sys.stderr); return 1


if __name__=='__main__':
    sys.exit(main())

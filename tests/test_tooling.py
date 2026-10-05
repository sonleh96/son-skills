"""Failure cases are documented in docs/test-plan.md before these tests."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import stack


class ToolingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='son-skills-test-')
        self.base = Path(self.temp.name)
        self.root = self.base/'stack'
        self.remote = self.base/'remote'
        self.remote.mkdir()
        self.run_git('init')
        self.put('LICENSE','MIT test fixture\n')
        self.put('skills/alpha/SKILL.md','---\nname: alpha\ndescription: Test fixture\n---\nOriginal behavior.\n')
        self.put('skills/old/SKILL.md','---\nname: old\ndescription: Old fixture\n---\nOld behavior.\n')
        self.commit()
        self.root.mkdir()
        shutil.copytree(ROOT/'scripts',self.root/'scripts',ignore=shutil.ignore_patterns('__pycache__'))
        source_files = {}
        for name in ['LICENSE','skills/alpha/SKILL.md','skills/old/SKILL.md']:
            target = self.root/'upstream'/'fixture'/name
            target.parent.mkdir(parents=True,exist_ok=True)
            data = (self.remote/name).read_bytes()
            target.write_bytes(data)
            source_files[name] = {'sha256':hashlib.sha256(data).hexdigest(),'mode':'100644','size':len(data)}
        self.lock = {'schema_version':1,'sources':{'fixture':{
            'url':self.remote.as_uri(),'ref':'HEAD','scope':'',
            'commit':self.run_git('rev-parse','HEAD').strip(),
            'license':'MIT','license_path':'LICENSE','author':'Fixture','files':source_files}}}
        self.write_json('sources.lock.json',self.lock)
        self.skill = {'name':'son-fixture','category':'test','description':'Use when testing portable fixture bundles.',
                      'explicit_only':True,'sources':[{'id':'fixture:alpha','path':'skills/alpha/SKILL.md'}]}
        self.write_json('stack.json',{'schema_version':1,'skills':[self.skill]})
        folder=self.root/'skills'/'son-fixture'
        (folder/'agents').mkdir(parents=True)
        (folder/'references').mkdir()
        (folder/'SKILL.md').write_text('---\nname: son-fixture\ndescription: '+json.dumps(self.skill['description'])+'\ndisable-model-invocation: true\n---\nRead `references/rules.md`.\n')
        (folder/'agents'/'openai.yaml').write_text('policy:\n  allow_implicit_invocation: false\n')
        (self.root/'policies').mkdir()
        (self.root/'policies'/'rules.md').write_text('A portable rule.\n')
        (folder/'references'/'rules.md').symlink_to('../../../policies/rules.md')

    def tearDown(self):
        self.temp.cleanup()

    def run_git(self,*args):
        return subprocess.check_output(['git','-C',str(self.remote),*args],text=True,stderr=subprocess.DEVNULL)

    def put(self,name,text):
        p=self.remote/name
        p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(text)

    def commit(self):
        self.run_git('add','.')
        self.run_git('-c','user.name=Test Fixture','-c','user.email=fixture@example.invalid',
                     '-c','commit.gpgsign=false','commit','-m','Fixture state')

    def write_json(self,name,obj):
        (self.root/name).write_text(json.dumps(obj,indent=2)+'\n')

    def check(self):
        completed=subprocess.run([sys.executable,str(self.root/'scripts'/'upstream.py'),'check'],
                                 capture_output=True,text=True,timeout=40)
        output=json.loads(completed.stdout)
        report=json.loads((Path(output['output'])/'report.json').read_text())
        return completed,report

    def test_f1_modified_baseline_is_rejected(self):
        (self.root/'upstream'/'fixture'/'LICENSE').write_text('tampered')
        result=subprocess.run([sys.executable,str(self.root/'scripts'/'upstream.py'),'check'],capture_output=True,text=True)
        self.assertEqual(result.returncode,2)
        self.assertIn('snapshot drift',result.stderr)
        self.assertFalse((self.root/'reviews').exists())

    def test_f2_changes_licenses_modes_and_renames_are_reported(self):
        self.put('LICENSE','MIT test fixture, changed attribution\n')
        self.put('skills/alpha/SKILL.md','---\nname: alpha\ndescription: Test fixture\n---\nChanged behavior.\n')
        (self.remote/'skills'/'alpha'/'SKILL.md').chmod(0o755)
        old=self.remote/'skills'/'old'/'SKILL.md'
        new=self.remote/'skills'/'new'/'SKILL.md'
        new.parent.mkdir()
        old.rename(new)
        self.commit()
        result,report=self.check()
        self.assertEqual(result.returncode,0,result.stderr)
        source=report['sources']['fixture']
        self.assertEqual(source['changed_files'],4)
        self.assertEqual(source['added_skills'],['skills/new/SKILL.md'])
        self.assertEqual(source['removed_skills'],['skills/old/SKILL.md'])
        self.assertEqual(source['rename_hints'],[{'from':'skills/old/SKILL.md','to':'skills/new/SKILL.md'}])
        self.assertTrue(source['license_changed'])
        self.assertEqual(source['affected_combined_skills'],['son-fixture'])
        patch=(Path(report['output'])/'fixture.patch').read_text()
        self.assertIn('+Changed behavior.',patch)
        self.assertIn('new mode 100755',patch)

    def test_f3_out_of_scope_commit_has_no_content_change(self):
        source=self.lock['sources']['fixture']
        source['scope']='skills'
        self.put('skills/LICENSE','MIT test fixture\n')
        self.commit()
        src=self.root/'upstream'/'fixture'
        (src/'LICENSE').rename(src/'skills'/'LICENSE')
        source['files']['skills/LICENSE']=source['files'].pop('LICENSE')
        source['license_path']='skills/LICENSE'
        source['commit']=self.run_git('rev-parse','HEAD').strip()
        self.write_json('sources.lock.json',self.lock)
        self.put('unrelated.txt','Outside the selected scope.\n')
        self.commit()
        result,report=self.check()
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(report['status'],'unchanged')
        self.assertEqual(report['changed_files'],0)
        self.assertNotEqual(report['sources']['fixture']['accepted_commit'],report['sources']['fixture']['observed_commit'])

    def test_f4_failed_remote_keeps_partial_report_and_fails_exit(self):
        self.lock['sources']['broken']=dict(self.lock['sources']['fixture'])
        self.lock['sources']['broken']['url']=(self.base/'missing-remote').as_uri()
        shutil.copytree(self.root/'upstream'/'fixture',self.root/'upstream'/'broken')
        self.write_json('sources.lock.json',self.lock)
        result,report=self.check()
        self.assertEqual(result.returncode,2)
        self.assertEqual(report['status'],'failed')
        self.assertIn('broken',report['errors'])
        self.assertIn('fixture',report['sources'])

    def test_f5_collision_preflight_does_not_overwrite(self):
        extra=dict(self.skill,name='son-aaa')
        self.write_json('stack.json',{'schema_version':1,'skills':[extra,self.skill]})
        shutil.copytree(self.root/'skills'/'son-fixture',self.root/'skills'/'son-aaa',symlinks=True)
        entry=self.root/'skills'/'son-aaa'/'SKILL.md'
        entry.write_text(entry.read_text().replace('name: son-fixture','name: son-aaa'))
        destination=self.base/'installed'
        destination.mkdir()
        existing=destination/'son-fixture'
        existing.mkdir()
        (existing/'SKILL.md').write_text('User work.\n')
        with self.assertRaisesRegex(ValueError,'nothing installed'):
            stack.install(destination,apply=True,root=self.root)
        self.assertEqual((existing/'SKILL.md').read_text(),'User work.\n')
        self.assertEqual(sorted(p.name for p in destination.iterdir()),['son-fixture'])

    def test_f6_bundles_are_self_contained_and_install_is_idempotent(self):
        destination=self.base/'installed'
        preview=stack.install(destination,root=self.root)
        self.assertEqual(preview['mode'],'preview')
        self.assertFalse(destination.exists())
        stack.install(destination,apply=True,root=self.root)
        rule=destination/'son-fixture'/'references'/'rules.md'
        self.assertFalse(rule.is_symlink())
        self.assertEqual(rule.read_text(),'A portable rule.\n')
        self.assertEqual((destination/'son-fixture'/'licenses'/'fixture.txt').read_text(),'MIT test fixture\n')
        second=stack.install(destination,apply=True,root=self.root)
        self.assertEqual(second['already_identical'],1)
        self.assertEqual(second['new_skills'],[])
        self.assertNotIn('disable-model-invocation:',(destination/'son-fixture'/'SKILL.md').read_text())
        self.assertIn('allow_implicit_invocation: false',(destination/'son-fixture'/'agents'/'openai.yaml').read_text())
        stack.build(root=self.root,harness='claude')
        self.assertIn('disable-model-invocation: true',(self.root/'.build'/'claude'/'skills'/'son-fixture'/'SKILL.md').read_text())

    def test_f7_repeat_check_deduplicates_without_moving_baseline(self):
        before=(self.root/'sources.lock.json').read_bytes()
        self.put('skills/alpha/SKILL.md','New behavior.\n')
        self.commit()
        _,first=self.check()
        _,second=self.check()
        self.assertTrue(first['new_since_previous_check'])
        self.assertFalse(second['new_since_previous_check'])
        self.assertEqual(second['status'],'changes')
        self.assertEqual((self.root/'sources.lock.json').read_bytes(),before)
        self.assertIn('Original behavior.',(self.root/'upstream'/'fixture'/'skills'/'alpha'/'SKILL.md').read_text())

    def test_f8_unsafe_paths_are_rejected(self):
        for path in ['../escape','/absolute','a/../../escape','']:
            with self.subTest(path=path),self.assertRaises(ValueError):
                stack.safe_relative(path)
        outside=self.base/'private.md'
        outside.write_text('Outside snapshot.\n')
        link=self.root/'upstream'/'fixture'/'escaped.md'
        link.symlink_to(outside)
        data=os.readlink(link).encode()
        self.lock['sources']['fixture']['files']['escaped.md']={'sha256':hashlib.sha256(data).hexdigest(),'mode':'120000','size':len(data)}
        self.write_json('sources.lock.json',self.lock)
        with self.assertRaisesRegex(ValueError,'symlink escapes'):
            stack.validate(self.root)

    def test_f9_invocation_policy_drift_is_rejected(self):
        meta=self.root/'skills'/'son-fixture'/'agents'/'openai.yaml'
        meta.write_text('policy:\n  allow_implicit_invocation: true\n')
        with self.assertRaisesRegex(ValueError,'invocation policy mismatch'):
            stack.validate(self.root)


if __name__=='__main__':
    unittest.main()

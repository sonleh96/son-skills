"""Filesystem tests for the portable global instruction installer.

Failure modes covered:
1. Preview accidentally writes files.
2. Apply renders the source and creates relative aliases.
3. A second apply is not idempotent.
4. A late conflict leaves earlier targets untouched.
5. Regular files, directories, wrong symlinks, and dangling symlinks are refused.
6. A matching canonical symlink is kept while a canonical symlink cycle is rejected.
7. Invalid homes are rejected.
8. Required companion limitations are reported.
9. The Claude template alias is no longer a relative symlink to AGENTS.md.
10. Retargeting a canonical AGENTS.md symlink updates both application aliases.
"""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "instructions.py"
sys.path.insert(0, str(ROOT / "scripts"))
import instructions


class InstructionsInstallerTests(unittest.TestCase):
    def run_cli(self, home, *options):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--home", str(home), *options],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_claude_template_alias_is_relative(self):
        alias = ROOT / "instructions" / "CLAUDE.md"
        self.assertTrue(alias.is_symlink())
        self.assertEqual(os.readlink(alias), "AGENTS.md")

    def test_preview_writes_nothing_and_reports_external_prerequisites(self):
        with tempfile.TemporaryDirectory() as temporary:
            home = Path(temporary) / "home" / "linux-user"
            home.mkdir(parents=True)
            result = self.run_cli(home)
            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads(result.stdout)
            self.assertEqual(report["mode"], "preview")
            self.assertFalse((home / "AGENTS.md").exists())
            self.assertFalse((home / ".codex").exists())
            self.assertFalse((home / ".claude").exists())
            limitations = " ".join(report["limitations"])
            for required in ["model-policy.md", "agent-memory.md", "cross-harness-handoffs.md", "unslop", "model catalogs"]:
                self.assertIn(required, limitations)

    def test_apply_renders_source_and_creates_relative_aliases(self):
        with tempfile.TemporaryDirectory() as temporary:
            home = Path(temporary) / "home" / "linux-user"
            home.mkdir(parents=True)
            result = self.run_cli(home, "--apply")
            self.assertEqual(result.returncode, 0, result.stderr)
            expected = instructions.TEMPLATE.read_text(encoding="utf-8").replace("${SON_HOME}", str(home))
            canonical = home / "AGENTS.md"
            codex = home / ".codex" / "AGENTS.md"
            claude = home / ".claude" / "CLAUDE.md"
            self.assertEqual(canonical.read_text(encoding="utf-8"), expected)
            self.assertTrue(codex.is_symlink())
            self.assertTrue(claude.is_symlink())
            self.assertEqual(os.readlink(codex), "../AGENTS.md")
            self.assertEqual(os.readlink(claude), "../AGENTS.md")
            self.assertEqual(codex.resolve(), canonical.resolve())
            self.assertEqual(claude.resolve(), canonical.resolve())

    def test_second_apply_is_idempotent(self):
        with tempfile.TemporaryDirectory() as temporary:
            home = Path(temporary) / "home"
            home.mkdir()
            first = self.run_cli(home, "--apply")
            self.assertEqual(first.returncode, 0, first.stderr)
            paths = [home / "AGENTS.md", home / ".codex" / "AGENTS.md", home / ".claude" / "CLAUDE.md"]
            before = [(path.lstat().st_mtime_ns, os.readlink(path) if path.is_symlink() else path.read_bytes()) for path in paths]
            second = self.run_cli(home, "--apply")
            self.assertEqual(second.returncode, 0, second.stderr)
            report = json.loads(second.stdout)
            self.assertEqual(report["changes"], [])
            self.assertEqual(len(report["unchanged"]), 3)
            after = [(path.lstat().st_mtime_ns, os.readlink(path) if path.is_symlink() else path.read_bytes()) for path in paths]
            self.assertEqual(after, before)

    def test_late_conflict_causes_zero_earlier_writes(self):
        with tempfile.TemporaryDirectory() as temporary:
            home = Path(temporary) / "home"
            home.mkdir()
            conflict = home / ".claude" / "CLAUDE.md"
            conflict.mkdir(parents=True)
            result = self.run_cli(home, "--apply")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("no files changed", result.stderr)
            self.assertFalse((home / "AGENTS.md").exists())
            self.assertFalse((home / ".codex").exists())
            self.assertTrue(conflict.is_dir())

    def test_conflicts_leave_all_existing_paths_unchanged(self):
        cases = [
            ("canonical regular file", lambda home: (home / "AGENTS.md").write_text("different\n")),
            ("canonical directory", lambda home: (home / "AGENTS.md").mkdir()),
            ("canonical wrong symlink", self.make_canonical_wrong_symlink),
            ("canonical dangling symlink", self.make_canonical_dangling_symlink),
            ("alias regular file", self.make_alias_regular_conflict),
            ("alias directory", self.make_alias_directory_conflict),
            ("alias wrong symlink", self.make_alias_wrong_symlink),
            ("alias dangling symlink", self.make_alias_dangling_symlink),
        ]
        for name, setup in cases:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as temporary:
                home = Path(temporary) / "home"
                home.mkdir()
                setup(home)
                canonical = home / "AGENTS.md"
                if canonical.is_symlink():
                    before = ("symlink", os.readlink(canonical))
                elif canonical.is_file():
                    before = ("file", canonical.read_bytes())
                elif canonical.is_dir():
                    before = ("directory", None)
                else:
                    before = None
                result = self.run_cli(home, "--apply")
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("no files changed", result.stderr)
                if before is None:
                    self.assertFalse(instructions.present(canonical))
                elif before[0] == "symlink":
                    self.assertTrue(canonical.is_symlink())
                    self.assertEqual(os.readlink(canonical), before[1])
                elif before[0] == "file":
                    self.assertEqual(canonical.read_bytes(), before[1])
                else:
                    self.assertTrue(canonical.is_dir())
                self.assertFalse((home / ".claude").exists())

    @staticmethod
    def make_canonical_wrong_symlink(home):
        target = home / "wrong.md"
        target.write_text("wrong\n")
        (home / "AGENTS.md").symlink_to(target)

    @staticmethod
    def make_canonical_dangling_symlink(home):
        (home / "AGENTS.md").symlink_to("missing.md")

    @staticmethod
    def make_alias_regular_conflict(home):
        alias = home / ".codex" / "AGENTS.md"
        alias.parent.mkdir()
        alias.write_text("different\n")

    @staticmethod
    def make_alias_directory_conflict(home):
        (home / ".codex" / "AGENTS.md").mkdir(parents=True)

    @staticmethod
    def make_alias_wrong_symlink(home):
        alias = home / ".codex" / "AGENTS.md"
        alias.parent.mkdir()
        target = home / "wrong.md"
        target.write_text("wrong\n")
        alias.symlink_to(target)

    @staticmethod
    def make_alias_dangling_symlink(home):
        alias = home / ".codex" / "AGENTS.md"
        alias.parent.mkdir()
        alias.symlink_to("missing.md")

    def test_canonical_symlink_cycle_is_rejected_before_writes(self):
        with tempfile.TemporaryDirectory() as temporary:
            home = Path(temporary) / "home"
            home.mkdir()
            canonical = home / "AGENTS.md"
            codex = home / ".codex" / "AGENTS.md"
            codex.parent.mkdir()
            canonical.symlink_to(".codex/AGENTS.md")
            codex.symlink_to("../AGENTS.md")
            result = self.run_cli(home, "--apply")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("cyclic", result.stderr)
            self.assertFalse((home / ".claude").exists())
            self.assertEqual(os.readlink(canonical), ".codex/AGENTS.md")
            self.assertEqual(os.readlink(codex), "../AGENTS.md")

    def test_matching_canonical_symlink_is_kept(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            home = base / "home"
            home.mkdir()
            expected = instructions.TEMPLATE.read_text(encoding="utf-8").replace("${SON_HOME}", str(home))
            shared = base / "shared-agents.md"
            shared.write_text(expected, encoding="utf-8")
            canonical = home / "AGENTS.md"
            canonical.symlink_to(shared)
            result = self.run_cli(home, "--apply")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(canonical.is_symlink())
            self.assertEqual(os.readlink(canonical), str(shared))
            self.assertEqual((home / ".codex" / "AGENTS.md").resolve(), canonical.resolve())
            self.assertEqual((home / ".claude" / "CLAUDE.md").resolve(), canonical.resolve())

    def test_aliases_follow_canonical_retarget(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            home = base / "home"
            dotfiles = base / "dotfiles"
            home.mkdir()
            dotfiles.mkdir()
            expected = instructions.render(home)
            version_one = dotfiles / "v1.md"
            version_two = dotfiles / "v2.md"
            version_one.write_text(expected, encoding="utf-8")
            version_two.write_text("version two guidance\n", encoding="utf-8")
            canonical = home / "AGENTS.md"
            canonical.symlink_to("../dotfiles/v1.md")

            result = self.run_cli(home, "--apply")

            self.assertEqual(result.returncode, 0, result.stderr)
            codex = home / ".codex" / "AGENTS.md"
            claude = home / ".claude" / "CLAUDE.md"
            self.assertEqual(os.readlink(codex), "../AGENTS.md")
            self.assertEqual(os.readlink(claude), "../AGENTS.md")
            canonical.unlink()
            canonical.symlink_to("../dotfiles/v2.md")
            self.assertEqual(codex.resolve(), version_two.resolve())
            self.assertEqual(claude.resolve(), version_two.resolve())
            self.assertEqual(codex.read_text(encoding="utf-8"), "version two guidance\n")
            self.assertEqual(claude.read_text(encoding="utf-8"), "version two guidance\n")

    def test_invalid_home_fails_before_writes(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            file_home = base / "not-a-home"
            file_home.write_text("file\n")
            for value in ["relative-home", str(file_home), str(base / "missing")]:
                with self.subTest(value=value):
                    result = self.run_cli(value, "--apply")
                    self.assertNotEqual(result.returncode, 0)
                    self.assertFalse((base / "AGENTS.md").exists())


if __name__ == "__main__":
    unittest.main()

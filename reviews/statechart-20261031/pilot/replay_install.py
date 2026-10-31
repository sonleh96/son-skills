#!/usr/bin/env python3
"""Exercise the real stack installer against fresh temporary destinations."""
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent / "repo"
sys.path.insert(0, str(ROOT / "scripts"))
import stack


BASE = ROOT.parent / "replay"


def digest(folder: Path) -> str:
    h = hashlib.sha256()
    for path in sorted(folder.rglob("*")):
        if not (path.is_file() or path.is_symlink()):
            continue
        h.update(path.relative_to(folder).as_posix().encode())
        h.update(b"\0")
        h.update(stack.content(path))
        h.update(b"\0")
    return h.hexdigest()


def main() -> None:
    preview_root = BASE / "preview"
    preview = stack.install(preview_root / "skills", root=ROOT, harness="cursor")
    assert not preview_root.exists(), "preview mutated its destination"

    fresh_root = BASE / "fresh"
    first = stack.install(fresh_root / "skills", apply=True, root=ROOT, harness="cursor")
    installed = fresh_root / "skills"
    entry = installed / "statechart" / "SKILL.md"
    route = installed / "son-mode" / "references" / "statechart-routing.md"
    assert entry.is_file()
    assert route.is_file()
    assert not route.is_symlink()
    assert (installed / "statechart" / "SON-RUNTIME.json").is_file()
    assert entry.read_bytes() == (ROOT / "skills" / "statechart" / "SKILL.md").read_bytes()
    assert route.read_bytes() == (ROOT / "skills" / "son-mode" / "references" / "statechart-routing.md").read_bytes()
    before_repeat = digest(fresh_root)
    second = stack.install(fresh_root / "skills", apply=True, root=ROOT, harness="cursor")
    after_repeat = digest(fresh_root)
    assert second["new_skills"] == []
    assert second["already_identical"] >= len(first["new_skills"])
    assert before_repeat == after_repeat, "repeat install changed destination bytes"

    conflict_root = BASE / "conflict"
    conflict_skills = conflict_root / "skills"
    conflict_entry = conflict_skills / "statechart" / "SKILL.md"
    conflict_entry.parent.mkdir(parents=True)
    conflict_entry.write_text("User work.\n")
    sentinel = conflict_root / "sentinel.txt"
    sentinel.write_text("keep me\n")
    try:
        stack.install(conflict_skills, apply=True, root=ROOT, harness="cursor")
    except ValueError as error:
        conflict_error = str(error)
        assert "nothing installed" in conflict_error
    else:
        raise AssertionError("conflicting statechart destination was accepted")
    assert conflict_entry.read_text() == "User work.\n"
    assert sentinel.read_text() == "keep me\n"
    assert not (conflict_skills / "son-mode").exists()
    assert not (conflict_root / "agents").exists()

    result = {
        "root": str(ROOT),
        "preview": preview,
        "first_apply": first,
        "second_apply": second,
        "repeat_digest": after_repeat,
        "conflict_error": conflict_error,
        "observed": {
            "preview_destination_absent": True,
            "fresh_statechart_present": True,
            "route_materialized": True,
            "repeat_bytes_unchanged": before_repeat == after_repeat,
            "conflict_destination_unchanged": True,
        },
    }
    output = BASE / "replay.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

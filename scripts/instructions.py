#!/usr/bin/env python3
"""Preview or install the portable global instruction files."""

import argparse
import json
import os
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "instructions" / "AGENTS.md"
PLACEHOLDER = "${SON_HOME}"
LIMITATIONS = [
    "Required companion files are not bundled: model-policy.md, agent-memory.md as the memory index, and cross-harness-handoffs.md.",
    "The installed unslop skill is a prerequisite and is not bundled.",
    "This installer does not rewrite model catalogs or install auth, config, memory, or hooks.",
]


def present(path):
    """Return whether a path exists, including a dangling symlink."""
    return path.exists() or path.is_symlink()


def validate_home(value):
    """Return an existing absolute directory suitable as a home."""
    try:
        home = Path(value).expanduser()
    except (OSError, RuntimeError) as exc:
        raise ValueError(f"Invalid home path: {value}") from exc
    if not home.is_absolute():
        raise ValueError(f"Home must be an absolute path: {value}")
    home = home.absolute()
    try:
        resolved = home.resolve(strict=True)
    except (OSError, RuntimeError) as exc:
        raise ValueError(f"Home path is missing or cyclic: {home}") from exc
    if not resolved.is_dir() or resolved == Path(resolved.anchor):
        raise ValueError(f"Home must be a non-root directory: {home}")
    return home


def render(home):
    """Render the portable template for an absolute home path."""
    try:
        template = TEMPLATE.read_text(encoding="utf-8")
    except OSError as exc:
        raise ValueError(f"Cannot read instruction template: {TEMPLATE}") from exc
    if PLACEHOLDER not in template:
        raise ValueError(f"Instruction template lacks {PLACEHOLDER}: {TEMPLATE}")
    return template.replace(PLACEHOLDER, str(home))


def resolve_existing(path, label):
    """Resolve an existing path or report a dangling or cyclic symlink."""
    try:
        return path.resolve(strict=True)
    except (OSError, RuntimeError) as exc:
        raise ValueError(f"{label} is a dangling or cyclic symlink: {path}") from exc


def add_issue(issues, message):
    issues.append(message)


def validate_parent(parent, issues):
    """Check an alias parent without creating it."""
    if not present(parent):
        return False
    if parent.is_symlink():
        try:
            resolved = resolve_existing(parent, "Alias parent")
        except ValueError as exc:
            add_issue(issues, str(exc))
            return True
        if not resolved.is_dir():
            add_issue(issues, f"Alias parent is not a directory: {parent}")
        return True
    if not parent.is_dir():
        add_issue(issues, f"Alias parent conflicts with a non-directory: {parent}")
    return True


def inspect_canonical(canonical, expected, issues):
    """Check the canonical file and return its resolved path when usable."""
    if not present(canonical):
        return None, "missing"
    if canonical.is_symlink():
        try:
            resolved = resolve_existing(canonical, "Canonical AGENTS.md")
        except ValueError as exc:
            add_issue(issues, str(exc))
            return None, "conflict"
        try:
            matches = resolved.is_file() and canonical.read_bytes() == expected
        except OSError:
            matches = False
        if not matches:
            add_issue(issues, f"Canonical symlink has different readable contents: {canonical}")
            return None, "conflict"
        return resolved, "unchanged"
    if not canonical.is_file():
        add_issue(issues, f"Canonical path conflicts with a directory or special file: {canonical}")
        return None, "conflict"
    try:
        matches = canonical.read_bytes() == expected
    except OSError:
        matches = False
    if not matches:
        add_issue(issues, f"Canonical file differs: {canonical}")
        return None, "conflict"
    return resolve_existing(canonical, "Canonical AGENTS.md"), "unchanged"


def inspect_alias(alias, canonical_resolved, expected, issues):
    """Check an alias and return its planned action."""
    if not present(alias):
        return {"kind": "symlink", "path": alias, "target": None}
    if alias.is_symlink():
        try:
            resolved = resolve_existing(alias, "Instruction alias")
        except ValueError as exc:
            add_issue(issues, str(exc))
            return None
        if canonical_resolved is None or resolved != canonical_resolved:
            add_issue(issues, f"Instruction alias does not resolve to canonical AGENTS.md: {alias}")
            return None
        return None
    if not alias.is_file():
        add_issue(issues, f"Instruction alias conflicts with a directory or special file: {alias}")
        return None
    try:
        matches = alias.read_bytes() == expected
    except OSError:
        matches = False
    if not matches:
        add_issue(issues, f"Instruction alias file differs: {alias}")
    return None


def plan(home):
    """Preflight all targets and return a write plan."""
    home = validate_home(home)
    rendered = render(home)
    expected = rendered.encode("utf-8")
    canonical = home / "AGENTS.md"
    aliases = [home / ".codex" / "AGENTS.md", home / ".claude" / "CLAUDE.md"]
    issues = []
    parent_present = [validate_parent(alias.parent, issues) for alias in aliases]
    canonical_resolved, canonical_state = inspect_canonical(canonical, expected, issues)

    try:
        canonical_physical = canonical.resolve(strict=False)
    except (OSError, RuntimeError) as exc:
        add_issue(issues, f"Canonical path is cyclic: {canonical}")
        canonical_physical = canonical

    operations = []
    unchanged = []
    if canonical_state == "missing":
        operations.append({"kind": "file", "path": canonical, "content": expected})
    elif canonical_state == "unchanged":
        unchanged.append(canonical)

    for alias, parent_exists in zip(aliases, parent_present):
        before = len(issues)
        action = inspect_alias(alias, canonical_resolved, expected, issues)
        if action is not None:
            try:
                parent_physical = alias.parent.resolve(strict=True if parent_exists else False)
                action["target"] = os.path.relpath(canonical_physical, parent_physical)
            except (OSError, RuntimeError, ValueError) as exc:
                add_issue(issues, f"Cannot create a relative instruction alias: {alias}")
                action = None
            if action is not None:
                operations.append(action)
        elif len(issues) == before and present(alias):
            unchanged.append(alias)

    if canonical_resolved is not None:
        for alias, parent_exists in zip(aliases, parent_present):
            if not present(alias):
                try:
                    physical_alias = alias.parent.resolve(strict=True if parent_exists else False) / alias.name
                except (OSError, RuntimeError):
                    continue
                if physical_alias == canonical_resolved:
                    add_issue(issues, f"Alias path resolves to the canonical path: {alias}")
    elif canonical_state == "missing":
        for alias, parent_exists in zip(aliases, parent_present):
            if not present(alias) and parent_exists:
                try:
                    physical_alias = alias.parent.resolve(strict=True if parent_exists else False) / alias.name
                except (OSError, RuntimeError):
                    continue
                if physical_alias == canonical_physical:
                    add_issue(issues, f"Alias path resolves to the canonical path: {alias}")

    if issues:
        unique_issues = list(dict.fromkeys(issues))
        detail = "\n".join(f"- {issue}" for issue in unique_issues)
        raise ValueError(f"Preflight failed; no files changed:\n{detail}")

    directories = []
    for alias, exists in zip(aliases, parent_present):
        if not exists:
            directories.append(alias.parent)
    return {
        "home": home,
        "canonical": canonical,
        "aliases": aliases,
        "expected": expected,
        "operations": operations,
        "directories": directories,
        "unchanged": unchanged,
    }


def apply_plan(instructions_plan):
    """Apply a plan without replacing any existing path."""
    for directory in instructions_plan["directories"]:
        directory.mkdir()
    for operation in instructions_plan["operations"]:
        path = operation["path"]
        if operation["kind"] == "file":
            with path.open("xb") as stream:
                stream.write(operation["content"])
        else:
            os.symlink(operation["target"], path)


def summary(instructions_plan, mode):
    """Return a JSON-safe report."""
    changes = []
    for directory in instructions_plan["directories"]:
        changes.append({"path": str(directory), "action": "create directory"})
    for operation in instructions_plan["operations"]:
        change = {"path": str(operation["path"]), "action": "create " + operation["kind"]}
        if operation["kind"] == "symlink":
            change["target"] = operation["target"]
        changes.append(change)
    return {
        "mode": mode,
        "home": str(instructions_plan["home"]),
        "changes": changes,
        "unchanged": [str(path) for path in instructions_plan["unchanged"]],
        "limitations": LIMITATIONS,
    }


def run(home, apply=False):
    """Build a plan and optionally apply it."""
    instructions_plan = plan(home)
    if apply:
        apply_plan(instructions_plan)
    return summary(instructions_plan, "applied" if apply else "preview")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--home", default=None, help="Absolute home directory. Defaults to the current user home.")
    parser.add_argument("--apply", action="store_true", help="Write the preflighted files. Preview is the default.")
    args = parser.parse_args(argv)
    home = Path.home() if args.home is None else args.home
    try:
        result = run(home, apply=args.apply)
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())

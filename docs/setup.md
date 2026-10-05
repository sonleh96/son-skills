# Set up the personal stack

The repository is local-first and usable across Lemi, banking, coursework, personal, and other repositories.
It does not encode a Lemi tracker, branch convention, deployment target, or model catalog.
No existing global skills were replaced during creation.

## Build the right format

From the repository root:

```bash
python3 scripts/stack.py validate
python3 scripts/stack.py build --harness codex
python3 scripts/stack.py build --harness claude
python3 scripts/stack.py build --harness cursor
```

The outputs are `.build/codex/skills`, `.build/claude/skills`, and `.build/cursor/skills`.
All carry self-contained reference files, original license notices, and pinned provenance.
Codex uses `agents/openai.yaml` for explicit-only selection.
Claude and Cursor retain their frontmatter setting.
The source checkout preserves both forms so a build cannot silently turn a manual workflow into an automatic one.

## Preview installation

Choose the active application's destination rather than installing duplicate copies through several discovery roots.
These commands only preview the operation:

```bash
python3 scripts/stack.py install --harness codex --dest "$HOME/.codex/skills"
python3 scripts/stack.py install --harness claude --dest "$HOME/.claude/skills"
python3 scripts/stack.py install --harness cursor --dest "$HOME/.cursor/skills"
```

For a repository-local installation, use its actual skill directory as `--dest`.
When installation is desired, repeat the chosen command with `--apply`.
The installer checks every destination first and refuses to overwrite any differing skill.
Identical copies are a no-op.
For a later version, review and back up existing `son-` directories before replacing them; the initial installer intentionally has no force option.

Do not run a recursive bulk installer over `upstream/`.
That would discover the original stacks and reintroduce conflicting names, orchestration, and policies.
Use the built combined skills.

## Per-project setup

1. Read the project's instructions and existing tooling.
2. Reuse its actual issue tracker, labels, docs directories, and validation commands.
3. If no tracker is configured, keep specs and tickets as local documents.
4. Read `GLOSSARY.md` or `GLOSSARY-MAP.md` when present.
   Create glossary content only when a term has been resolved.
5. Read Son's canonical model policy when a task requires model selection.
   Do not copy pstack model slugs or write a competing model rule.
6. Use the installed personal `unslop` skill for prose.

Matt's original setup skill remains in the snapshot for reference.
The combined stack does not require running it before a local spec or review.
Tracker-driven triage remains deferred until its states and roles are configured for a real project.

## What is and is not verified

The tooling has been exercised with real temporary Git repositories and a live check of all four upstreams.
Built Codex skills are checked with the installed skill-creator validator.
The formats preserve each application's intended invocation metadata.
Actual discovery and task quality in fresh Codex, Claude Code, and Cursor sessions still need a pilot after installation.

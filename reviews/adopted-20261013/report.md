# October adoption verification

The stack contains 97 creator skills and three Son controls.
The adoption decisions and exact commits are in [the update note](../../docs/updates/2026-10-13.md).

## Passed

- Snapshot, source mapping, invocation metadata and registry validation.
- All 16 Python tooling tests, including the reproduced prototype adapter regression.
- Five upstream plan-fence tests using Node's test runner against the actual checker.
- Wizard quote round-trip, new-file mode 0600, symlink preservation and EOF failure checks using the actual library.
- Shell syntax checks for wizard and worktree-audit, and Node syntax checks for changed PR watcher files.
- Codex, Claude Code and Cursor builds, each containing 100 skills.
- Codex and Claude installation preflight against the previous committed build, with no unreviewed installed drift.
- Both installations match 99 built skills; each personal unslop remains unchanged.
- Native Codex discovery reports all 100 expected names enabled with no discovery errors.
- Protected hashes confirm unchanged global model policy, saved model configuration, global instructions, Codex configuration, Claude settings and writing skill entry points.
- RPI is absent from both installations, and the HumanLayer accepted pin remains unchanged.
- README link checks and Git whitespace checks.

## Preserved copies

Replaced skills are backed up under each application's skill-backups/son-skills-20261013 directory.
The previous installed source was checked before moving any copy.
New duplicate files with 2 suffixes appeared during rebuilding.
They are preserved in the ignored .local/update-20261013/duplicate-copies directory and excluded from tracked source snapshots.
Their paths are recorded in duplicate-copies.json.

## Limits

Review was sequential self-review.
No new skill was evaluated against a live product task.
Claude Code installation was verified by file contents and invocation metadata, without a new Claude model session.
The full Bun PR watcher suite did not run because Bun is unavailable.
The Cursor bundle was built but not installed.

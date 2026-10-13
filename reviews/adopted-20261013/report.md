# October adoption verification

The stack contains 97 creator skills and three Son controls.
The adoption decisions and exact commits are in [the update note](../../docs/updates/2026-10-13.md).

## Passed

- Snapshot, source mapping, invocation metadata and registry validation.
- All 16 Python tooling tests, including the reproduced prototype adapter regression.
- All 63 Bun tests across the PR watcher, orchestration store and CLI, and plan-fence checker.
- Strict TypeScript checking for the complete PR watcher.
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

## Full Bun verification

On 13 October 2026, installed Bun 1.4.3, revision `1.4.3+c6da4a4d3`, through the [official Homebrew tap](https://bun.sh/docs/installation).
Copied the repository helper directory into `.cache/bun-watcher-20261013` and installed its existing dependencies with `bun install --frozen-lockfile`.
The copy isolates dependency files from the source and skill installations.
The source-file hashes and lockfile match the tested copy.

From the copied directory, `bun run test` ran `bun test orch watch-pr check-plan.test.ts`.
All 63 tests across five files passed, with 232 assertions and no failures.
The watcher checks cover CI fallback, review-thread pagination beyond the first page, readiness decisions, queued-stack polling, rendering and CLI exit codes.
`bun run typecheck` also passed with strict checking enabled.
No code fixes or dependency changes were needed.

Read the [complete suite output](bun-suite.txt) and [version, command and source-hash record](bun-verification.json).
To repeat the checks from a clean dependency copy, run from the repository root:

```bash
run_dir=$(mktemp -d /tmp/son-skills-bun-XXXXXX)
cp -R skills/son-mode/scripts/. "$run_dir/"
cd "$run_dir"
bun install --frozen-lockfile
bun run test
bun run typecheck
```

Remove that temporary directory after preserving any output you need.
These are offline tests with local Git fixtures and fakes for external services.
They do not prove a real GitHub PR is ready to merge.

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
The Cursor bundle was built but not installed.

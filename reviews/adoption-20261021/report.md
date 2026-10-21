# Adoption report

## Decision

Adopt Pstack commit `190d28736eff128ec94f502a22c7fe0c4b56cd37`, reviewed against accepted commit `1dcc2bacde73ddd284803b7af28164d0436198fc`.
The candidate manifest and the materialized `upstream/pstack/` tree both contain 172 files.
The snapshot verification includes file bytes, executable modes, and symlink targets.

## Disposition

Two new originals are active: `in-your-own-words` and `sharpen`.
Both use the original Pstack entrypoint, remain explicit-only, and receive the standard Son compatibility reference.
Two new originals are catalogued as inactive: `create-formal-verification-skill` and `maintain-formal-verification-skill`.
Formal verification remains deferred until a concrete verifier, repository contract, and reproducible validation path exist.
The formal-verification setup offer remains inactive.

The approved changed originals include `arena`, `automate-me`, `correct`, `figure-it-out`, `how`, `interrogate`, `ketchup`, `make-bot-ui`, `no-comments`, the approved premise, root-cause, idempotency, and behavior-testing principles, `recall`, `reflect`, `show-me-your-work`, `swarm`, and `typescript-best-practices`.
`principle-type-system-discipline` and `principle-migrate-callers-then-delete-legacy-apis` retain their current full content as intentional local edits.
`unslop` retains its personal body unchanged.
`why` retains its personal body and all retained references unchanged.
The clean imported baseline hashes for these retained files are recorded in `stack.json` before restoration.

The Son helper port adopts the reviewed owner-approval `ACTION_REQUIRED` gate classification on both watcher paths.
It adopts forge-based `gh` and Origin orchestration without a Graphite dependency.
It adopts Origin-aware worktree audit mapping.
It adapts the reviewed autopilot, orchestration, shipping, and related playbook changes while preserving the Son-owned wrappers and native boundaries.
The Son-owned principle index imports only the reviewed premise, root-cause, and behavior-testing routing description updates.
The compatibility policy explicitly keeps Son's model policy, parent role assignment, native capability checks, and writing rules authoritative over imported source wording.

The editable Son resolver intentionally deviates from the imported helper for historical forge rows.
For both `gh` and Origin, it selects the sole `OPEN` row when `--state all` also returns closed or merged history, regardless of row order.
It rejects multiple open rows with stale-close guidance, accepts one historical row when no open row exists, and rejects multiple historical rows with a direct historical-chain resolution instruction.
The immutable upstream snapshot and reviewed candidate manifest remain unchanged.
Because this helper is not a leaf original, `stack.json` does not assign it an imported baseline hash; this report is the source of record for the local deviation.

RPI and HumanLayer remain pinned at `ca7c8088db69e315a8b2deea43820270457f8f3c`.
Matt remains pinned at `49dd158d1076134a641b33efb035946536778336` and its chief-of-staff change remains deferred.
No Borghei review files were changed.

## Failure modes considered before validation

The port could select a source tree that differs from the reviewed commit.
The snapshot could drift in bytes, modes, or symlink targets.
An adapter could alter a relative link or entrypoint name incorrectly.
An imported body could override Son's model, writing, authority, or capability rules.
The owner-approval state could be misclassified on one watcher read path.
Forge frontier resolution could accept malformed output, choose the wrong base chain, or require `gt`.
Origin worktree states could map to the wrong PR or cleanup bucket.
The retained personal bodies could be overwritten or their clean baselines could be replaced with personal hashes.
The new active and deferred catalog dispositions could be incomplete or create a dangling setup route.

## Evidence

`python3 scripts/stack.py validate` passed with 6 sources, 440 source files, 121 originals, 102 active creator skills, 3 controls, and 105 total skills.
`python3 scripts/stack.py catalog` regenerated the 121-entry catalog.
All three `scripts/stack.py build --harness` commands completed with 105 built skills.
`python3 -m unittest discover -s tests -v` passed 29 tests.
`/opt/homebrew/bin/bun run typecheck` passed with strict checking.
`/opt/homebrew/bin/bun run test` passed 68 tests with zero failures.
The Bun suite used temporary Git repositories and fake `gh` and `origin` executables to exercise the actual frontier CLI paths.
The watcher fixtures covered both fast-path and rollup `ACTION_REQUIRED` cases for `Code Review Gate` and ordinary checks.
An actual temporary Git worktree and fake Origin CLI passed the Origin worktree audit mapping and safe bucket path.
`bash -n skills/son-mode/scripts/worktree-audit.sh` passed.
`git diff --check` passed.

The pre-fix real store boundary reproduced the regression with a temporary Git repository and a fake external `gh` executable: a closed row before an open row raised `branch topic has multiple pull requests (#1, #2); close the stale ones first`.
The same fixture succeeded after the fix and selected the open row.
The focused orchestration test covers closed-before-open ordering, one historical fallback, multiple historical rejection, and multiple open rejection for both `gh` and Origin.

The first Bun invocation reported the expected missing local `commander` dependency.
The existing package script then populated the task-local `node_modules`, after which the full suite passed.
That untracked directory is a local validation artifact for root to retain or clean before commit.

Global installation, commit, push, and final publication checks remain outside this subtask and are owned by root.

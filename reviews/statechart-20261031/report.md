# Statechart adoption report

## Decision

Adopt the reviewed Pstack commit `4dd1d05818d19792e7cd6e818f1667f95f7e1dbe`.
The previous accepted Pstack commit was `190d28736eff128ec94f502a22c7fe0c4b56cd37`.
The materialized `upstream/pstack/pstack/` tree contains all 573 files from the accepted source commit.
The source lock records the same 573 files and preserves their reviewed bytes, modes, and symlink targets.
The other five provider pins are unchanged.

## Disposition

The active catalog adds only the explicit-only `statechart` original.
Its 407 source files are retained byte-for-byte except for the required entrypoint adapter metadata and small native Codex routing paragraph.
The adapter adds `context: fork` and `agent: son-agent` for Claude Code.
The separate `skills/son-mode/references/statechart-routing.md` contract is additive and does not replace the Son mode body or installation.
Its SHA-256 is `890509f1aa5f928dc2815876f517c49bb45d1b4a3595550e8be252a5f3030014`.
The route guards the already-inside-`son-agent` case and reports unavailable native delegation instead of silently running directly.
The skill defines no model role and no provider fallback.

Existing Son mode, setup, personal writing, model, and routing policies remain locally owned and unchanged.
The only Pstack source advancement is the immutable reviewed snapshot needed to carry the exact statechart files.

All other Pstack changes since `190d28736eff128ec94f502a22c7fe0c4b56cd37` remain deferred.
This includes Pstack mode and playbook changes, watcher and helper retirement, interrogate support-file deletion, and unrelated workflow edits.
`ketchup-video` is catalogued as inactive because this adoption does not add a native video rendering workflow.
Formal-verification skill generators and setup offers remain inactive and deferred.
No source files were discarded from the immutable accepted snapshot.

## Failure modes considered

The pilot considered snapshot drift, adapter prose changes, invocation policy drift, route redispatch, early destination writes, overwrite of existing work, non-idempotent repeats, false model passes, deadlock, unpinned tools, and confusion between model counterexamples and actual installer behavior.
The detailed list is in [`pilot/failure-modes.md`](pilot/failure-modes.md).

## Evidence

The exact cache comparison passed for all 573 Pstack files and the Pstack lock entry.
`python3 scripts/stack.py validate` passed with 6 sources, 841 source files, 123 catalogued originals, 103 active creator skills, 3 controls, and 106 total skills.
`python3 scripts/stack.py catalog` regenerated the 123-entry catalog.
`python3 scripts/stack.py build --harness cursor` passed with 106 built skills.
All three harness builds passed with 106 skills each.
The completed installed checks are recorded below.

The original statechart suite ran from a complete scratch copy of the 407-file skill with no source `node_modules` and the provisioned fast-check 4.5.3 dependency.
The completed run passed 367 tests with 0 failures, 0 cancellations, 0 skipped tests, and 0 todo tests.
Its process exit status was 0.
The run used canonical macOS `TMPDIR=/private/tmp/statechart-pilot-20261031/test-tmp`, `NODE_OPTIONS=--v8-pool-size=1`, and the pinned Java 25 and TLC 1.7.4 toolchain.
The V8 pool setting avoided a Node 24 worker-shutdown hang observed after the SIGTERM fixture and did not change source tests.
The canonical temp path also proves the upstream relative-symlink launcher fixture without changing source tests.
An earlier incomplete copy omitted `references/render.md` and was not used as final evidence.
The completed copy included that reference file.
The complete output is in [`pilot/original-suite.log`](pilot/original-suite.log).

The correct bounded installer model passed through the actual statechart CLI with Java 25 and TLC 1.7.4.
The conflict configuration checked `TypeOK`, `NoWriteBeforePreflight`, `NoPartialWritesOnConflict`, and `NoDeadlock` over 3 states and 3 steps.
The no-conflict configuration covered the ready, write, and done branch over 4 states and 4 steps with the same four rules holding.
`NoPartialWritesOnConflict` is intentionally vacuous in the no-conflict run and is exercised meaningfully by the conflict run.
The deliberate `EARLY_WRITE = TRUE` counterfactual exited 1 and reported both expected invariant violations.
The counterexample is intentionally not an installer bug claim.
Its evidence is in [`pilot/correct-report.md`](pilot/correct-report.md), [`pilot/no-conflict-report.md`](pilot/no-conflict-report.md), and [`pilot/counterfactual-report.md`](pilot/counterfactual-report.md).

The actual `scripts/stack.py install` replay passed from a scratch repository copy.
Preview left its destination absent.
Fresh apply materialized the statechart and additive route files across 106 skills.
A second apply reported 106 identical skills, no new skills, and an unchanged destination digest.
A conflicting existing statechart raised `nothing installed` and preserved the user file, sentinel, and empty sibling destination.
The replay script and machine-readable result are in [`pilot/replay_install.py`](pilot/replay_install.py) and [`pilot/replay.json`](pilot/replay.json).

`python3 -m unittest discover -s tests -v` passed all 29 Python tests.
The source and pilot contain no dependency directory or generated dependency lock changes.
The completed installed checks are recorded below.

## Canonical checkout synchronization

The dirty canonical checkout at `/Users/sonle/Documents/work/son-skills` was inspected before the limited synchronization.
Its existing statechart body differed from the reviewed source only by the existing Son compatibility line, with no other personal body changes.
The prior statechart entrypoint was backed up at `.local/statechart-20261031/main-backup/statechart-SKILL.md`.
The route file was absent, and that absence is recorded at `.local/statechart-20261031/main-backup/statechart-routing.md.absent`.
The canonical entrypoint now matches the clean adapter at SHA-256 `c2ef338f007b542959c0eaf6c5ebc5f527fab15daf3e749320e8b76e91c6c905`.
The additive route contract now matches SHA-256 `890509f1aa5f928dc2815876f517c49bb45d1b4a3595550e8be252a5f3030014`.
Only the statechart `imported_files.SKILL.md` record in the canonical `stack.json` changed, from the prior entrypoint hash and size to the clean adapter hash and size `9539`.
The canonical checkout remains uncommitted, and no other main files were changed by this synchronization.


## Installed native checks

Both Codex and Claude Code already contained an unrouted statechart installation when the write preflight ran.
Each complete directory was backed up under `.local/statechart-20261031/installed-backups/`.
Only the two statechart entrypoints were replaced, and one new routing reference was added to each Son mode installation.
All 406 original supporting files match the reviewed build.
Existing compatibility copies, runtime metadata, and richer discovery metadata remain unchanged.
All 2,161 other recorded installed files and 18 protected global files match their baseline hashes.
The canonical model policy, writing rules, application configuration, and native agent definitions remain unchanged.

Fresh native Codex invoked `son-agent` with `gpt-5.6-luna` at `max` and passed both correct configurations, the deliberate counterfactual, and a fresh real installer replay.
The delegation tool exposed no service-tier selector.
Fresh Claude Code emitted a `task_started` event for `subagent_type: son-agent` at fork depth one, inherited Fable 5.1 at `high`, and passed all three model configurations.
Its first task allowlist blocked combined scratch preparation, so root prepared the inputs and retried only the three exact helper commands.
No global permission setting changed.

TLC's local RMI listener required the normal Codex approval flow even with cached dependencies.
The new routing reference records that observed requirement and distinguishes execution exit 2 from a model violation.
No original helper code changed to bypass a sandbox.

Java Temurin 25.0.5, the checksum-pinned TLA tools 1.7.4 jar, Pele 1.9.0, and test dependency fast-check 4.5.3 are installed outside the repositories.
Three standalone SVGs were rendered with Pele.
The counterfactual SVG was inspected in the browser, and a background rectangle in the generated SVG fixed title contrast under dark mode.
The temporary localhost preview server and browser tab were closed.

Native model reports, TLC logs, inputs, and replay evidence are under [`native/`](native/).
The primary readable charts are [`pilot/correct-chart.svg`](pilot/correct-chart.svg), [`pilot/no-conflict-chart.svg`](pilot/no-conflict-chart.svg), and [`pilot/counterfactual-chart.svg`](pilot/counterfactual-chart.svg).
The Codex native run pinned its inputs while the primary view labels were being refined.
That changes label punctuation, not the checked model or its state counts.
Machine-readable results are in [`verification.json`](verification.json).
Raw application transcripts and complete preservation baselines remain local and are not published.

Publication uses the isolated `codex/statechart-20261031` branch based on GitHub's published `10008d4`.
The original checkout's pending October 29 adoption and unpublished commit are left intact.
Its task-scoped source synchronization is recorded above, so a later canonical rebuild retains the new route.


## Reproduce the model checks

From this checkout, copy the model inputs into a new scratch directory and call the installed helper.
Use the Claude Code skill directory instead of the Codex directory when checking that installation.
The counterfactual command intentionally exits 1.

```sh
statechart_pilot_dir=$(mktemp -d)
cp reviews/statechart-20261031/pilot/Installer.tla reviews/statechart-20261031/pilot/*.cfg reviews/statechart-20261031/pilot/view.mjs "$statechart_pilot_dir/"
"$HOME/.codex/skills/statechart/scripts/statechart" "$statechart_pilot_dir/Installer.tla" --config "$statechart_pilot_dir/Installer.cfg" --view "$statechart_pilot_dir/view.mjs" --out "$statechart_pilot_dir/conflict"
"$HOME/.codex/skills/statechart/scripts/statechart" "$statechart_pilot_dir/Installer.tla" --config "$statechart_pilot_dir/InstallerNoConflict.cfg" --view "$statechart_pilot_dir/view.mjs" --out "$statechart_pilot_dir/no-conflict"
"$HOME/.codex/skills/statechart/scripts/statechart" "$statechart_pilot_dir/Installer.tla" --config "$statechart_pilot_dir/InstallerEarlyWrite.cfg" --view "$statechart_pilot_dir/view.mjs" --out "$statechart_pilot_dir/counterfactual"
```

The Python replay expects a scratch checkout named `repo` beside the copied `replay_install.py` file.
Copy the replay script into a new scratch parent and copy the source checkout into its `repo` subdirectory while excluding `.git`, `.build`, `.cache`, and `.local`.
Run `python3 -I replay_install.py` from that scratch parent.
It calls the real installer and preserves a repeatable machine-readable result.

## Independent review

Astra at `high` reviewed committed adoption `790a080` against published base `10008d4` and reported no actionable findings.
The review independently checked all source records, the minimal adapter and import hashes, unchanged prior skills and provider objects, installed routing, and model/replay claim consistency.
It inspected recorded test evidence without repeating the full suites or native pilots.
Exact Codex child spawn arguments and broader preservation checks remain root-verified evidence rather than independently exported tool events.
The detailed review remains local at `.local/statechart-20261031/independent-review.md`.

The whitespace check passes for code and authored prose.
Nine raw generated TLC logs retain their terminal blank line and are excluded from that whitespace check.
Their generated bytes were not edited to remove those warnings.

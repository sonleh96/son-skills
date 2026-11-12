# Adoption report

## Decision

Adopt Emil commit `715c1807e08c497cfd1dc4feb450a2a3300ef2a9` and Matt commit `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`.
The work starts from published base `2eb7464cdb4deed7fdcbc802b1879d915329ae69`.
The provider snapshots and source locks preserve the exact reviewed files, modes, and symlink targets.

## Accepted scope

The existing adapted copies updated are `animate`, `animation-performance`, `emil-design-eng`, `improve-animations`, `review-animations`, `code-review`, `codebase-design`, `grilling`, `implement-spec`, `improve-codebase-architecture`, `research`, and `wayfinder`.
The new active originals are `choreograph` and `gestures`.
The port kept the existing compatibility symlinks, application metadata, licenses, and supporting files.
The new motion skills add native Son routing without changing their creator workflows.
`choreograph` retains its original greeting-only response, while `gestures` retains its original invocation behavior.

The shared compatibility policy describes fresh-context delegation.
It carries the full brief into a fresh native context, uses Codex's `fork_turns="none"` when available, and does not suppress authorized stage-specific agents.
The motion playbook links the two new skills.

## Deferred scope

`remove-animations` and `software-factory` are present only in their provider snapshots and inactive dispositions.
`chief-of-staff` remains deferred.
The reviewed Matt setup and tracker changes remain in upstream source data but do not refresh the active setup copy.
RPI, unrelated provider changes, pending canonical Pstack or statechart work, canonical personal edits, and canonical provider-pin changes remain outside this isolated adoption.

## Failure modes considered

The port could use a different commit than the approved review.
The snapshot could drift in bytes, modes, or symlink targets.
Relative links or creator names could be adapted incorrectly.
The new route could redispatch the same skill from inside `son-agent` while accidentally suppressing authorized stage-specific agents.
Fresh-context wording could suppress Matt's authorized stage-specific agents.
The new skills could lose their supporting files or their original invocation behavior.
Deferred skills could become active through the registry or generated bundles.
The provider snapshot update could overwrite the published baseline's local adapters.
The catalog or build outputs could diverge from the registry.
The motion pilot could claim device behavior from desktop pointer events.
Narrow geometry could let keyboard or release targets move the tile outside the clipped stage.
Runtime-only telemetry could be invisible to a browser surface limited to DOM inspection.

## Evidence

The cached reviewed commit manifests matched every file hash, mode, and size before the snapshots were accepted.
`python3 scripts/stack.py validate` passed with 6 sources, 840 source files, 127 originals, 105 active creator skills, 3 controls, and 108 total skills.
`python3 scripts/stack.py catalog` generated 127 catalog rows.
`python3 -m unittest discover -s tests -v` passed 29 tests.
`python3 scripts/stack.py build --harness codex` built 108 skills.
`python3 scripts/stack.py build --harness claude` built 108 skills.
`python3 scripts/stack.py build --harness cursor` built 108 skills.
`node --check reviews/adoption-20261112/pilot/pilot.js` passed.
Static fixture string and structure assertions passed for rapid view changes, direct pointer tracking, rendered-position catch, reduced release behavior, reduced-motion media queries, geometry clamping, DOM telemetry, and no dependencies.
These static checks do not prove actual rapid input, drag interruption, or system media behavior.
The root-coordinated Codex in-app browser evidence is preserved in `browser-observations.json`.
At 375 by 812, six ArrowRight presses kept the card inside the stage after the geometry fix.
Five view inputs spanning 66 ms left exactly one active and aria-visible view.
Release and immediate re-grab recorded one catch 17 ms after release against a declared 220 ms settle.
The fixture reduced-motion toggle settled at x=0 with an idle phase and kept one active view after Next and Back.
The browser console had no warnings or errors.
System media was not emulated, and this run does not prove touch latency, frame timing, refresh-rate behavior, or real-device scrolling.
The twelve selected creator entrypoints match the deterministic `scripts/port.py` output for their reviewed commits.
The selected twelve existing copies and the two new copies match their recorded `imported_files` hashes.
All three bundles contain the same 108 skill names, the motion routing reference, and choreograph recipes.

## Limits

The selected files are installed in Codex and Claude Code.
Both native Codex design pilots completed through fresh Son agents.
The Claude native pilot is blocked by an expired existing login.
The motion fixture is a desktop pointer check and does not prove touch latency, device hit-target feel, refresh-rate behavior, or platform scrolling.

## Installation and preservation

The targeted installation changed 266 files across Codex and Claude Code.
All 16 protected policy, writing, and native-agent files remained unchanged.
The installer also verified that 2,972 unrelated installed files remained unchanged.
Existing per-application metadata and runtime references were preserved.
The new runtime files point to the canonical checkout.

The canonical checkout validates with 109 skills because its separate pending remove-animations adoption remains intact.
The isolated publication contains 108 skills and leaves remove-animations inactive.
The canonical source merge preserved all four unrelated provider objects and had no unexpected changes among the recorded existing source paths.
All 29 Python tests passed in the merged checkout, and all three canonical builds produced 109 skills.
See the [test log](checks/canonical-python-tests.log), [installation manifest](installation-result.json), and [preservation evidence](preservation-result.json).

## Browser observations

The Codex in-app browser exercised the dependency-free fixture after the Chrome connector failed to connect.
Five view inputs arrived within 66 ms against a 240 ms transition and left exactly one active and accessible view.
A native pointer release followed by a re-grab recorded a catch after 17 ms, during the 220 ms settle.
Reduced-motion toggle interaction settled the tile at center and retained one active view.
A reproduced narrow-screen clipping defect was fixed and retested at 375 by 812.
Six right-arrow presses then kept the tile inside the stage.
The browser reported no console warnings or errors.
The temporary tab was closed, the viewport override was reset, and the local server stopped.
See [browser observations](browser-observations.json) for actions, times, and before/after geometry.
These checks do not prove touch latency, frame rate, a physical device result, or system reduced-motion handling.

## Claude execution limit

Claude recognized choreograph and started its native son-agent fork at depth 1.
The task then failed because the existing login had expired and could not renew.
The wrapper returned exit 0 and a success-shaped result despite the failed task.
This is a blocked execution check, not a successful pilot.
Son was asked to refresh the login through claude auth login.
No credential or model settings changed.

## Native Codex results

Both explicit invocations completed a read-only task through one fresh native son-agent, with no nested agents reported.
The requested planning model was gpt-6-astra at xhigh.
The exported CLI events do not expose the full spawn arguments or actual child-model identity, and the delegation tool has no service-tier selector.
Choreograph returned a timeline, stationary elements, and concrete interruption checks.
It correctly rejected a mandatory transform-string rewrite for the supplied Motion 14.2 HTML shorthand example.
Gestures distinguished direct tracking and positional catch behavior from a production velocity-seeded spring.
See the [choreograph result](native/codex-choreograph.md), [gestures result](native/codex-gestures.md), and [structured summary](native/codex-summary.json).

These pilots verify invocation, routing, and useful task analysis.
They do not certify the fixture as a production gesture component.
The audits identified direction and stale-view risks, fixed-duration settling, velocity and cancellation gaps, and accessibility limitations in the fixture.
Those findings are preserved as audit output rather than expanded into an unrelated component framework.
The earlier browser pass establishes only the bounded cases recorded in its evidence.
Codex also reported skill-context-budget warnings while loading the large installed catalog.
Explicit invocations still loaded the selected skills and completed their native routes.
No global plugin or model setting was changed to suppress those warnings.
The [Claude summary](native/claude-summary.json) preserves its failed execution separately from successful loader discovery.

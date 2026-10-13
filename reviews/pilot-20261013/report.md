# Native skill pilot

Codex and Claude Code loaded the updated skills and completed read-only audits of the existing EPLAY importer.
Both resumed their own chats for `ketchup`.
The pilot exposed routing and catch-up errors, which were corrected and rerun.
The full [evidence record](evidence.json) contains native session IDs, source hashes, discovery results, installation checks, and preserved-policy checks.
Raw session logs remain local under the ignored `.local/pilot-20261013/` directory.

## What ran

| Task | Codex | Claude Code |
| --- | --- | --- |
| Animation performance audit | Automatic selection and direct `$animation-performance`, Astra at high effort, Standard tier | `/animation-performance`, Fable 5.1 at high effort |
| Son mode performance routing | `$son-mode` at configured Sol high on the first resume, then Astra high in a fresh session after the routing fix | `/son-mode`, then fresh sessions after the routing fix |
| Catch up after the audit | `$ketchup` in the same native session, configured Sol at high effort | `/ketchup` in the same native session |
| Portable instruction installer | Luna at max effort, Fast tier, scoped file ownership; one test correction resumed on configured Sol high | Installer output checked through filesystem tests, not a Claude implementation run |

The audit inspected `importer/index.html` and `importer/importer.js` in EPLAY.
It found a persistent picker highlight that transitions width while the screen rebuilds.
It also found that progress updates replace their element, so the declared width transition does not establish an active animation path.
These are code-grounded findings.
They do not establish dropped frames or a measured slowdown.
The prompts excluded app launches, recordings, fixes, and delegation inside the audit sessions.

## Failures and corrections

| Observed failure | Correction | Repeat evidence |
| --- | --- | --- |
| Codex chose general perf-issue while Claude chose motion-design | Son's playbook index explicitly routes web frame-cost diagnosis to motion-design and animation-performance | [Codex routing](codex-route-after.md), [Claude routing](claude-route-final.md) |
| Claude promoted an optional future recording to a pending user approval | Shared ketchup guidance distinguishes a completed diagnosis-only task from a request to expand scope | [Failing catch-up](claude-ketchup-after.md), [corrected catch-up](claude-ketchup-final.md) |
| Codex treated reloaded instructions as the latest human message and skipped the audit | Shared ketchup guidance excludes harness-injected instruction blocks and uses the preceding human task | [Failing catch-up](codex-ketchup-final.md), [corrected instruction-reload case](codex-ketchup-boundary.md) |
| Animation claims inferred a visible stall from source alone | Shared performance guidance requires an actual update path and labels unrecorded effects as hypotheses | Both audits distinguish code risks from observed frames |
| Codex CLI resume reset prior model overrides | Pass model and effort explicitly on each resumed pilot and verify the session metadata | Actual models are recorded per turn in evidence.json |
| New aliases bypassed a symlinked canonical AGENTS.md and became stale after retargeting | Point aliases at the canonical entry, preserving its final symlink | [Reproduction](canonical-retarget-reproduction.json), [fixed behavior](canonical-retarget-verified.json), and the new filesystem regression |
| Installer test depended on this Mac's live global file | Removed the host-dependent test and retained portable filesystem checks | [26 passing tests](tests.txt) |

Creator skill bodies remain unchanged.
The edits belong to Son's compatibility rules, Son controls, and routing.
The model policy, shared global rules, personal writing skills, accepted sources, and deferred RPI decision remain intact.
Skill previews match 99 built copies in each application, with personal unslop retained.
Codex native discovery reports 100 enabled expected skills and no discovery errors.
The final resumed implementation verification explicitly used Luna at max effort and passed 25 tests without changing source before independent review.
The later canonical-link regression brings the final suite to 26 passing tests.

## Portable global instructions

[instructions/AGENTS.md](../../instructions/AGENTS.md) preserves the complete current global guidance.
The only substitution replaces the home prefix with `${SON_HOME}`.
[instructions/CLAUDE.md](../../instructions/CLAUDE.md) is a relative alias to that same source.
The repository's own AGENTS.md stays separate.

The installer preflights all three global targets, refuses conflicts, and leaves matching files unchanged.
The real-home preview reports no writes.
Temporary-home tests verify rendering, aliases, repeated installation, late conflicts, wrong and dangling links, canonical cycles, and invalid home paths.
See the [machine setup guide](../../docs/instructions.md) for preview and apply commands and required local companions.

## Limits

No Chrome Performance trace or real-device recording was collected.
The native Chrome DevTools connector could not reach port 9222.
Visual equivalence, actual frame costs, and any performance improvement remain unverified.
This task did not edit EPLAY.
The importer JavaScript changed outside the pilot after its reference hash was captured.
The evidence records both hashes; findings describe the observed source rather than a frozen or current product revision.
Existing Codex and Google Drive MCP startup errors did not prevent these file-based tasks and remain outside this change.

Cursor's bundle builds, but Cursor discovery was not piloted.
Windows symlink permissions and native Windows discovery remain untested.
The pilot covers two real tasks and does not establish stack-wide quality or a time saving against a baseline.
The prior 63-test Bun watcher verification remains in the [adoption report](../adopted-20261013/report.md); watcher code did not change in this pilot.

The [independent review](independent-review-before.md) found one P2 canonical-link bug.
It was reproduced, fixed, and covered by a passing regression.
Review of the committed correction is pending.

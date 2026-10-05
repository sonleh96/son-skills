# Pilot against Son's actual work

The earlier audit in this conversation found no recorded Matt skill loads in the last 25 distinct Codex and Claude sessions it examined.
A separate Cursor sample found four loads in one older transcription session, covering grilling, domain modeling, a documented interview, and bug diagnosis.
Those observations do not establish a complete cross-application usage rate.
They suggest that clearer task-based entry points matter more than adding more installed names.

The underlying local audit is at `/Users/sonle/Documents/work/skill-audit-2026-10-05/`.
Private transcripts are not copied into this repository.
The new repository does not rerun or expand that historical session scan.

## Start with these workflows

| Work Son already does | First workflow to try | Expected improvement to test |
| --- | --- | --- |
| Banking discovery and IT questionnaires | `grilling`, `domain-modeling`, and `to-questionnaire` | Questions tied to decisions, evidence, units, and actual recipient knowledge |
| Repository handovers and explanations | `how`, `show-me`, and `handoff` | Shorter explanations with verified state and useful continuation pointers |
| Release and PR reviews | `code-review`, `blast-radius`, and `pr` | Clearer behavior, downstream risk, and proof without long status prose |
| Product UI and prototype work | `emil-prototype`, `emil-design-eng`, and `break-ui` | Distinct design options and failures exposed by realistic content |
| Slow or repeatedly corrected engineering sessions | `diagnosing-bugs`, then `retro` | Faster reproduction and fewer repeated instruction fixes |

Use son-mode to choose and execute one primary playbook for substantial tasks.
The listed skill sequences are recommendations.
Manual skills run only when requested.
Use `to-spec`, `to-tickets`, and `implement-spec` when a real task needs a spec or dependency graph, rather than turning every edit into a large workflow.
Keep specialist Swift, native motion, and loop automation available for matching work.

## Measure a useful result

Try 12 to 20 representative tasks across repositories.
Record the task, skill and source revision, application and model, setup time, active human time, elapsed time, corrections, accepted quality, and evidence path.
Compare with a similar task completed under the existing setup.
Keep skills that reduce correction or verification effort without weakening the result.
Revise or remove ones that add ceremonies or ambiguous routing.

## Initial scenario review

These are reasoning checks of the authored instructions, not live agent evaluations.

| Prompt | Intended route | Boundary checked |
| --- | --- | --- |
| Review this PR without changing code | `code-review` | Findings and evidence only |
| Turn our settled discussion into tickets | `to-tickets` | Synthesis without another interview; local output if tracker unknown |
| Animate this dropdown | `animate` | Purpose, frequency, tokens, reduced motion, and rendered check |
| Audit all animation and propose improvements | `improve-animations` | Source remains unchanged |
| Try the worst realistic data in this component | `break-ui` | Valid contracts, dev-only fixtures, report before fixing |
| Create a PR description | `pr` | No implied push or PR publication |
| Reflect on why this session went badly | `retro` | Proposed improvements, no automatic global rule or memory edits |
| Continue the Claude task in this checkout | `handoff` | Matching handoff and current-state verification before changes |
| Watch the original skills for updates | `update-son-skills` | Supported scheduler, read-only diff, failures reported |

The local tooling tests establish repository behavior.
They do not prove reliable skill selection, better UI judgment, or improved task outcomes.

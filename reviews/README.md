# Check the evidence

Start with the record that answers your question.
These files describe checks already run; they do not rerun them when you open the README.

| You want to know | Read |
| --- | --- |
| What passed in the current design? | [Redesign validation](redesign-validation.md) |
| How do our skills differ from the creators' versions? | [Saved comparison](originals-verified/report.md), with links to all three patches for each skill |
| Did the import change anything beyond the intended adaptations? | [Adaptation audit](redesign-adaptation-audit.json), covering 211 files across 95 skills |
| Which failure cases did the tooling tests exercise? | [Failure modes](../docs/test-plan.md) and [the 14-test run](redesign-tooling-tests.txt) |
| Did the built Codex skills pass format validation? | [Results for all 98 skills](redesign-skill-validation.json) |
| What does the scheduled review do? | [Saved automation configuration](automation.json) |

## Get a fresh comparison

The saved comparison records the upstream commits observed on October 5, 2026.
For current changes, run this from the repository root:

```bash
python3 scripts/upstream.py check
```

Open the `report.md` in the output directory printed by the command.
For each skill, `upstream.patch` shows the creator's changes, `local.patch` shows our adaptations and edits, and `ours-vs-latest.patch` compares our current copy directly with the latest original.
The JSON separates expected adaptations from later edits and identifies files changed on both sides.

A file changed on both sides needs review; it may still merge cleanly.
The check never applies the patches or moves the accepted source versions.
Use the [update review guide](../docs/update-review.md) when deciding what to adopt.

## What these checks establish

The records cover source integrity, file adaptation, build formats, temporary installations, and diff behavior.
They also record a successful fetch from all four creators.
Fresh-session discovery, actual model routing, and task quality across Codex, Claude Code, and Cursor still need a [real-task pilot](../docs/pilot.md).

## Earlier design

The `initial-validation`, `initial-upstream`, `skill-validation`, `tooling-tests`, and `link-validation` files describe the former 18-workflow design at commit `52020e7`.
Keep them as history.
Use the redesign records above to assess the current stack of 95 creator skills and three Son commands.

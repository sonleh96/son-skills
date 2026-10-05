---
name: son-review
description: "Review a diff against the requested behavior and repository standards, then inspect downstream effects. Use for code review, PR review, or questions about what a change could break."
---

Read `references/working-agreements.md` before following this workflow.
Consult `references/sources.md` only when detailed creator examples or specialist guidance are needed.

# Review intent, code, and consequences

1. Establish the exact base and head or working-tree diff.
   Read the request, acceptance criteria, full diff, and relevant surrounding code.
2. Review spec compliance separately from repository standards.
   For each finding, state the trigger, wrong behavior, consequence, and evidence at a real file and line.
   Omit preferences that are neither a defect nor a repository requirement.
3. Follow changed contracts beyond direct callers.
   Inspect serialization, migrations, runtime order, cleanup, flags, external library versions, and consumers in other languages when relevant.
4. Identify the one or two facts on which the change's safety depends.
   Prove them with a real-code check or running application when practical.
   Say whether each fact is asserted, source-backed, executed, or observed in the app.
   Do not present a search with no matches as proof that no consumer exists.
5. Use independent reviewers only when authorized and available.
   Give them the same intent and concrete review scope.
   Recheck their findings yourself and distinguish confirmed defects from disagreement.
   Otherwise perform the two passes sequentially and label the result self-review.
6. Return prioritized actionable findings, cleared concerns, and validation limits.

A review request does not authorize implementation or automatic commits.
Do not run a multi-model panel, rewrite source, or open a model-configuration PR as a side effect.

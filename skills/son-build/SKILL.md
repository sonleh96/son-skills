---
name: son-build
description: "Implement an authorized feature or ticket graph in small verified slices. Use for implementation from a settled spec, including dependency ordering and evidence-based completion."
disable-model-invocation: true
---

Read `references/working-agreements.md` before following this workflow.
Consult `references/sources.md` only when detailed creator examples or specialist guidance are needed.

# Build a verified slice

1. Read the accepted task, relevant source, tests, types, and comparable code.
   Inspect the branch and local changes before editing.
   Identify the next unblocked ticket and its acceptance criteria.
2. List the ways the behavior can fail before adding tests.
   Prefer an end-to-end check for visible behavior.
   For pure logic with branches, use focused unit checks with literal expected results.
   Never mock our own modules to avoid exercising them.
3. When test-first work is appropriate, run one meaningful failing check, implement the smallest slice, and run it again.
   Do not write the whole test suite ahead of the behavior.
   If a regression test is impractical, preserve a repeatable real-code reproduction and name the coverage gap.
4. Keep each slice working before starting its dependent tickets.
   Make retryable operations converge after partial failure.
   Avoid shared mutable files between workers.
5. Use one writer by default.
   If delegation is separately authorized, give each writer a disjoint scope and isolated checkout, verify its base, and integrate completed slices in dependency order.
   Never reset a dirty checkout to match a branch.
6. Run the repository's relevant validation and inspect the final diff against the acceptance criteria.
   Review standards and spec compliance as separate passes.
   A self-review is not an independent review.
7. Report delivered behavior, evidence, unresolved items, and branch state.

Close tickets, open or update a PR, mark it ready, merge, or deploy only when the task's authority includes that action.
Clean up only worktrees and resources created for this task after their work is safely retained.

---
name: son-pr
description: "Write a concise PR description with the reason, change shape, proof, and rollout risk. Use when drafting or updating a PR body; publishing requires the task to authorize it."
---

Read `references/working-agreements.md` before following this workflow.
Consult `references/sources.md` only when detailed creator examples or specialist guidance are needed.

# Write a reviewable PR

Read the final diff, original request, repository PR template, and actual validation evidence.
Describe the final implementation rather than the conversation that produced it.

1. Lead with the concrete problem and resulting behavior.
   For a small change, one or two sentences and a validation note are enough.
2. Add the smallest structural view that helps a reviewer understand a substantial change.
   Use pseudocode for logic, a diff sketch for before and after, a shallow tree for responsibilities, or Mermaid for interactions.
   Omit a visual if prose already explains the change.
3. Include evidence of before and after when available.
   Link actual screenshots, commands, test results, and artifacts.
   Distinguish local verification from CI and independent review.
4. Name material migration, compatibility, rollout, and rollback risks.
   Explain effects beyond the diff when relevant.
   If added test lines exceed implementation lines, explain why.
5. Save the description locally.
   When creation or update is authorized, use structured fields or a body file to preserve exact text, then verify the resulting PR.

Follow the repository template before any source template.
Do not force empty sections, a diagram, or a fixed bullet count onto a trivial PR.
Drafting a body does not authorize a commit, push, PR creation, merge, or notification.
In Codex, attach a created or actively reviewed PR using its native artifact tool when available.

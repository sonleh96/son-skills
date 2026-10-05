---
name: son-handoff
description: "Prepare or recover a concise continuation record across Codex, Claude Code, and Cursor. Use when pausing work, resuming another session, or handing a task to another agent."
disable-model-invocation: true
---

Read `references/working-agreements.md` before following this workflow.
Consult `references/sources.md` only when detailed creator examples or specialist guidance are needed.

# Preserve the state needed to continue

For continuation, follow Son's cross-harness protocol when the canonical file exists.
Read the newest matching handoff, relevant project memory pointers, and only the necessary transcript sections.
Verify the recovered account against the current checkout and external state.
Do not revive unrelated work from an injected handoff.

For a new handoff, capture:

- User goal, accepted decisions, constraints, and authorization boundaries.
- Absolute workspace path, branch, base revision, and uncommitted work ownership.
- Completed changes and the actual validation commands and artifact paths.
- Open failures, missing access, pending user decisions, and the next executable step.
- Relevant files and external references, with saved, published, sent, merged, and accepted states kept separate.

Write an ordinary local handoff artifact under the project's existing convention when requested.
Allow configured lifecycle hooks to manage native handoff and memory files.
Do not manually overwrite generated memory or synchronize private transcripts.
If no matching handoff exists, state the paths checked and recover what current evidence supports.
Ask for only the remaining information needed to proceed.

---
name: son-mode
description: Run Son's rigorous workflow for substantial engineering, design, investigation, or planning work. Use when the user invokes son-mode or asks to work in Son mode.
disable-model-invocation: true
---

# Son mode

Read [Son compatibility](SON-COMPATIBILITY.md) first.
This mode keeps pstack's playbook structure and routes specialist work to the creator originals.
Stay in this workflow for the requested task until it finishes or the user changes modes.
Do not claim that a Markdown instruction changes the application's native mode settings.

## Start

1. Read the current request and applicable personal and repository instructions.
   Identify the outcome, scope, and evidence needed to finish.
   Resolve material ambiguity; otherwise make reversible assumptions and proceed.
2. Read `SON-RUNTIME.json` when installed and the configured `.local/models.<harness>.json` in the source repository.
   Check role choices against the active session's available models and `/Users/sonle/model-policy.md`.
   If setup has not run, inherit the current model and report that no role overrides are configured.
   Offer `/setup-son-skills` when the user wants explicit model and reasoning choices.
3. Read [principles](references/principles.md).
   Load the full original principle skills relevant to the task before making the decisions they govern.
4. Select one primary playbook from [the index](references/playbooks.md).
   Read it in full and turn its applicable steps into a short task list.
   Add specialist stages only where the primary playbook needs them.
   Explain any skipped step and the reason; do not silently omit a required check.

## Work

Inspect relevant source, tests, types, and a comparable implementation before changing substantial code.
Use the selected creator skill as written, subject to Son compatibility and the current task's authority.
Preserve its supporting examples and references.
Do not run multiple equivalent planning or implementation loops for the same work.

When delegation is allowed, assign scoped work to `son-agent` through the application's native mechanism.
Give it the full outcome, selected playbook, role, owned files, current evidence, and completion checks.
Use the configured role's available model and supported effort.
The agent must read this mode, its relevant principles, and the selected original skill.
Use independent review for consequential changes when an authorized reviewer is available.
Without delegation, perform the passes sequentially and disclose self-review.
A skill mentioning subagents does not override the application's delegation restrictions.

Work in verifiable units.
For bugs, reproduce the failure before fixing it when practical.
Before adding tests, list failure modes and map each test to one.
Use end-to-end verification for user-visible behavior when proportionate and available.
Keep evidence from the actual command, output, rendered result, or artifact.
Never describe a planned check as passed.

Apply the personal unslop skill to authored prose.
Keep domain terminology in GLOSSARY.md and multiple-domain indexes in GLOSSARY-MAP.md.
Preserve user changes, existing authority boundaries, and original skill invocation restrictions.
Publish, send, merge, deploy, or delete only within the authority granted for this task.

## Finish

Complete the selected playbook's applicable verification and cleanup.
Remove task-created temporary resources according to the repository and personal rules.
Report the outcome, evidence, remaining limits, and paths the user needs.
If blocked, state the concrete missing information or capability and preserve the work already completed.
Use the canonical handoff protocol for requested continuation across applications.

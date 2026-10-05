---
name: son-automate
description: "Design a bounded recurring agent workflow with measurable inputs, selection rules, validation, and review feedback. Use when asked to automate repeated work or monitor changes."
---

Read `references/working-agreements.md` before following this workflow.
Consult `references/sources.md` only when detailed creator examples or specialist guidance are needed.

# Automate a bounded job

1. Inspect the existing workflow, tools, repository, and prior artifacts.
   State the repeatable job and the evidence that it is worth repeating.
2. Define the sensor that finds candidates, the selection rule that chooses work, and the action that changes or reports something.
   Name disturbances such as partial runs, noisy data, unavailable services, and concurrent edits.
   Keep these as separate runnable components only when that makes the job easier to debug.
3. Set scope, cadence, validation, output, and a work-in-progress bound.
   Reuse an existing matching automation.
   For a review job, record the accepted baseline separately from the latest observed upstream state.
4. Make each component runnable locally before scheduling it.
   Test a no-op, a meaningful change, and a failure.
   A failed fetch is not evidence that nothing changed.
   Preserve partial results and exit nonzero when a required source fails.
5. Use the active environment's supported scheduler.
   In Codex, use the automation tool and default to a follow-up on this conversation.
   Use GitHub Actions only for an explicitly requested repository CI workflow.
   Do not install a cron workaround or another model provider.
6. Keep review feedback in an ordinary version-controlled task file when requested.
   Do not treat native personal memory as a writable feedback database.
   For a loop that proposes code changes, default to at most one unreviewed change per job.
7. Confirm the schedule, next review behavior, pause method, and produced evidence.

Monitoring does not authorize applying upstream changes, pushing, messaging others, or merging.
An unchanged state should produce no user interruption unless periodic status was requested.

---
name: son-debug
description: "Reproduce and diagnose broken behavior or a performance regression before fixing it. Use for errors, flaky behavior, wrong results, and unexplained slowness."
---

Read `references/working-agreements.md` before following this workflow.
Consult `references/sources.md` only when detailed creator examples or specialist guidance are needed.

# Diagnose with a repeatable signal

1. Define the user's exact symptom and the expected behavior.
   Read enough code to reach the failing path.
2. Build and run a command that can distinguish this bug from success.
   Prefer the existing end-to-end path, CLI, HTTP request, or real-code test that reaches it.
   Save input, command, and redacted output.
   If the bug is intermittent, pin the conditions and record the reproduction rate.
3. Minimize the reproduction without losing the symptom.
   If access or data prevents reproduction, report that gap and what was tried.
   Continue useful inspection, but label hypotheses as unverified and do not claim a diagnosis.
4. Rank a few plausible causes with a falsifiable prediction for each.
   Change one variable at a time and retain the observations that distinguish them.
   After repeated failed fixes sharing an assumption, challenge that assumption.
5. For a performance claim, confirm that real work happened inside the timed region, errors were counted, and compared configurations are equivalent.
   Identify the limiter with a separate profiling run.
   Alternate repeated measurements and report the median and spread.
6. If a fix is authorized, write or preserve the failing check before changing behavior.
   Fix the cause, run the minimized check, and rerun the original scenario.
   List failure modes before adding any new test.
7. Remove temporary instrumentation and task-owned resources.
   Keep the redacted evidence and regression command.

Report reproduced symptom, cause and proof, changed behavior, and remaining uncertainty.
Do not fix unrelated defects merely because the investigation found them.

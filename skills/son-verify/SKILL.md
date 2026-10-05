---
name: son-verify
description: "Build or maintain a repeatable way to exercise an app and preserve evidence, or verify a performance claim. Use when asked to prove behavior or make project verification repeatable."
disable-model-invocation: true
---

Read `references/working-agreements.md` before following this workflow.
Consult `references/sources.md` only when detailed creator examples or specialist guidance are needed.

# Prove the behavior

Choose whether the request is a one-time verification, a reusable project verification recipe, maintenance of that recipe, or a benchmark.

1. Inspect the actual start, build, auth, test, and cleanup commands.
   Identify an isolated instance that this task owns.
   A doctor command should check its version, readiness, auth, and port ownership.
2. List concrete failure modes and the real user actions that expose them.
   Map each check to a failure mode before writing tests.
3. Drive the actual app, CLI, or service using available native tools.
   Capture the command, environment, expected result, observed result, and durable output or screenshot.
   A successful build alone does not prove user-visible behavior.
4. For a reusable recipe, save launch, doctor, drive, evidence, and cleanup instructions plus a small feature map linked to source entry points.
   Use the active tool's repository skill convention.
   Run one mapped feature from launch through cleanup and confirm the evidence survives.
5. For maintenance, compare the feature map with source and exercise each mapped behavior.
   Change only the verification recipe when that is the requested scope.
   Report product regressions without rewriting the expected behavior to hide them.
6. For a benchmark, write the claim first, verify outputs and error counts, compare equivalent production settings, and identify the limiter.
   Alternate at least five runs per side for a decision between options and report median and range.
   Use a separate profiling run and measure the path the user waits on.
   Mark a difference smaller than noise as inconclusive.
7. Tear down only resources created by the task.
   Keep a concise decision log for long unattended work, not for every trivial action.

Report observed results separately from unrun checks, source-based conclusions, and device limitations.

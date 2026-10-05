---
name: son-motion
description: "Name, build, review, or audit animation with frequency, accessibility, interruption, and performance checks. Use for motion work; keep audits read-only unless implementation is requested."
disable-model-invocation: true
---

Read `references/working-agreements.md` before following this workflow.
Consult `references/sources.md` only when detailed creator examples or specialist guidance are needed.

# Make motion serve the interaction

Choose the requested mode before editing.
Naming an effect, finding opportunities, reviewing a diff, auditing a codebase, and implementing motion have different outputs.
Read `references/motion.md` for default values and the review checklist.

1. Read existing motion tokens, libraries, usage frequency, and supported platforms.
   Name the purpose of the motion.
   Do not animate frequent keyboard actions or data people must read steadily.
2. For naming, identify the effect and explain the property or gesture that distinguishes it.
   Do not redesign it.
3. For opportunity finding or audit, cite current code and behavior.
   Prioritize by user impact and frequency, including cases where no animation is best.
   Save exact proposed values and verification steps for each accepted finding.
   Keep product source unchanged.
4. For implementation, use the cheapest existing tool that fits.
   CSS transitions fit interruptible state changes, CSS or WAAPI fits predetermined motion, and springs fit gestures and momentum.
   Prefer transform and opacity and measure exceptions.
   Reuse tokens and preserve a sensible transform origin.
5. For React Native or Expo, keep gesture-driven updates on the UI thread with the project's existing animation tools.
   Verify gesture handoff, cancellation, screen lifetime, reduced motion, and device performance.
   Do not copy web CSS recipes into native code.
6. For a review, inspect the rendered interaction as well as the code.
   Check rapid reversal, repeated triggers, entry and exit, focus, reduced motion, and hover capability.
   Report a file, symptom, exact proposed correction, and evidence for each finding.

Treat creator preferences as defaults, not browser guarantees.
Compositing depends on properties, browser, library version, and runtime conditions.
Measure before claiming hardware acceleration or a performance improvement.
Mark anything judged only from source as unverified in the rendered result.

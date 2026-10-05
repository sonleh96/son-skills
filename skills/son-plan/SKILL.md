---
name: son-plan
description: "Turn an understood problem into a concise spec, module sketch, and dependency-ordered tickets. Use when asked to plan substantial work or convert a discussion into implementation work."
disable-model-invocation: true
---

Read `references/working-agreements.md` before following this workflow.
Consult `references/sources.md` only when detailed creator examples or specialist guidance are needed.

# Plan work that can be verified

Start from the conversation and repository evidence.
A request to synthesize a spec does not require another interview.
For a small change, write a short plan in the conversation instead of creating a document tree.

1. Define the user problem, desired behavior, constraints, exclusions, and observable acceptance criteria.
   Read the glossary and relevant ADRs.
2. Read existing interfaces and callers.
   Sketch caller usage before module internals.
   Prefer a small public interface that hides the hard behavior.
   For a consequential uncertain boundary, compare two structurally different sketches and state why one fits.
   Do not spawn a model contest by default.
3. Choose the highest practical test boundary and list ways the feature can fail.
   Reuse an existing end-to-end path before inventing a test framework.
4. Save a spec with problem, behavior, decisions, acceptance checks, exclusions, and unresolved questions.
   Include a code shape only when it expresses a decision more precisely than prose.
   Do not pad the spec with exhaustive repetitive user stories.
5. Split delivery into vertical slices that each leave something working and verifiable.
   Each ticket names its outcome, scope, blocking ticket IDs, evidence, and completion criteria.
   Check for cycles and missing dependencies.
6. For work larger than one session, keep a decision map with the destination, unresolved choices, dependencies, and next ready ticket.

Use the repository's existing tracker configuration when present.
If no tracker is configured, save the spec and ticket files locally under the repository's existing docs convention.
Do not invent labels or publish tickets without authority.
The result is a plan, not permission to implement it.

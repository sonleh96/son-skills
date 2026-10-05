---
name: son-explain
description: "Explain how a subsystem works, why a decision was made, or teach a concept using source-backed examples and a small visual when useful."
disable-model-invocation: true
---

Read `references/working-agreements.md` before following this workflow.
Consult `references/sources.md` only when detailed creator examples or specialist guidance are needed.

# Explain the thing the user needs

Choose the question before choosing the format.
How requires a traced path through real code.
Why requires evidence of a decision and its alternatives.
Teaching requires a worked example and a chance to check understanding.
Rephrasing requires simpler language, not more detail.

1. Locate the relevant source, test, decision, or document.
   Trace an input through the actual boundaries to its output.
   Cite only files and artifacts you have read.
2. For rationale, check commits, ADRs, issues, and other authorized sources that can establish the decision.
   Mark a plausible explanation as inference when the historical record is missing.
   Do not search unrelated private conversations by default.
3. Lead with the answer in plain language.
   Ground each new term before relying on it.
   Separate current behavior, intended behavior, and historical reasons.
4. Use the smallest helpful visual near the sentence it supports.
   Prefer a call tree, pseudocode, diff sketch, or Mermaid for compact technical explanations.
   Use a focused local HTML artifact when interaction or visual comparison materially helps.
5. For teaching, connect the concept to the user's repository, show one example, then offer a small prediction or exercise.
   Adapt to the answer before adding depth.
   For a brief answer request, skip the lesson structure.

Read-only explanation does not authorize product edits.
Do not require subagents or a particular model to answer a simple question.

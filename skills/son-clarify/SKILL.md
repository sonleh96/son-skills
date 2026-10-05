---
name: son-clarify
description: "Stress-test a plan, resolve domain terminology, or prepare questions for a stakeholder. Use when Son asks to grill an idea, define terms, or create a questionnaire."
disable-model-invocation: true
---

Read `references/working-agreements.md` before following this workflow.
Consult `references/sources.md` only when detailed creator examples or specialist guidance are needed.

# Clarify a decision

Choose the requested mode from the task.
Use an interview for an unresolved decision, a glossary pass for terminology, or a questionnaire when the answer belongs to someone outside the conversation.
Do not turn a request to summarize a settled decision into another interview.

1. Read the available evidence, relevant code, glossary, and ADRs first.
   State the decision and the specific uncertainty that affects it.
2. In an interview, ask one consequential question at a time.
   Give concrete alternatives and your recommendation with its reason.
   Prefer an observable experiment over asking the user to predict runtime behavior.
   Use counterexamples to test boundaries and follow an answer to its implications.
3. In a terminology pass, separate concepts that share an overloaded name.
   Cross-check the proposed meaning against actual behavior.
   Write a term only once its meaning is resolved.
   A glossary entry contains the canonical term, definition, example, and distinction from nearby terms.
   Use `GLOSSARY-MAP.md` only when multiple domain glossaries need an index.
4. For an external questionnaire, state the decision the answers will inform.
   Include only questions the recipient can answer, grouped by topic, with units, time period, acceptable evidence, and unknown as an allowed answer.
   Save a draft locally unless sending was requested.
5. Finish with resolved decisions, remaining questions, and the next action.
   Record an ADR only for a consequential tradeoff that is expensive to reverse and surprising without context.

Keep provisional assumptions out of the glossary.
Respect a request to stop at analysis.

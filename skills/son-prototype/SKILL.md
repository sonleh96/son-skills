---
name: son-prototype
description: "Build a disposable experiment to resolve a behavior question or compare distinct UI directions in a live picker. Use when asked to prototype, explore variants, or test a design assumption."
disable-model-invocation: true
---

Read `references/working-agreements.md` before following this workflow.
Consult `references/sources.md` only when detailed creator examples or specialist guidance are needed.

# Prototype the uncertain part

Choose one question that a runnable artifact can answer.
Distinguish a behavior experiment from a visual comparison.
Do not build a production feature under the label prototype.

1. State the hypothesis, unknown, and observation that will settle it.
   Read the relevant domain vocabulary, interfaces, tokens, and constraints.
2. For logic or state behavior, build the smallest executable slice that exposes the transitions and outputs.
   Use realistic inputs and the actual boundary when practical.
3. For visual comparison, choose two or three structurally distinct directions.
   Name each direction's layout, density, motion, or interaction difference before building.
   Use an isolated route or local artifact with a neutral keyboard-accessible picker.
   Show one full-size variant at a time in realistic context.
   A change of accent color alone is not a different design.
4. Keep production code untouched during exploration unless the user specifically authorized an in-place prototype.
   Each candidate still needs keyboard support, responsive layout, and reduced motion.
5. Run it, capture the result, and report what the experiment resolved and what remains uncertain.
   Let the user select a visual direction before promoting it.
6. Extract only the decision-bearing types or behavior into a subsequent plan.
   Integration and cleanup follow the authorized scope.

Use existing libraries and tooling.
Do not install dependencies or spawn competing agents solely because an upstream prototype workflow does so.

---
name: son-types
description: "Tighten TypeScript or React contracts against real callers, or inspect Swift value and concurrency boundaries. Use for overly broad props, invalid states, unsafe assertions, or concurrency errors."
---

Read `references/working-agreements.md` before following this workflow.
Consult `references/sources.md` only when detailed creator examples or specialist guidance are needed.

# Make the contract match real behavior

1. Read the type, runtime validation, every relevant live caller, and the public export boundary.
   Separate production usage from stories, tests, fixtures, and demos.
   For a published library, inspect documented external contracts before assuming local callers are exhaustive.
2. Find invalid states admitted by optional fields, unrelated booleans, broad unions, casts, or duplicated shapes.
   Derive types from the authoritative schema or value where possible.
   Use discriminated states when each state has distinct required data.
3. Keep optionality when a valid live or public use genuinely omits a value.
   Do not weaken the production contract to simplify a story.
   Update supporting fixtures and every affected caller together.
4. Concentrate parsing at external boundaries.
   Let internal types express validated invariants without repeated defensive checks.
   Never use a cast to hide an unhandled state.
5. For Swift, verify the compiler version, language mode, and default actor isolation first.
   Prefer value semantics and structured task lifetimes.
   Check actor reentrancy after suspension, cancellation, ownership, and exactly-once continuation completion.
   Use current official documentation for version-sensitive concurrency features.
6. Run the type checker and the behavior checks covering the changed contract.
   Verify exports and consumers, not merely the edited component.

Do not remove a public state because an internal search did not find a caller.
Report a migration that exceeds the requested scope before expanding it.

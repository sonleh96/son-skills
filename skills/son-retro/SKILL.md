---
name: son-retro
description: "Review a session for recurring mistakes and propose small changes to tools, navigation, verification, or instructions. Use for retrospectives or improving agent guidance."
disable-model-invocation: true
---

Read `references/working-agreements.md` before following this workflow.
Consult `references/sources.md` only when detailed creator examples or specialist guidance are needed.

# Improve the next session

1. Read the requested session's evidence, or use the current conversation by default.
   Limit transcript access to the authorized scope.
   Separate a repeated mistake from a one-time surprise.
2. For each candidate, name the observed mistake, its cost, and its evidence.
   Check whether the right instruction or tool already existed but was missed or broken.
3. Prefer a smaller interface, stronger type, working check, or navigation pointer over another paragraph of rules.
   Reproduce a past failure before adding a mechanical check.
4. For instruction changes, preserve commands, real constraints, and task scope.
   Use specific triggers and concrete completion criteria.
   Conditional XML may help a Claude-specific file, but do not inject it into the shared canonical instructions without a reason.
   Keep shared rules, repository guidance, model policy, and tool configuration in their existing owners.
5. Present a short ranked list of accepted candidates, rejected ideas, and deferred work.
   Include the exact target file and proposed edit for an actionable recommendation.
6. Apply only the improvements the user has authorized.
   A request to reflect alone produces recommendations.
   Do not automatically file backlog issues, modify global skills, or write native memory.

Finish with the concrete change and the failure it prevents, or state that no durable change is justified.
Do not turn every correction into a permanent rule.

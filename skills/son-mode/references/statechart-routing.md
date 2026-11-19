# Statechart routing

`statechart` is an explicit-only skill for bounded model checks and state charts.

Claude Code uses the entrypoint's `context: fork` and `agent: son-agent` metadata.

At a Codex root, dispatch a scoped native `son-agent` task with the full statechart request and current repository context.

When already running inside `son-agent`, load and execute `statechart` directly without redispatching or spawning another agent.

If native delegation is unavailable, report that the route is unavailable instead of doing statechart work directly.

Use Son's configured model and writing policies.
This skill defines no model role and no provider fallback.

Statechart checks may start a local RMI listener through TLC.
If the harness blocks that listener, rerun with its normal approval flow instead of treating the execution error as a rule failure.
An exit code 2 means the check could not execute; it does not mean a model rule failed.

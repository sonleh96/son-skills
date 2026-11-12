# Motion routing

`choreograph` and `gestures` are creator skills with native Son routing.

At a Codex root, dispatch a scoped native `son-agent` task with the full motion request, current project context, selected skill, owned paths, and completion checks.

When already inside `son-agent`, load the selected motion skill and execute it directly without redispatching or spawning another agent.

If native delegation is unavailable, report that the route is unavailable instead of doing the motion work directly.

The skills define no model role or provider fallback.
Use Son's configured model, writing policy, and capability checks.

For `gestures`, keep the creator's real-device requirement in the handoff.
A desktop pointer simulation can check event flow and interruption logic, but it does not prove touch latency, hit-target feel, or a 60/120 Hz device result.

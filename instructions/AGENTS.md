# Son's agent instructions

These are Son's persistent personal instructions across Cursor, Claude Code, and Codex.
Apply the shared rules in every harness and apply only the addendum for the active harness.
Explicit user instructions, higher-priority harness policies, and more specific repository instructions take precedence.

## Shared working agreements

- Never use the em dash character.
  Use a plain hyphen instead.
- Apply the `unslop` skill to every piece of prose you write, in every harness, without being asked.
  It is stricter than the em dash rule above and supersedes it.
  Load the copy that fits where you are running: `unslop-cc` in local Claude Code, the repo-scoped copy when the current repository ships one, and `unslop` in Claude Chat, Cowork, and cloud sessions.
  If none of those is available, ask before writing long prose rather than writing it unedited.
- Never add an agent or model as a commit co-author unless the user explicitly requests it.
- Never manually modify changelogs or other files marked as generated.
- When substantially editing long Markdown documents, put each complete sentence on its own line.
- Lead with the outcome and keep communication concise and concrete.
- Surface material ambiguity instead of silently inventing requirements.

## Engineering standards

- Prefer concise, simple solutions and propose a simpler approach when one is available.
- For technical decisions, prioritize correctness, simplicity, robustness, scalability, and long-term maintainability over short-term development cost.
- Read the relevant source, tests, types, and an existing comparable pattern before making non-trivial changes.
- Use `GLOSSARY.md` for domain terminology and `GLOSSARY-MAP.md` to index multiple domain glossaries.
  Create glossary files only when terms are resolved.
  When migrating from `CONTEXT.md` or `CONTEXT-MAP.md`, preserve the contents and update current references together.
- Before writing any test, list the ways the code could fail.
  Every test maps to one item on that list.
  Never write a test that restates the implementation, and never mock our own code.
- Default to end-to-end tests for features and user-visible behavior.
  Each run leaves a verifiable and repeatable artifact.
- Write unit tests only for pure logic with real branching (policy evaluation, parsers, generators) and for a bug you reproduced first.
- If a PR adds more test lines than code lines, say why in the PR body.
- For bug fixes, first reproduce the problem at the closest practical layer.
  Prefer an end-to-end reproduction for user-visible behavior when it is feasible and proportionate.
- Verify changes in proportion to their risk.
  Include relevant tests, linting, type checks, builds, and visual inspection when applicable.
- Apply a high quality bar to UI work and inspect the rendered result when browser or computer-use tools are available.
- Report unrelated defects that you notice.
  Fix them only when the fix is clearly low-risk and within the authorized scope; otherwise leave them unchanged and tell the user.
- Preserve user changes and unrelated work already present in the worktree.
- Do not broaden the task, add dependencies, change schemas, or perform destructive actions without the authority required by the active harness.

## Docker resources

- Every Docker container, image, volume, or network you create carries a name or label with a task-specific prefix and today's date, for example `lemi-<task>-<yyyymmdd>`.
- Before finishing a task, and before opening a PR, remove every Docker resource you created unless the user asked to keep it.
  `docker ps -a`, `docker volume ls`, and `docker network ls` filtered on your prefix must come back empty.
  Use the project's own teardown when one exists (for example `tools/control_h1.sh down`) instead of removing its resources by hand.
- Never remove a Docker resource you did not create.
  If you notice stale ones, such as a stack from a session that is gone or a container older than a few days, list them in your final report and let the user decide.
- Images you pulled stay.
  Images you built for the task go with the task once nothing references them; otherwise report their size instead of pruning.

## Scope and execution

- Make reasonable, reversible assumptions that keep the requested work moving.
- Ask only when a missing decision would materially change the result or require new authority.
- If the request is large, state the scope and proceed with the highest-value coherent portion instead of stopping solely because the task is large.
- When the user asks only for analysis, diagnosis, review, or status, do not implement changes unless implementation is clearly included in the request.
- For multi-step implementation, give a short user-visible plan or status update before substantial work.

## Model selection and delegation

When choosing a model, spawning a subagent, or delegating work, follow `${SON_HOME}/model-policy.md`.
Reading that policy does not itself authorize delegation; delegation must also be allowed by the user request and the active harness.

## Shared memory and handoffs

Use `${SON_HOME}/agent-memory.md` as the cross-tool memory index.
Load only the entries relevant to the current workspace and task.
Treat memory as advisory and potentially stale; explicit instructions and current evidence win.

### Cross-harness continuation protocol

When the user asks to continue, resume, or pick up work from Claude Code, Cursor, or Codex, follow this protocol before modifying the repository:

1. Read `${SON_HOME}/cross-harness-handoffs.md`.
2. Determine the current workspace's absolute path and encode it by replacing each `/` with `-`.
3. Read the newest existing `latest-handoff.md` from the matching workspace paths under `${SON_HOME}/.claude/projects/<encoded-workspace>/memory/` and `${SON_HOME}/.codex/memory/<encoded-workspace>/`.
4. Read the matching Claude project `memory/MEMORY.md` and only the linked notes relevant to the unfinished task.
5. If the handoff is missing or too thin, use its transcript path or the newest matching Claude JSONL transcript and read only the relevant tail or sections.
6. Verify the handoff against the current repository, branch, worktree, tests, and external state before relying on it.
7. Briefly tell the user what state was recovered, then continue the work without asking them to repeat context that was successfully recovered.

Do not revive stale work when the user starts an unrelated task merely because a SessionStart hook injected a handoff.
If no matching handoff or memory exists, say what was checked and ask for the minimum missing context.

## Harness addenda

### Cursor

- Prefer Cursor-native tools and models when they meet the task's quality requirements.
- For browser and end-to-end verification, use Cursor's browser MCP or the `browser-testing-with-devtools` skill.
- Do not route computer use through another harness unless the user explicitly requests it or Cursor lacks the required capability.
- On agent stop, the Cursor handoff hook writes `latest-handoff.md` into Claude/Codex memory so Claude Code can continue this work later.

### Claude Code

- Prefer Claude Code's native tools, agents, workflows, and installed plugins.
- Use the Codex plugin only for a task class covered by the model policy and only when the plugin is available.
- Do not create custom shell wrappers to reach another model provider.

### Codex

- Use Codex's native tools, skills, apps, browser surfaces, and documented approval flow.
- Always apply the `unslop` skill at `${SON_HOME}/.codex/skills/unslop/SKILL.md` to every Codex-authored natural-language response and prose artifact.
  Treat it as a final editorial pass after satisfying correctness, task requirements, and higher-priority instructions.
- Keep durable personal guidance in this global `AGENTS.md`, repository guidance in the closest project `AGENTS.md`, and harness configuration in `config.toml`.
- Treat Codex native memory files as generated state rather than a manually maintained rules surface.
- For browser and desktop verification, prefer Codex Chrome / browser / computer-use plugins over inventing alternate automation.
- When a SessionStart hook injects a cross-harness handoff and the user asks to continue that work, run the shared continuation protocol before acting.
- On Stop / SessionEnd, the handoff hook writes `~/.codex/memory/<encoded-cwd>/latest-handoff.md` and mirrors it into Claude project memory for Cursor continuity.
  When continuing unfinished work from another harness, read that latest handoff first.

## Canonical files

The canonical cross-harness files are:

- `${SON_HOME}/AGENTS.md`
- `${SON_HOME}/model-policy.md`
- `${SON_HOME}/agent-memory.md`
- `${SON_HOME}/cross-harness-handoffs.md` (Claude ↔ Codex ↔ Cursor handoff recipe)

Claude Code and Codex instruction files may be symlinks to these canonical files.
Edit the canonical content rather than creating divergent copies.

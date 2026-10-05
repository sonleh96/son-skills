# Install and configure Son's skills

The stack is local first and applies across repositories.
It does not choose a project tracker, branch convention, or deployment target.
No global skills were replaced during this redesign.

## Build and preview

```bash
python3 scripts/stack.py build --harness codex
python3 scripts/stack.py build --harness claude
python3 scripts/stack.py build --harness cursor
```

Builds appear under `.build/<harness>/skills/` and `.build/<harness>/agents/`.
Codex uses `agents/openai.yaml` for invocation policy and a TOML custom agent.
Claude Code and Cursor keep manual-invocation frontmatter and a Markdown custom agent.
The agent omits fixed model overrides so the parent's explicit role choice can apply.

Preview the relevant installation:

```bash
python3 scripts/stack.py install --harness codex --dest "$HOME/.codex/skills"
python3 scripts/stack.py install --harness claude --dest "$HOME/.claude/skills"
python3 scripts/stack.py install --harness cursor --dest "$HOME/.cursor/skills"
```

Use the project's corresponding directory for a repository-local installation.
The installer writes `son-agent` to the adjacent `agents/` directory and renders its skill path for that destination.
Repeat with `--apply` only when installation is intended.
It preflights every skill and agent, refuses differing existing copies, and leaves identical copies alone.
Many original names may already exist in your current setup; review those collisions before migrating them.
There is no force option.
Do not bulk-install `upstream/`, which also contains inactive skills and original control commands.

## /setup-son-skills

After installation and application refresh, invoke `/setup-son-skills`, or `$setup-son-skills` in Codex.
The command reads the active application's available models and supported efforts.
If no native model listing exists, it asks for your available choices.
It reads the canonical model policy, lets you choose a budget, then shows six role assignments for acceptance.

| Budget | Reasoning target |
| --- | --- |
| Small | Medium |
| Medium | High |
| Large | Extra high |
| Unlimited | Max |

A budget is a reasoning preset, not a dollar or token cap.
A selected model receives the highest supported effort at or below the target, unless you explicitly choose another supported effort.
`inherit-parent` preserves the parent model and effort.
Unsupported choices fail validation.

The setup saves `.local/models.<harness>.json` in this repository.
It does not change the parent model picker or rewrite `/Users/sonle/model-policy.md`.
Son mode rechecks runtime availability before delegation and uses only controls the current application exposes.
See the [configuration schema](../skills/setup-son-skills/references/configuration.md) for scripted setup.

## Project use

Invoke `/son-mode` for substantial work and choose its primary playbook by task.
Matt's `setup-matt-pocock-skills` remains available for actual tracker, label, and glossary configuration.
Use `GLOSSARY.md` and `GLOSSARY-MAP.md`; create terminology only when it has been resolved.
The three Son controls do not replace project-specific setup.

Creator instructions retain their tool and agent references.
[Son compatibility](../policies/compatibility.md) specifies how to resolve them with real available tools and current authority.
Keep this checkout at the path recorded in `SON-RUNTIME.json`; rebuild after moving it.

## Verification limits

Build and temporary-install checks verify files, schemas, references, and collision handling.
Actual skill discovery, model routing, and task quality in fresh Codex, Claude Code, and Cursor sessions require a pilot after installation.
Native custom-agent formats follow [Codex](https://developers.openai.com/codex/subagents/), [Claude Code](https://code.claude.com/docs/en/sub-agents), and [Cursor](https://cursor.com/docs/subagents) documentation checked for this redesign.

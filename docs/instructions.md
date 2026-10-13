# Portable global instructions

[instructions/AGENTS.md](../instructions/AGENTS.md) contains the full shared global instructions.
[instructions/CLAUDE.md](../instructions/CLAUDE.md) points to that same file.
The only template substitution replaces the source machine's home directory with `${SON_HOME}`.
The installer renders it as the selected machine's absolute home path.
Your model, writing, testing, and continuation rules remain intact.
The repository's own AGENTS.md stays separate.

## Install on another machine

Install the [skills](setup.md) first so the instructions can find `unslop`.
Then preview the shared instruction installation:

```bash
python3 scripts/instructions.py --home "$HOME"
```

Add `--apply` to install.
The installer writes `$HOME/AGENTS.md` and creates relative aliases at `$HOME/.codex/AGENTS.md` and `$HOME/.claude/CLAUDE.md`.
Existing matching files and aliases stay in place.
New application aliases follow the canonical AGENTS.md even if its symlink target changes later.
A differing file, directory, dangling symlink, or incorrect alias stops the preflight before any write.
There is no force option.
On this Mac, the preview reports three unchanged paths and no writes.

## Bring the required local companions

The global rules refer to `model-policy.md`, `agent-memory.md`, and `cross-harness-handoffs.md` in your home directory.
Bring your intended versions when setting up another machine.
This command does not copy those files, model catalogs, authentication, application settings, memory, or hooks.
It does not install the separate Claude Code `unslop-cc` skill.
Use an installed repo-scoped `unslop` as the shared instructions allow, or bring your personal Claude writing skill.
Missing files do not authorize guessed model assignments or fabricated memory.

Use `/setup-son-skills` in Claude Code or `$setup-son-skills` in Codex to check that machine's available models.
The installer and filesystem tests ran on macOS with temporary homes, including a Linux-style home path.
Windows symlink permissions and native Windows discovery remain untested.

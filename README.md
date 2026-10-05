# Son's skills

A personal stack of 95 minimally adapted creator skills, with three Son commands, `son-agent`, 24 original principles, and 29 playbooks.
It works across repositories without a Lemi-specific configuration.
The repository is local and has not been installed globally or published.

## Start here

| Command | Purpose |
| --- | --- |
| [/setup-son-skills](skills/setup-son-skills/SKILL.md) | Detect available models, choose a reasoning budget, and save assignments by role |
| [/son-mode](skills/son-mode/SKILL.md) | Follow a rigorous playbook with applicable principles, creator skills, verification, and scoped son-agent work |
| [/update-son-skills](skills/update-son-skills/SKILL.md) | Compare pinned originals, your editable skills, and the creators' latest versions on demand |

Use the slash command where supported, or `$setup-son-skills`, `$son-mode`, and `$update-son-skills` in Codex.
Commands become discoverable after installation and application refresh.
The equivalent update command works now from this checkout:

```bash
python3 scripts/upstream.py check
```

The check writes three patches per active creator skill.
They show upstream changes since the accepted version, local differences from that version, and your current copy versus latest upstream.
The report separates expected adapter edits from later customizations and flags files changed on both sides.
It never applies an update.

## What stays close to the creators

Skill bodies, examples, scripts, templates, and supporting files remain in their original folders under `skills/`.
The adapter adds one compatibility reference, original license notices, and invocation metadata.
Only duplicate command names and their explicit references receive prefixes.
Pstack's `teach` and `tdd` become `pstack-teach` and `pstack-tdd`.
Matt's `prototype`, `teach`, and `tdd` receive `matt-` prefixes; Emil's `prototype` becomes `emil-prototype`.

[Son compatibility](policies/compatibility.md) resolves differences in model selection, tool availability, task authority, testing, and personal instructions.
Playbooks select the relevant originals without combining their bodies.
The earlier 18 synthesized workflows are preserved in Git history at `52020e7`.

| Creator | Active originals | Original skills retained in snapshots |
| --- | --- | --- |
| [Pstack](https://github.com/cursor/plugins/tree/main/pstack) | 48 | 54 |
| [Emil Kowalski](https://github.com/emilkowalski/skills) | 14 | 14 |
| [HumanLayer](https://github.com/humanlayer/skills) | 6 | 6 |
| [Matt Pocock](https://github.com/mattpocock/skills) | 27 | 38 |

Pstack's three original control commands are replaced by Son's controls, and Benny's three automations remain inactive.
Matt's seven in-progress and four miscellaneous skills remain inactive.
All 112 originals have a disposition in the [catalog](docs/catalog.md).
The 23 pstack playbooks retain their steps with renamed references; six Son playbooks route work across creators.

## Build and verify

Requires Python 3.9 or newer and Git.
Repository tooling uses the Python standard library.
Creator support scripts retain their own dependencies; building a bundle does not install or run them.

```bash
python3 scripts/stack.py validate
python3 -m unittest discover -s tests -v
python3 scripts/stack.py build --harness codex
python3 scripts/stack.py build --harness claude
python3 scripts/stack.py build --harness cursor
```

Each build includes complete skill folders and a native `son-agent` definition.
Skills contain local compatibility and license files.
Setup and update commands use `SON-RUNTIME.json` to locate this checkout, so keep it at its recorded path or rebuild after moving it.
Model assignments stay in ignored `.local/` configuration and never rewrite the canonical model policy.

See [installation and setup](docs/setup.md), [routing decisions](docs/decisions.md), [creator analysis](docs/creator-analysis.md), and the [pilot scenarios](docs/pilot.md).

## Update on demand or every two weeks

Run `/update-son-skills` whenever you want a fresh comparison.
Use `--source matt` to inspect one creator or `--installed-skills /absolute/path/to/skills` to compare a separate installed copy as well.
Without that option, your copy means this repository's editable `skills/` directory.

The existing Codex automation checks all four creators every two weeks on Monday at 09:00 in the configured local timezone.
It reports meaningful new upstream changes and failed checks, and stays quiet on repeated pending diffs.
Both paths use the same checker and preserve your skills and accepted source pins.
See [update review and adoption](docs/update-review.md).

## Layout

```text
skills/                 95 creator skills and three Son commands
agents/                 Canonical son-agent instructions
policies/               Shared Son compatibility rules
stack.json              Exact source mappings and imported file baselines
catalog.json            Generated inventory of all 112 source skills
sources.lock.json       Accepted commits, modes, sizes, and file hashes
upstream/               Immutable creator snapshots
scripts/                Model setup, build, validation, install, and diff tooling
.local/                 Ignored local model configuration
.build/                 Ignored application-specific bundles
reviews/                Verification evidence and local update reports
```

[Third-party notices](THIRD_PARTY_NOTICES.md) preserve the original MIT attributions.
The license for Son's original tooling remains undecided while this repository is local.

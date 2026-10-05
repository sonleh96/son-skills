# Son's skills

A personal stack for work across all repositories, with 18 combined workflows drawn from 112 skills by Matt Pocock, Emil Kowalski, HumanLayer, and Lauren Tan's pstack.
The original sources are pinned and preserved for comparison.
The combined skills keep Son's working agreements and use the active tool's capabilities.

This is a local Git repository.
The stack has not been installed globally or published.

## Start here

- [Creator analysis](docs/creator-analysis.md) explains each stack's strengths and assumptions.
- [Combination decisions](docs/decisions.md) records overlaps, conflicts, and exclusions.
- [Complete catalog](docs/catalog.md) accounts for every original skill.
- [Setup](docs/setup.md) builds portable Codex, Claude Code, and Cursor copies.
- [Update review](docs/update-review.md) describes the active review every two weeks.
- [Pilot](docs/pilot.md) connects the stack to Son's observed workflow and defines what still needs real-task testing.

## Pick the task, then the skill

Use `$son-<name>` in Codex or the corresponding slash command where the active application supports it.
Manual skills require an explicit request.
Automatic skills may be selected when their descriptions match the task.
Neither mode expands the user's authorization.

| Task | Skill | Selection |
| --- | --- | --- |
| Challenge a decision, resolve terms, or prepare stakeholder questions | [son-clarify](skills/son-clarify/SKILL.md) | Manual |
| Turn an understood problem into a spec and dependency-ordered tickets | [son-plan](skills/son-plan/SKILL.md) | Manual |
| Implement authorized work in verified slices | [son-build](skills/son-build/SKILL.md) | Manual |
| Reproduce a bug and establish its cause | [son-debug](skills/son-debug/SKILL.md) | Automatic |
| Review intent, standards, and downstream effects | [son-review](skills/son-review/SKILL.md) | Automatic |
| Prove behavior or maintain a repeatable verification recipe | [son-verify](skills/son-verify/SKILL.md) | Manual |
| Write a concise, evidence-backed PR body | [son-pr](skills/son-pr/SKILL.md) | Automatic |
| Explain behavior, rationale, or a concept | [son-explain](skills/son-explain/SKILL.md) | Manual |
| Find improvements for the next session | [son-retro](skills/son-retro/SKILL.md) | Manual |
| Design a bounded recurring workflow | [son-automate](skills/son-automate/SKILL.md) | Automatic |
| Build or polish web UI and mobile interactions | [son-ui](skills/son-ui/SKILL.md) | Automatic |
| Resolve a behavior question or compare UI directions | [son-prototype](skills/son-prototype/SKILL.md) | Manual |
| Name, build, review, or audit motion | [son-motion](skills/son-motion/SKILL.md) | Manual |
| Exercise UI with realistic extreme data | [son-ui-stress](skills/son-ui-stress/SKILL.md) | Automatic |
| Tighten React and TypeScript contracts or inspect Swift boundaries | [son-types](skills/son-types/SKILL.md) | Automatic |
| Research a concrete decision against primary sources | [son-research](skills/son-research/SKILL.md) | Automatic |
| Prepare or recover a cross-tool continuation record | [son-handoff](skills/son-handoff/SKILL.md) | Manual |
| Edit agent instructions and technical documents | [son-writing](skills/son-writing/SKILL.md) | Automatic |

For a substantial feature, the usual sequence is clarify, plan, build, review, then PR.
Skip stages whose work is already settled.
A bug begins with debug.
A UI question may need a prototype before a plan.
The skills do not automatically invoke the next manual skill.

## Validate and build

Requires Python 3.9 or newer and Git.
The repository scripts use only Python's standard library.

```bash
python3 scripts/stack.py validate
python3 -m unittest discover -s tests -v
python3 scripts/stack.py build --harness codex
python3 scripts/upstream.py check
```

The build produces self-contained skills under `.build/codex/skills/`.
Each contains local working agreements, detailed source references, pinned attribution, and the relevant MIT license notices.
Creator source files are references, not additional discoverable skills.

## Sources and updates

| Source | Original skills | Pinned commit |
| --- | --- | --- |
| [pstack](https://github.com/cursor/plugins/tree/main/pstack) | 54 | `4e5b1cf2ccb0ea3716f08c8ee0a5856b5ab93536` |
| [Emil Kowalski](https://github.com/emilkowalski/skills) | 14 | `e8a175de22ae1e49370fc144c1f3bb9aeedf988d` |
| [HumanLayer](https://github.com/humanlayer/skills) | 6 | `ca7c8088db69e315a8b2deea43820270457f8f3c` |
| [Matt Pocock](https://github.com/mattpocock/skills) | 38 | `4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d` |

Captured on October 5, 2026.
The Matt snapshot includes 27 promoted skills, seven in-progress skills, and four miscellaneous skills.
The pstack count includes three Benny automation skills.
Experimental and specialist originals remain catalogued even when they are not active in the combined stack.

The Codex automation checks these sources every two weeks on Monday at 09:00 in the configured local timezone.
It reports meaningful new changes and failed checks in the originating chat.
It does not apply updates.
The first live check found no changes against the captured snapshots.

## Repository layout

```text
skills/                 Combined workflow instructions and discovery metadata
policies/               Shared working agreements and motion reference
stack.json              Ownership and source mapping for each combined skill
catalog.json            Generated inventory of every original skill
sources.lock.json       Accepted commits, modes, sizes, and file hashes
upstream/               Immutable tracked source snapshots
scripts/                Build, validation, installation, and diff tooling
tests/                  Real Git and filesystem failure-case tests
docs/                   Analysis, decisions, setup, review, and pilot guidance
reviews/                Initial verification and local update reports
```

Read [third-party notices](THIRD_PARTY_NOTICES.md) before redistribution.
Creator sources retain their MIT licenses.
The publication license for Son's original adaptations and tooling remains undecided while this repository is local.

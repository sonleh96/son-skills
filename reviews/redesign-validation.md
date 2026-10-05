# Original-skill redesign validation

Verified on October 5, 2026.
The earlier 18 synthesized skills have been replaced by 95 creator originals and three Son controls.

| Check | Result | Evidence |
| --- | --- | --- |
| Source integrity | Four unchanged snapshots, 392 files | scripts/stack.py validate and sources.lock.json |
| Minimal adaptation | 211 original files checked across 95 skills; no unexplained differences | [Adaptation audit](redesign-adaptation-audit.json) |
| Catalog | All 112 originals have a disposition | [Catalog](../catalog.json) |
| Control structure | Setup, mode, update, native son-agent, 24 principles, and 29 playbooks | README and generated builds |
| Failure cases | All 14 tests passed using real local Git repositories and filesystem operations | [Test output](redesign-tooling-tests.txt) |
| Codex skill schema | All 98 built skills passed the installed skill-creator validator | [Skill validation](redesign-skill-validation.json) |
| Native formats | Codex agent TOML and Claude Code or Cursor YAML parsed; agent paths target the installation | Format inspection and F13 |
| Live comparison | All four upstreams checked, zero new upstream changes, 95 three-way comparisons | [Report](originals-verified/report.md) |
| Biweekly automation | Existing automation updated and active with the same two-week cadence | [Persisted configuration](automation.json) |

The Codex build removes angle brackets from one original description because its validator forbids them.
The canonical original description and body remain intact.
PyYAML for the external validator came from an existing local cache; repository tooling uses the standard library.
Original punctuation and whitespace remain unchanged except the documented adapter edits.

The builds and temporary installations were verified locally.
Fresh-session discovery, runtime model routing, and task quality across the three applications remain untested until installation and a real-task pilot.
Creator support scripts were preserved and were not executed.
No remote, global installation, or Docker resource was created.

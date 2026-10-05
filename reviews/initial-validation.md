# Initial validation

Validated on October 5, 2026.

| Check | Result | Evidence |
| --- | --- | --- |
| Accepted source integrity | Four sources, 392 files, exact hashes and modes | `python3 scripts/stack.py validate` |
| Complete inventory | 112 originals, each with a disposition | [Catalog](../catalog.json) |
| Combined workflows | 18 skills with source attribution and owner | [Registry](../stack.json) |
| Git and filesystem failure cases | Nine tests passed | [Test output](tooling-tests.txt) |
| Codex skill validation | All 18 built skills passed the installed skill-creator validator | [Validator results](skill-validation.json) |
| Claude and Cursor metadata | YAML parsed; manual-only flags preserved | [Validator results](skill-validation.json) |
| Discoverable entries per build | Exactly 18, with source entry points stored as SOURCE.md references | Recursive build inspection |
| Live upstream comparison | All four sources checked; zero changed files | [Initial upstream report](initial-upstream.json) |
| Biweekly automation | Created, active, and persisted configuration read back | [Automation record](automation.json) |
| Local documentation links | 148 checked with no missing targets | [Link check](link-validation.json) |

The generic Codex validator rejected Claude's `disable-model-invocation` extension during the first pass.
The builder now emits application-specific metadata while preserving the intended manual-only behavior.
The final Codex pass succeeded for all 18 skills.
PyYAML came from an existing local cache for the external validator; the repository tooling itself has no third-party Python dependency.
The original snapshots contain existing whitespace warnings.
They remain unchanged for exact comparison; the authored-file whitespace check excludes `upstream/`.

The combined instructions received the scenario review described in [the pilot guide](../docs/pilot.md).
No independent agent evaluation or fresh application installation was performed.
Real-task quality, discovery in each application, and scheduled execution remain to be observed after this initial setup.

No Docker resources were created.
No remote repository was created and no global skill installation was changed.

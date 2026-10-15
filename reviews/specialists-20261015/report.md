# Data and ML skill installation

Verified on October 15, 2026.

The repository and both personal installations now contain three distinct specialist skills.
Direct invocations and Son mode selections route their work through native `son-agent`.

| Skill | Source | Use |
| --- | --- | --- |
| `data-scientist` | VoltAgent | Broad statistical research, exploratory analysis, and analytical recommendations |
| `predictive-modeling` | Borghei's `data-scientist`, renamed locally | Predictive tabular modeling, feature engineering, evaluation, and experiments |
| `ml-engineer` | VoltAgent | Production training pipelines, serving, monitoring, retraining, and rollback |

The VoltAgent source remains pinned to `c9e51ec0b3d43f5dcdd0b558a6cd28ba6ada97c1`.
Its existing local execution contracts remain, while the former fixed subagent-model blocks give way to Son routing and the central model policy.
Borghei is pinned to `4a698e8d07856fdca9ec3e69082a9d68c8dd45d0`.
The three Python helpers match that source exactly and retain its MIT plus Commons Clause license.
The four previously accepted providers and their snapshot manifests did not change.

## Routing and adaptations

Claude Code uses `context: fork` and `agent: son-agent` in all three entrypoints.
Codex uses the specialist dispatch instructions and its native `son-agent` definition.
An agent already executing the specialist reads its skill directly and does not dispatch another specialist agent.
An unavailable native route must be reported rather than replaced with unreported root execution.

The first Claude check exposed a short-answer request causing skipped Son startup reads.
The agent instruction now makes clear that output length does not waive those reads.
The focused rerun read Son mode, compatibility, the principles index, the relevant full principle, the routing contract, runtime configuration, and the investigation playbook before answering.

Borghei's tracker and hypothesis-testing examples placed `--json` after subcommands, which failed with exit code 2.
The editable examples now place root options before subcommands.
The scripts themselves remain unchanged.
Their approximation, local JSON tracking, and metric-direction limitations are documented in the skill.

## Verification

| Check | Result |
| --- | --- |
| Repository validation | Passed: 6 sources, 435 source files, 117 original entries, 103 active skills |
| Python repository suite | All 29 tests passed |
| Codex, Claude Code, and Cursor builds | Each built 103 skills |
| Temporary installation roundtrips | Passed, including repeat installation |
| Flat VoltAgent entrypoints | Catalogued separately, with isolated comparisons and overlap detection |
| Borghei directory selection | Future added helper files appear without including unrelated skill folders |
| Upstream comparison | No selected content changes for either new provider |
| Helper invocation checks | Experiment log and comparison, proportions example, and feature-ranking fixture passed |
| Native Codex checks | CLI answered all three scoped questions; a native Codex `son-agent` also loaded and executed all three without redispatch |
| Native Claude Code checks | All three direct Skill invocations forked and completed; the focused startup-read rerun passed |
| Installed contents | Both installations match all 102 repository-managed skills and their native agent definitions; personal `unslop` is retained |
| Existing policies | Model policy, global instructions, Codex configuration, Claude settings, and personal Codex writing skill hashes are unchanged |

The content comparison observed VoltAgent HEAD `408d3c9eee2d0c75c12a3abb5de29e53c2ca6b9e` and Borghei HEAD `4a698e8d07856fdca9ec3e69082a9d68c8dd45d0`.
The accepted VoltAgent pin stayed unchanged because the selected source files had no content changes.
The independent review found an outdated README license summary, which was corrected, and no actionable implementation defect.

## Installation and limits

The personal destinations are `~/.codex/skills` and `~/.claude/skills`, with the corresponding `son-agent` definitions under each application's `agents/` directory.
Backups and raw native-check logs are local and ignored by Git.
The original installations are backed up under `.local/install-backups/specialists-20261015T010505Z/`.
The subsequent startup correction has a second backup under `.local/install-backups/specialist-startup-20261015T010845Z/`.
Invocation evidence is under `.local/specialist-pilot-20261015/`.
The older Codex `machine-learning-engineer` and `mlops-engineer` folders were moved into a separate `retired-ml-aliases-*` backup so `ml-engineer` is the single active MLE/MLOps skill.
Neither older skill was present in the Claude Code personal skill directory.

These checks verify installation, loading, routing, and basic helper invocation.
They do not establish general statistical accuracy, predictive performance, production readiness, or improved task quality.
Cursor was built and tested in a temporary destination but was not installed globally.
The Codex CLI emitted existing MCP startup warnings for `codex` and `gdrive`, plus a hook warning about an ephemeral parent transcript.
Those warnings did not prevent the checks from completing; their configuration was left unchanged.

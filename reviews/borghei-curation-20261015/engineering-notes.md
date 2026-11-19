# Engineering, data and workflow review

No immediate imports are recommended from this slice.
Keep the existing Son controls, VoltAgent specialist roles, native analytics workflows and imported `predictive-modeling` package.
The best reuse is a short reference stage inside an existing playbook, selected only when the task needs it.

All 100 real skills in `engineering`, `data-analytics` and `workflow` were screened against the current baseline.
The sample under `engineering/skill-tester/assets/sample-skill/SKILL.md` is excluded as a fixture.
The matrix has 71 duplicates, 19 deferred specialists, five playbook inputs, four conflicts and one existing import.
No new general principle is warranted.

## Optional workflow references

| Rank | Source | Existing playbook and outcome | Incremental value |
| --- | --- | --- | --- |
| 1 | [agentic-evaluation-framework](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/agentic-evaluation-framework/SKILL.md#L62-L81) | `eval`, a credible comparison of prompt or agent variants | Human calibration, swapped answer order and critical-slice review supplement `arena` and `benchmark-checklist`. |
| 2 | [data-quality-auditor](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/data-quality-auditor/references/dq-incident-response.md#L53-L96) | `bug-fix` or `feature` for a data pipeline, verified recovery from bad data | Reuse native `analyze-data-quality`, `validate-data`, `data-engineer` and `incident-responder`; add affected-record scope, recovery choices and downstream verification. |
| 3 | [runbook-generator](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/runbook-generator/SKILL.md#L23-L28) | `feature`, `bug-fix` or `pause-safely`, an operational handoff | Reuse `handoff`, `documentation-and-adrs`, `sre-engineer` and verification skills; add per-step checks, rollback and escalation fields. |
| 4 | [skill-security-auditor](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/skill-security-auditor/SKILL.md#L23-L29) | `upstream-review`, a package trust-boundary review | Reuse `update-son-skills` and `security-engineer`; add manual inspection questions for instruction text, helpers, dependencies and filesystem boundaries. |
| 5 | [agent-harness](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/agent-harness/SKILL.md#L58-L102) | `eval` and `agent-automation`, a scenario regression report | Reuse existing trials and verification; add recorded tool-call assertions and paired scenario comparisons. |

Start with the first two only when a matching task arrives.
A future adoption can preserve an original as a skill package while a Son playbook references it.
This recommendation does not require another router, agent persona or orchestration runtime.

## Findings that block turnkey reuse

`dependency-auditor` uses a literal built-in CVE dictionary, not a current advisory service.
Its supported-file dispatch covers five ecosystem families, while the skill advertises eight.
Its version comparator returns equality when parsing fails, and license fallback matches substrings, which can collapse a compound or restricted license to a simple license.
See [CVE dictionary and parser dispatch](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/dependency-auditor/scripts/dep_scanner.py#L56-L92), [version matching](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/dependency-auditor/scripts/dep_scanner.py#L267-L304) and [license fallback](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/dependency-auditor/scripts/license_checker.py#L522-L557).
The skill acknowledges the representative CVE subset, but `skill-security-auditor` still routes to it for real-time lookup.

`runbook-generator` can turn a service name into a document that assumes Kubernetes, PostgreSQL and GitHub Actions.
It stamps `Last verified` with today's date during generation.
It also supplies `pnpm db:migrate`, error rate below 1% and p95 below 200 ms as fixed examples.
Those values and commands need service evidence before use.
See [stack defaults](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/runbook-generator/scripts/runbook_scaffolder.py#L74-L87), [verification-date stamping](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/runbook-generator/scripts/runbook_scaffolder.py#L116-L120) and [migration commands and targets](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/runbook-generator/scripts/runbook_scaffolder.py#L158-L192).
Its rollback validator checks whether a rollback heading exists, rather than whether each action has a working reversal.
See [rollback validation](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/runbook-generator/scripts/runbook_validator.py#L187-L218).

`skill-security-auditor` is useful as a manual review checklist, but its PASS verdict covers only selected patterns and files.
The code scanner collects Python files, the supply-chain collector omits `package.json`, and the prompt scanner skips fenced blocks.
These limitations conflict with the skill's broader advertised coverage.
See [Python-only collection](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/skill-security-auditor/scripts/code_scanner.py#L332-L339), [dependency file collection](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/skill-security-auditor/scripts/supply_chain_checker.py#L205-L233) and [fenced-block exclusion](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/skill-security-auditor/scripts/prompt_injection_scanner.py#L275-L279).

`a11y-audit` checks source markup and simplified CSS pairs.
Its RGBA parser drops alpha, so it can report a contrast ratio for colors that differ from the rendered colors.
It does not establish keyboard operation, accessible names after rendering or full WCAG conformance.
See [RGBA parsing](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/a11y-audit/scripts/contrast_checker.py#L75-L78) and [CSS pair extraction](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/a11y-audit/scripts/contrast_checker.py#L177-L212).
Defer this package and use existing browser inspection for current UI work.

`doc-drift-detector` has useful inputs, but its score is a heuristic.
The link checker marks unchecked external URLs valid and does not generate numeric suffixes for repeated heading anchors.
Python signature extraction also omits positional-only parameters.
See [score weights](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/doc-drift-detector/scripts/doc_staleness_scorer.py#L40-L58), [heading extraction](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/doc-drift-detector/scripts/link_checker.py#L174-L227), [unchecked URLs](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/doc-drift-detector/scripts/link_checker.py#L240-L245) and [parameter extraction](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/doc-drift-detector/scripts/api_doc_validator.py#L121-L180).
Use current repository link checks and targeted source validation until the concrete gaps are fixed and tested.

`agentic-evaluation-framework` correctly states that its scripts aggregate supplied scores and never invoke a model.
Its rubric scorer skips absent criteria instead of failing a missing mandatory criterion.
Its ranking output sorts Elo first even when the prose recommends Bradley-Terry for a fixed batch.
See [missing criterion handling](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/agentic-evaluation-framework/scripts/rubric_scorer.py#L90-L123) and [ranking order](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/agentic-evaluation-framework/scripts/pairwise_ranking.py#L154-L160).
Borrow the calibration method as a reference, not the untested gate.

`data-quality-auditor` openly limits the scripts to local inputs.
A separate row-count requirement is needed because an empty table passes its not-null check.
The freshness monitor accepts naive ISO timestamps but subtracts them from an aware UTC timestamp by default, and a future timestamp passes the max-age test.
See [empty data handling](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/data-quality-auditor/scripts/dq_check_runner.py#L238-L247), [timestamp parsing](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/data-quality-auditor/scripts/freshness_monitor.py#L48-L68) and [freshness comparison](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/data-quality-auditor/scripts/freshness_monitor.py#L95-L122).
The quarantine example also shows an insert followed by a delete without a transaction, so recovery commands need separate design and authority.
See [quarantine example](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/data-quality-auditor/references/dq-incident-response.md#L174-L184).

`prompt-governance` converts keyword and template syntax matches into safety verdicts.
Its catalog manager uses the supplied prompt name in a write path without a containment check, and writes before checking for duplicate content.
See [audit verdict logic](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/prompt-governance/scripts/prompt_auditor.py#L171-L235), [catalog write](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/prompt-governance/scripts/prompt_catalog_manager.py#L129-L151) and [CLI name handling](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/prompt-governance/scripts/prompt_catalog_manager.py#L333-L364).
Do not add this approval registry or safety gate.

`analytics-engineer` contains a grain inconsistency in its worked example.
The fact query joins order items but retains `order_id` as the unique key and copies the order total onto each item.
The next metric sums that total, which can multiply revenue for multi-item orders.
See [fact grain](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/data-analytics/analytics-engineer/SKILL.md#L149-L190) and [revenue metric](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/data-analytics/analytics-engineer/SKILL.md#L202-L214).
Revisit only for a real dbt task, using the existing data specialist and warehouse-specific evidence.

`code-tour` is the most distinctive deferred artifact utility.
Symbol-based stops and fingerprints can help maintain an ownership handoff.
The validator uses unqualified Python symbols or a substring window, and its why-ratio is a word-count and marker heuristic.
See [anchor lookup](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/code-tour/scripts/tour_validate.py#L46-L80) and [note scoring](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/engineering/code-tour/scripts/tour_render.py#L22-L55).
Pilot only when a maintained tour is needed, retaining `how` and `why` as the explanation workflow.

## Standards and persona assessment

Borghei separates skills, agents and personas, but Son already separates domain procedure, routing and scoped execution.
Importing the additional hierarchy would multiply the same responsibilities.
The DS wrapper hardcodes `sonnet` and its own tool list.
See [orchestration hierarchy](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/standards/orchestration-protocol.md#L16-L47) and [DS agent header](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/agents/engineering/cs-data-scientist.md#L1-L7).

Keep useful package boundaries and explicit handoff contracts as existing workflow practices.
Do not promote the author's 40% time-saving and 30% consistency thresholds, universal score floors, fixed handoff caps or mandatory persona hierarchy into Son principles.
See [quality threshold](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/standards/skill-authoring-standard.md#L289-L298) and [chain rules](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/standards/orchestration-protocol.md#L245-L260).
`extended-thinking-architect` and `self-improving-agent` also conflict with the existing model policy and native-memory boundaries.

The general lessons are already covered by `prove-it-works`, `explain-the-number`, `build-the-lever`, `encode-lessons-in-structure`, `test-behavior-not-implementation` and `sequence-verifiable-units`.
Judge calibration and data recovery remain domain methods, not new universal principles.

## Evidence and limits

The source is pinned to `4a698e8d07856fdca9ec3e69082a9d68c8dd45d0`.
The matrix records one row per real assigned skill, exact source links, inspection depth and relevant overlap.
82 rows received metadata screening, nine received complete skill-body reads and nine received complete skill bodies plus targeted support-code review.
Support depth does not imply every supporting file was reviewed.
The JSON lists the actual support files and relevant ranges.

No creator code was executed.
No package was installed, no platform behavior was tested and no accepted source, manifest, tracked file or global configuration was changed.
The review used Son's investigation playbook, skipping nested agents because the parent had already divided the work and prohibited delegation.
The installed runtime pointed to an absent local model configuration, so this agent inherited its parent role.

The older memory notes informed source preservation and specialist boundaries.
The current baseline supplied the present stack and existing `predictive-modeling` import status.
All future imports must retain the creator's MIT + Commons Clause licensing and supporting files.

The output validation checks that the real assigned inventory and matrix paths match exactly, each path appears once, every row has required fields and an allowed disposition/depth, and the fixture stays excluded.
This verifies the review artifact, not the creator utilities.

Validation passed for all 100 matrix rows, the excluded fixture and 68 cited ranges across 46 pinned source files.

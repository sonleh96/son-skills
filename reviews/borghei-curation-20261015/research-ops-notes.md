Recommend two conditional specialist pilots, [litreview](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/research/litreview/SKILL.md#L33-L51) and [process-mapper](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/business-operations/process-mapper/SKILL.md#L34-L41).
Keep the creator packages intact, including supporting files, provenance and MIT plus Commons Clause licensing.
Use Son mode to select a bounded stage and son-agent for scoped execution only when delegation is authorized.
Do not add research, operations, finance, legal, or industry personas.
No new universal principle is warranted by this slice.

I screened all 68 real skills in the seven assigned domains.
Twenty-five skills received full-body reads, including seven with supporting source inspection.
The remaining 43 received metadata and scope screening only.
The matrix records 2 borrow-skill, 7 playbook-input, 50 defer-specialist, 8 ignore-duplicate, and 1 ignore-conflict decisions.
All 68 inventory bodies exactly match Git blobs at commit `4a698e8d07856fdca9ec3e69082a9d68c8dd45d0`.
No creator code ran.

| Candidate | Increment beyond the current stack | Recommendation and limit |
| --- | --- | --- |
| litreview | A recorded search protocol, inclusion and exclusion decisions, review-type choice, theme evidence table, and citation audit. | Pilot as a source-preserving specialist package for literature reviews. Do not let the bundled quality or theme scores decide inclusion or the strength of a claim. |
| process-mapper | A concrete step inventory, observed timestamps, handoffs, rework, and separate valuation of touch time and elapsed time. | Pilot for one real operational process. Treat its payback output as an estimate from declared inputs, and its diagnostic thresholds as hypotheses to check. |
| dossier | Audience-specific briefing structure and explicit fact, inference, and speculation labels. | Feed an executive evidence-brief playbook. Existing research and finance tools already handle retrieval and briefing production. |
| product-research | Method selection, recruitment coverage, and evidence attached to participants and channels. | Feed product discovery planning around the installed PM interview and synthesis skills. Discard the automatic confidence gate. |
| knowledge-ops | Ownership, review dates, link inventories, and an explicit audit date. | Feed a read-only knowledge audit. Do not import zero-traffic deletion or a universal health score. |
| grants and research-finance | Funder-fit questions, proposal structure, cost blocks, and spend versus delivery. | Defer until an actual call or funded program exists. Their scores and budgeting assumptions need task-specific validation. |

The installed `/Users/sonle/.codex/skills/research/SKILL.md` already directs primary-source investigation and a cited Markdown artifact.
I read it in full.
The supplied `baseline.json` lists `research` in both `curated_skills` and `installed_codex_names`.
The missing capability is a literature-review protocol, not research access or a researcher role.
Litreview's [search record](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/research/litreview/references/search-strategy-and-prisma.md#L31-L42) and [theme evidence table](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/research/litreview/references/synthesis-and-citation-management.md#L36-L88) are the useful additions.
For the PNG paper, choose a scoping or narrative review when that matches the question, record the limits, and keep literature support separate from validation of the local screening results.
The source itself offers [alternative question frames and review types](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/research/litreview/references/search-strategy-and-prisma.md#L5-L27), so PICO is not a requirement for every question.

A small explicit compatibility adapter is sufficient for a protocol-focused litreview pilot.
It should require the existing research skill for source retrieval, choose the frame and review type for the task, preserve inclusion reasons and contradictions, and treat query and score outputs as drafts that cannot decide truth or eligibility.
Preserve the original package rather than rewriting its methods into Son prose.
This is a recommendation to borrow its procedure and references, with helpers optional.
If adoption means accepting its automated triage and synthesis labels as operational tools, defer it until the helpers are corrected and tested.
That would require real method and code work, not a cosmetic adapter.

The process-mapper pilot needs the same distinction between useful procedure and unvalidated automation.
The installed business-analyst already covers process maps and cost-benefit analysis broadly.
Borghei adds a usable [capture schema and validation sequence](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/business-operations/process-mapper/references/process-capture-methods.md#L92-L175) and a useful [separation of labor and elapsed-time value](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/business-operations/process-mapper/SKILL.md#L148-L164).
Its adapter should preserve observed baseline data, declared assumptions, modeled savings, and measured results as separate fields.
A manager's estimate is not an observed timestamp, predicted time saved is not realized savings, and a payback ranking is not an implementation decision.
The source's fixed approval-rejection threshold must never authorize removing a control.
Verify any later intervention by comparing the same process variant and observation window after implementation.

| Source finding | Evidence and implication |
| --- | --- |
| Literature quality score favors venue and study type. | [Source scorer lines 53-58](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/research/litreview/scripts/source_quality_scorer.py#L53-L58) assign fixed design and venue scores. Use claim-specific methodological assessment for exploratory, geospatial, education, and engineering studies. |
| The supplied as-of date does not control recency scoring. | [Source scorer lines 175-184](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/research/litreview/scripts/source_quality_scorer.py#L175-L184) use the machine year while reporting the supplied date. This undermines reproducible scoring. |
| Theme labels can hide conflicting evidence. | [Theme scorer lines 62-80](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/research/litreview/scripts/thematic_synthesis_builder.py#L62-L80) call three supportive records strong even with one disconfirming record, before checking contested status. [Lines 99-127](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/research/litreview/scripts/thematic_synthesis_builder.py#L99-L127) also count each finding item rather than distinct sources. |
| Search builder is a template generator. | [Query builder lines 93-110](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/research/litreview/scripts/search_strategy_builder.py#L93-L110) join supplied terms but do not apply the declared database-specific field syntax. It neither searches nor verifies coverage. |
| Process payback is assumption-driven arithmetic. | [Improvement scorer lines 43-89](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/business-operations/process-mapper/scripts/improvement_scorer.py#L43-L89) calculate from supplied savings, volume, labor rate, effort and cycle-time value. [Lines 21-40](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/business-operations/process-mapper/scripts/improvement_scorer.py#L21-L40) impose fixed confidence, risk and tier factors. |
| Process totals do not establish causal or net improvement. | [Process analyzer lines 114-131](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/business-operations/process-mapper/scripts/process_analyzer.py#L114-L131) sum a sequential path and infer constraints from elapsed share. [Portfolio lines 176-190](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/business-operations/process-mapper/scripts/improvement_scorer.py#L176-L190) add benefits without establishing that opportunities do not overlap. |
| Dossier helpers check declared metadata. | [Independence checker](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/research/dossier/scripts/source_triangulation_validator.py#L90-L104) trusts dependency labels. [Statement checker](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/research/dossier/scripts/fact_inference_separator.py#L69-L127) uses categories, counts and language substrings. Neither validates truth. |
| Knowledge audit can turn missing data into deletion advice. | [Directory scanner](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/business-operations/knowledge-ops/scripts/kb_health_auditor.py#L68-L87) sets every page's traffic to zero and supplies no link graph. [Orphan triage](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/business-operations/knowledge-ops/scripts/orphan_detector.py#L49-L90) defaults missing traffic to zero and recommends deletion for unlinked pages. Missing observations must remain unknown. |
| Knowledge audit misreads valid ownership and concise content. | [Auditor constants](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/business-operations/knowledge-ops/scripts/kb_health_auditor.py#L35-L38) flag any owner containing @ as an alias and define fewer than 250 words as thin. These are poor defaults for named email owners and small principle skills. |
| Grant fit has code-level scoring defects. | [Shared high score](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/research/grants/scripts/funder_fit_scorer.py#L44-L44) is 15, while [geography maximum](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/research/grants/scripts/funder_fit_scorer.py#L79-L83) is 10. A maximum input can score 105/100. [The recommendation branch](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/research/grants/scripts/funder_fit_scorer.py#L126-L149) can rate an out-of-scope topic strongly because it only skips when the entire total is zero. These are static deductions, not runtime reproductions. |
| Research confidence and portfolio value are heuristics. | [Insight scorer](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/research-ops/product-research/scripts/insight_confidence_scorer.py#L78-L137) counts labels and participants without examining contradiction or claim meaning. [Research allocation](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/research-ops/research-finance/scripts/portfolio_prioritizer.py#L109-L132) greedily selects by a declared-value ratio. Neither output is validated probability or decision value. |

Concrete playbook proposals are below.
Build the first two only if the pilots earn their place through actual tasks.
The others are follow-up ideas, not a request to add six workflows at once.

| Outcome | Existing skills to reuse | Increment from Borghei | Completion evidence |
| --- | --- | --- | --- |
| Literature evidence review | research, data-scientist only for statistical appraisal, pdf, documents | litreview search log, screening reasons, evidence matrix and citation hygiene | Saved queries and dates, source inventory, inclusion reasons, cited claims, contradictory evidence and review limitations. |
| Operational process decision | business-analyst, data-analytics:validate-data, spreadsheets | process-mapper capture fields, handoff map, separate touch and elapsed savings | One observed variant, baseline timestamps, reconciled map, explicit assumptions and an improvement proposal. A future implementation needs a new measured comparison. |
| Executive evidence brief | research, documents, presentations, or existing Investment Banking meeting-prep for a deal | dossier outline and claim-category ledger | Decision-focused brief with source provenance, stated inferences, unresolved questions and an as-of date. |
| Product discovery evidence readout | installed PM assumption, interview-script and summarize-interview skills, metric-diagnostics | product-research method selection and recruiting coverage | Decision and method rationale, participant coverage, source-linked claims, negative cases and explicit uncertainty. |
| Document comparison | pdf, documents, spreadsheets, legal-advisor when legal interpretation is requested | tabular-document-review column schema, document manifest and NOT FOUND status | Every source document represented, defined columns, cell citations, explicit missing values and direct checks of consequential cells. |
| Knowledge handoff audit | documentation-and-adrs, pages:maintain-space, existing handoff workflow | knowledge-ops ownership and freshness inventory | Explicit audit date, owner and retention checks, tested links and a proposed remediation list. Archive or deletion happens only with the required authority. |

The financial skills add little beside the available Investment Banking index, native spreadsheets, metric diagnostics and cohort analysis.
The Data Analytics market-sizing skill already covers source-backed inputs, audit-ready calculations, sensitivity and validation priorities.
The installed PM interview and summarize-interview skills already handle much of product-research's execution.
The native document, PDF and spreadsheet skills already cover the practical document formats that tabular-document-review explicitly leaves to external tools.
These comparisons distinguish available capabilities from capabilities curated into Son.
The current baseline proves availability, not that a connector can read a particular future source.

Do not turn an industry checklist into a principle.
The [EdTech defaults](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/vertical-advisors/edtech-advisor/SKILL.md#L32-L64) center US student-data rules and district sales.
The [FinTech workflow](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/vertical-advisors/fintech-advisor/SKILL.md#L63-L84) explicitly targets US/EU regimes.
The RA/QM collection should remain task-triggered for a named regulation, certification or medical-device program.
Clinical research is separate from the PNG exploratory inspection screen; its [stated limits](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/research-ops/clinical-research/SKILL.md#L24-L32) concern clinical operations and simple parallel study designs.
No live legal, regulatory or clinical validity review occurred here.

Reject procurement-optimizer as a default package because it prescribes [serving notice on every auto-renewal](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/business-operations/procurement-optimizer/SKILL.md#L131-L145) and treats the step as costless.
Any useful spend inventory can be recreated within an authorized contract-aware task without importing that standing instruction.
The same caution applies to routine notice suggestions in vendor-management, which remains deferred.

The portable lessons are already represented by pstack.
Observing the actual process and checking a citation belong under prove-it-works.
Showing why a score or saving has its value belongs under explain-the-number.
Removing redundant steps before automating them belongs under subtract-before-you-add and laziness-protocol, subject to actual control requirements.
An owner, source record or check encoded in metadata belongs under encode-lessons-in-structure.
Keep these as examples within task playbooks rather than creating competing principles.

Inspection detail is in `research-ops.json` under `entries`, `evidence`, `support_inspections` and `baseline_checks`.
The review followed the parent contract and investigation playbook, with nested how-agent work skipped because the parent forbade delegation.
The configured runtime pointed to a missing `.local/models.codex.json`, so the assigned model was retained.
This researcher performed self-review; parent inspection is still required.
No source package, manifest, tracked file, global configuration, installed skill or native memory changed.

The JSON coverage can be checked without running any creator code:

```python
import json
from pathlib import Path
root = Path('/Users/sonle/Documents/work/son-skills/.local/borghei-review-20261015')
report = json.loads((root / 'research-ops.json').read_text())
inventory = json.loads((root / 'inventory.json').read_text())
expected = {e['path'] for e in inventory['entries']
            if e['domain'] in report['assigned_domains'] and not e['fixture']}
actual = [e['path'] for e in report['entries']]
assert len(actual) == len(set(actual)) == 68
assert set(actual) == expected
```

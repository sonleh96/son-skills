# Combination decisions

Each task has one combined workflow that owns its sequence and output.
Other creators contribute techniques or reference material.
The combined workflow governs execution; upstream source text does not automatically activate tools, agents, or side effects.

| Area | Relationship | Decision |
| --- | --- | --- |
| Matt interviews, domain modeling, and questionnaires | Complementary stages of resolving a decision | Combine in `son-clarify`, with explicit interview, glossary, and external-questionnaire modes |
| Matt specs and tickets; pstack architect | Complementary planning artifacts | `son-plan` owns the spec and task graph; sketches are proportionate to uncertainty |
| Matt implement-spec; pstack mode, arena, and swarm | Competing orchestration and model assumptions | Keep ticket ordering in `son-build`; use one writer unless delegation is separately authorized |
| Matt and pstack TDD | Shared red-before-green discipline, different default test seams | Son's failure-mode and end-to-end policy wins; use the closest meaningful reproduction for a bug |
| Matt diagnosing-bugs; pstack root-cause and benchmark guidance | Complementary diagnosis and measurement | `son-debug` owns the loop and labels unreproduced hypotheses |
| Matt code-review; pstack interrogate and blast-radius | Overlapping review plus useful downstream analysis | One `son-review` flow, separate spec and standards passes, executable proof for material risks |
| Pstack verification generation and maintenance | Complementary lifecycle stages | One `son-verify` skill with distinct one-time, creation, maintenance, and benchmark modes |
| Matt pr; HumanLayer visual-pr and show-me | Substantial overlap with shared ancestry | One `son-pr` flow; repository templates win and visuals are optional |
| Pstack how, why, teach, and bro; Matt teach and wait-what; HumanLayer show-me | Overlapping explanations with different evidence needs | `son-explain` distinguishes runtime behavior, historical rationale, teaching, and rephrasing |
| Matt retro; pstack reflect and correct | Overlapping learning loops | `son-retro` proposes evidence-backed improvements; applying changes follows existing authority |
| Matt writing-for-agents; pstack technical-writing and unslop; HumanLayer improve-claude-md | Overlapping writing guidance and a Claude-specific mechanism | `son-writing` handles document structure; installed personal unslop remains mandatory; XML is optional and local |
| HumanLayer loop design and loop packaging; pstack automate-me | Complementary automation design, packaging, and preference discovery | `son-automate` uses the active scheduler and bounded work; it does not auto-create personal modes |
| Matt prototype; Emil prototype; pstack design-space exploration | Same name, different output | `son-prototype` chooses a behavior experiment or visual picker; no automatic promotion to production |
| Emil motion construction, review, audit, naming, and discovery | Shared domain with conflicting write scopes | `son-motion` selects mode before editing; audits and opportunity scans leave product code unchanged |
| Emil web design, Apple-style interaction, mobile web, and Sonner | Complementary specialist guidance | `son-ui` reuses product tokens and preserves rendered verification and device caveats |
| Emil break-ui; HumanLayer narrow props | Complementary stress testing with possible fixture conflict | `son-ui-stress` uses valid extreme data and never widens production contracts for a demo |
| HumanLayer prop narrowing; pstack types; Matt deep modules; Emil Swift | Shared contract discipline across distinct languages | `son-types` selects by language and checks actual public contracts and compiler mode |
| Matt research; pstack how and why | Source investigation with different scopes | `son-research` uses primary sources, distinguishes inference, and avoids mandatory background agents |
| Matt handoff; pstack recall | Overlapping continuity | `son-handoff` follows the existing cross-harness protocol and leaves generated memory to its hooks |

## Conflicts resolved by Son's rules

The following adaptations are intentional and should survive future upstream refreshes.

- Analysis stays analysis unless the user also asked for implementation.
- A request to draft a spec or PR body does not authorize publishing it.
- Model selection stays in the canonical model policy.
- Delegation requires active authorization and available tools.
- Unit tests do not become the default for user-visible behavior merely because they are cheap.
- Test fixtures do not broaden production types, but undocumented public consumers are not assumed absent.
- Creator-specific absolute paths and Claude or Cursor APIs are not portable tool calls.
- A retrospective does not automatically write global skills, memory, or backlog tickets.
- A planning flow does not force another interview after the user has already settled the decision.
- A preview or compiled artifact is not proof of acceptance or deployment.

## Deliberate exclusions

`setup-pstack` is excluded from activation because it writes model rules that would compete with Son's existing configuration.
`no-comments` is excluded because its broad deletion stance and agent dependency are unsuitable as a default across repositories.
The full source remains available for selective study.

Benny, Matt's in-progress skills, and tracker-driven triage remain deferred.
Their value depends on project-specific services, experimental behavior, or authority that this repository does not supply.
Specialists such as library selection, provisioning wizards, exercise scaffolding, and dependency-specific migrations remain reference-only.

## Portability

All combined names use the `son-` prefix, avoiding collisions with the installed creator skills.
The canonical source includes explicit-only frontmatter where applicable.
Codex builds encode this in `agents/openai.yaml` and omit Claude's unsupported frontmatter extension.
Claude and Cursor builds retain `disable-model-invocation`.
Each build copies shared references into the skill, so installation does not depend on a symlink back to this checkout.
Detailed source Markdown is bundled under reference directories with `SKILL.md` renamed to `SOURCE.md` to avoid duplicate discovery.
Those documents may refer to upstream dependencies outside the selected folder; pinned provenance links locate the originals.

## Change ownership

Update `skills/` for deliberate workflow changes and `policies/` for shared behavior.
Update `stack.json` when source mappings change.
Regenerate catalogs and bundles with the scripts.
Accepted source snapshots and hashes move together only after review.
The two-week automation never changes them.

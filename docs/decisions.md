# Routing and adaptation decisions

The 95 active creator skills keep their own workflows and supporting files.
Son mode selects a playbook and loads the relevant originals.
Shared compatibility rules resolve conflicts without rewriting each skill.

| Area | Relationship | Route |
| --- | --- | --- |
| Matt grilling, domain modeling, specs, and tickets | Complementary stages | Product-planning playbook; skip settled stages |
| Matt implement-spec and pstack feature orchestration | Competing owners for execution | Select one primary playbook and implementation owner |
| Matt and pstack TDD | Overlap with different default test seams | Keep both names; Son's failure-mode and end-to-end policy wins |
| Matt code-review, pstack interrogate, and blast-radius | Overlapping review with distinct risk checks | Choose the relevant review; add downstream proof where needed |
| Verification creation and maintenance | Complementary lifecycle stages | Keep separate skills and choose by existing project state |
| Matt pr, HumanLayer visual-pr, and show-me | Related communication workflows | Use pr for PR prose, show-me for explanation, visual-pr when explicitly requested |
| Matt and pstack teach | Different teaching approaches | Preserve both with creator prefixes |
| Matt retro and pstack reflect or correct | Overlapping learning loops | Choose task retrospective, broader reflection, or a specific correction |
| Technical writing, writing-for-agents, and improve-claude-md | Different audiences and formats | Route by artifact; apply personal unslop to prose |
| HumanLayer loops and pstack automate-me | Complementary discovery, design, and packaging | Agent-automation playbook; use the supported scheduler |
| Matt and Emil prototype | Same name, different purpose | Matt for a behavior experiment; Emil for interface alternatives |
| Emil motion skills | Different write scopes | Keep construction, review, audit, naming, and discovery separate |
| Emil break-ui and HumanLayer prop narrowing | Stress data versus production contracts | Use realistic valid data; inspect public consumers before narrowing exported types |
| Matt handoff and pstack recall | Overlapping continuity | Follow Son's canonical continuation protocol |

## Minimal changes

Each original receives a one-line compatibility reference, license copy, and discovery metadata.
The six colliding skill names receive creator prefixes.
Explicit references and resolvable relative links follow those names.
Ordinary prose, examples, and support files remain intact.
Build-time frontmatter translation supports the target application's schema without editing the canonical body.

`stack.json` records the exact source path and the hashes of each initially adapted file.
The update checker compares those hashes with current local files to distinguish later edits from the adapter.
Never refresh the imported baseline merely to make a local customization disappear from a report.

## Controls and principles

`setup-son-skills` keeps pstack's model discovery, reasoning presets, role table, and confirmation flow.
It writes local configuration instead of a competing global model rule.
`son-mode` owns the playbook and completion loop.
`son-agent` loads that mode for scoped delegated work when the active application allows it.
The 24 pstack principle skills remain intact and available.

`update-son-skills` is Son's on-demand review command.
Its comparison tool fetches upstream files as data and never runs their scripts.

## Inactive originals and external dependencies

Benny's three automations need separate service and notification configuration.
Pstack's poteto-mode, setup-pstack, and poteto-help are replaced by the Son controls.
Matt's seven in-progress and four miscellaneous skills remain catalogued but inactive.

Other promoted originals remain available, including tracker setup and specialist skills.
Their external dependencies are not installed automatically.
`no-comments` still requires Comment Sicko; Son compatibility forbids substituting broad comment deletion.
Pstack's deslop and control tools also require available equivalents or an explicit unmet-capability report.

## Ownership

Edit originals under `skills/` only for a deliberate customization.
Edit shared differences in `policies/compatibility.md` and routing in `skills/son-mode/`.
Keep source mappings accurate and regenerate the catalog and builds.
Accepted snapshots and locks move together only after a reviewed adoption.

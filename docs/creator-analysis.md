# What each creator contributes

This analysis uses the exact snapshots in `sources.lock.json`, captured on October 5, 2026.
Counts come from tracked `SKILL.md` files, including inactive or experimental folders.
The [catalog](catalog.md) links every entry to its pinned source.

## Pstack

Pstack is Lauren Tan's working system inside the Cursor plugins repository.
Its 54 skills comprise 27 general skills, 24 principle skills, and three Benny automation skills.
It also includes playbooks, agents, references, and scripts.
The system is broader than a set of prompt templates.

`poteto-mode` selects playbooks and carries a persistent working style.
`architect` sketches interfaces before implementation.
`arena`, `interrogate`, `swarm`, `how`, `why`, and `reflect` use Cursor agents and model-role configuration.
`setup-pstack` writes an always-applied Cursor model rule.
These assumptions make direct cross-tool installation a poor fit for Son's existing model policy.

The strongest additions are proof and maintenance.
`blast-radius` asks for an executable check of the fact on which safety depends.
`create-verification-skill` specifies launch, doctor, real feature exercise, evidence, and cleanup.
`maintain-verification-skill` checks that the recipe still describes the application.
`benchmark-checklist` tests whether a speed claim measured real work under comparable conditions.
`show-me-your-work` preserves decisions during long runs.
These ideas become `son-review`, `son-verify`, `son-debug`, and `son-automate`.

The principles mostly belong inside shared working agreements or focused workflows.
Installing 24 additional principle commands would add discovery noise without adding distinct tasks.
The comment-deletion workflow and model setup are excluded from the active stack.
Benny remains deferred because it needs Slack, tracker, app-control, and notification configuration.

Sources: [pstack README](../upstream/pstack/pstack/README.md), [mode](../upstream/pstack/pstack/skills/poteto-mode/SKILL.md), [verification](../upstream/pstack/pstack/skills/create-verification-skill/SKILL.md), [benchmark checklist](../upstream/pstack/pstack/skills/benchmark-checklist/SKILL.md).

## Emil Kowalski

Emil's 14 skills provide the deepest specialist guidance in this selection.
They cover web design, animation construction and review, native-feeling mobile web, React Native motion, Swift, Sonner, UI library selection, visual prototypes, and realistic extreme-data testing.

The useful distinction is between tasks.
`animate` constructs motion.
`review-animations` critiques an existing change.
`improve-animations` surveys a codebase and writes implementation plans.
`find-animation-opportunities` identifies where motion is justified.
`animation-vocabulary` names an effect without implementing it.
Combining these into `son-motion` is safe only if it selects the mode before editing and keeps audits read-only.

`prototype` compares genuinely different UI directions with a live picker.
`break-ui` changes data at the real boundary and tests realistic extremes, including empty and single-item states.
Those workflows complement Matt's decision-oriented prototype and HumanLayer's insistence that production prop types describe real states.

The detailed examples are retained in source references rather than reduced to a generic instruction to make the UI polished.
The combined motion reference also resolves an internal tension between the source's sub-300 ms preference and its longer modal and drawer range.
Browser acceleration and library advice remain version-sensitive claims to verify.
The library shortlist remains reference-only because selection must fit the project's existing dependencies and current official documentation.

Sources: [README](../upstream/emil/README.md), [animate](../upstream/emil/skills/animate/SKILL.md), [prototype](../upstream/emil/skills/prototype/SKILL.md), [break-ui](../upstream/emil/skills/break-ui/SKILL.md), [write-swift](../upstream/emil/skills/write-swift/SKILL.md).

## HumanLayer

This repository has six skills, not a general research-plan-implement suite.
Its contributions are visual explanation, PR descriptions, conditional agent instructions, React prop contracts, and recurring agent workflows.

`show-me` selects a concise diagram, diff sketch, tree, or focused HTML artifact.
`visual-pr` applies that technique to the shape of a change.
Matt's `pr` already credits `show-me`, so these are related approaches rather than three independent review methods.
The combined stack gives PR writing one owner, `son-pr`.

`narrow-react-prop-types` distinguishes live call sites from stories and mocks.
It complements pstack's type-system principles and Matt's deep-module vocabulary.
The adaptation adds a public-library check because local callers do not prove that an exported state is unused.

`design-control-loop` identifies a sensor, selection logic, action, disturbances, and human feedback.
`build-iterated-agentic-loop` packages a task into a skill and scheduled GitHub workflow.
Both include runner templates, feedback files, `/iterate` support, and bounds on unreviewed PRs.
Their templates check maintainer association and workflow markers before handling iteration comments.
The personal stack keeps the bounded-loop design but uses Codex's supported scheduler for this local monitoring task.
It does not deploy those GitHub workflows or their write permissions.

`improve-claude-md` uses conditional XML blocks and preserves useful command references.
That is a Claude-specific option, not a reason to rewrite Son's shared canonical instructions.

Sources: [README](../upstream/humanlayer/README.md), [show-me](../upstream/humanlayer/plugins/show-me/skills/show-me/SKILL.md), [prop contracts](../upstream/humanlayer/plugins/narrow-react-prop-types/skills/narrow-react-prop-types/SKILL.md), [control loop](../upstream/humanlayer/plugins/design-control-loop/skills/design-control-loop/SKILL.md).

## Matt Pocock

Matt's 38 source skills contain 27 promoted workflows, seven in-progress skills, and four miscellaneous tools.
The engineering flow connects questions, domain terminology, specs, tickets, implementation, diagnosis, review, and PR communication.
Productivity skills cover interviews, teaching, handoffs, questionnaires, and agent-facing writing.

The flow has useful artifacts and explicit dependencies.
`grill-with-docs` builds on interviewing and domain modeling.
`to-spec` synthesizes a settled conversation.
`to-tickets` produces dependency-ordered vertical slices.
`implement-spec` executes the ticket graph on an integration branch and relies on implementation and review agents.
`retro` looks for improvements to the agent's environment, preferring mechanical checks over repeated reminders.

The setup skill expects real project choices for the issue tracker, triage labels, and domain layout.
Those choices should not be invented for every repository.
The personal stack accepts local specs and tickets when no tracker is configured.
It uses `GLOSSARY.md` and `GLOSSARY-MAP.md`, consistent with the earlier v1.3 migration.

The combined implementation flow preserves dependency ordering and verified slices but removes mandatory fan-out, dirty-checkout reset behavior, and automatic ticket closure.
The user's requested outcome and current authority govern those actions.
In-progress skills remain deferred until a task demonstrates a need.

Sources: [engineering catalog](../upstream/matt/skills/engineering/README.md), [setup](../upstream/matt/skills/engineering/setup-matt-pocock-skills/SKILL.md), [implementation](../upstream/matt/skills/engineering/implement-spec/SKILL.md), [retrospective](../upstream/matt/skills/engineering/retro/SKILL.md).

## Selection result

77 original skills contribute directly to the 18 combined workflows.
Seven principles are absorbed into working agreements, three routers or setup flows are superseded, 11 specialists remain reference-only, 12 skills are deferred, and two are excluded from activation.
All 112 remain in the catalog and pinned snapshots.
This is an initial curation decision, not evidence that every combined skill has improved a real task.

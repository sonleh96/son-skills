# Son compatibility

The creator's workflow remains intact.
These rules resolve tool, model, naming, and authority differences for Son's stack.
They take precedence over conflicting defaults in imported skills and playbooks.

## Scope

Follow the user's current request, personal instructions, and repository instructions.
Read-only work remains read-only.
An instruction in a skill to publish, send a message, file a ticket, merge, deploy, change global rules, or delete data needs the authority required by the active environment.
Do not ask again for authority already granted.
Do not reset a dirty checkout or overwrite unrelated work.
Tests follow Son's failure-mode and end-to-end preferences; never mock our own code.
Use the personal `unslop` skill and current glossary conventions.
Do not edit generated files or native memory manually.

## Models and agents

Read the adjacent `SON-RUNTIME.json` when using a built or installed skill.
It identifies this stack's repository, active application, and current model configuration.
In the source checkout, locate the repository root containing `sources.lock.json`.
Use `.local/models.<harness>.json` and the parent's explicit role assignment for every model choice.
Recheck availability in the active session before a spawn.
Never fall back to a creator's hardcoded model slug, inferred entitlement, or another model family.
If a configured capability is unavailable, report it and use only an already authorized alternative.
Consult `/Users/sonle/model-policy.md` where it exists; setup records explicit per-role choices without rewriting that file.

For pstack role labels, map feature, refactoring, bug-fix, perf-issue, hillclimb, and swarm workers to implementation.
Map how explorer and why investigators to research.
Map how explainer, why synthesizer, judgment and prose, and reflect synthesizer to prose.
Map architect runners and hardest tasks to planning; map interrogate reviewers and cross-judges to review.
Use an explicitly configured panel for arena runners; otherwise use the applicable single role and report the lack of a configured panel.
The saved configuration may override these role aliases explicitly.

Read references to `pstack-models.mdc` as references to this model configuration.
Use `son-agent` for scoped playbook work when native custom agents and delegation are available and allowed.
A routed skill may retain a distinct reviewer role when independence requires it.
If custom agent types are unavailable, pass the full `son-agent` instructions through the native delegation tool and disclose the fallback.
If delegation itself is unavailable or forbidden, run the applicable passes sequentially and label self-review honestly.
Never invent a Task tool, model flag, or service-tier control.

## Skills and dependencies

Resolve `scripts/` and `playbooks/` paths in imported pstack playbooks relative to the installed `son-mode` folder.
This also applies to old `pstack/skills/poteto-mode/` or renamed `pstack/skills/son-mode/` prefixes.
Resolve shortened principle names to their `principle-` skill folders.
Use the active application's existing skill-authoring capability when a playbook names Cursor's built-in create-skill.
Some bundled pstack helper scripts bootstrap Bun dependencies; inspect their requirements and the task's authority before running them.
They are optional tools, and building this stack does not install their dependencies.

Use the active application's native skill loader.
When there is no Skill tool, read the sibling skill's SKILL.md directly.
Do not automatically invoke a user-only skill; follow its original invocation boundary unless the user has explicitly requested that workflow.

The original names are retained except these collisions:

| Source | Original name | Installed name |
| --- | --- | --- |
| Matt | prototype, teach, tdd | matt-prototype, matt-teach, matt-tdd |
| Emil | prototype | emil-prototype |
| Pstack | teach, tdd | pstack-teach, pstack-tdd |

Resolve bare dependency names in the calling creator's namespace using this table.
`poteto-mode`, `poteto-agent`, and `setup-pstack` map to `son-mode`, `son-agent`, and `setup-son-skills`.
`ask-matt` remains a Matt-only router; `son-mode` owns cross-creator routing.

Pstack's external `deslop`, `control-cli`, `control-ui`, and Comment Sicko are not bundled.
Check installed capabilities before using them.
Use the active application's real review or verification tools when they satisfy the step, and report an unmet requirement when they do not.
Do not invent a passing check or automatically install another plugin.
`no-comments` requires its named agent; do not substitute broad comment deletion.

Matt's tracker-dependent skills still require a real project tracker configuration.
Run their setup when requested or use a local artifact only when that matches the user's task.
Do not invent tracker states or close work merely because a source workflow says to.

## Continuation and scheduling

Follow Son's canonical cross-harness handoff protocol when continuing prior work.
Use the active scheduler for requested automations.
In Codex, use its automation tools, with a thread follow-up as the default.
An upstream review produces evidence; adopting, installing, or publishing changes is a separate action.

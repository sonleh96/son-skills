# Son's skills

Son's personal stack for Codex, Claude Code, and Cursor.
It brings together pstack's engineering workflows, Matt Pocock's planning and implementation skills, Emil Kowalski's interface and motion guidance, and HumanLayer's explanation and automation skills.

Start with `/son-mode` when a task needs rigor.
Give it the problem and the result you want.
It chooses a playbook, reads the skills that apply, and works through verification and cleanup.
The creator skills keep their original instructions and examples, so you can inspect the method or use a skill directly.

## Install

This repository is local and has not been installed globally or published.
From this checkout, preview the installation for the application you use:

```bash
# Codex
python3 scripts/stack.py install --harness codex --dest "$HOME/.codex/skills"

# Claude Code
python3 scripts/stack.py install --harness claude --dest "$HOME/.claude/skills"

# Cursor
python3 scripts/stack.py install --harness cursor --dest "$HOME/.cursor/skills"
```

Pick one command and add `--apply` to install.
The installer builds the skills and `son-agent`, checks for conflicts, then copies them into place.
If you already have a skill with the same name and different contents, it stops before installing anything.
Review that difference before replacing an existing copy.

For a project-only install, use that project's skill directory as `--dest`.
See [setup](docs/setup.md) for the file locations and application-specific details.
The commands below become available after installation and an application refresh.
Use `$son-mode` and the other `$skill-name` forms in Codex, or slash commands where supported.

## Get started

1. Run [`/setup-son-skills`](skills/setup-son-skills/SKILL.md).
   Pick a reasoning budget and choose models for the roles you need.
2. Use [`/son-mode`](skills/son-mode/SKILL.md) at the start of substantial work.
   Describe the task, constraints, and what would count as done.

For example:

```text
/son-mode the list jumps when I load the next page. Reproduce it, fix the cause,
and verify scrolling with both short and long results.
```

```text
/son-mode turn our settled discussion into a spec and dependency-ordered tickets.
Keep the output local for now.
```

```text
/son-mode compare two layouts for this onboarding flow. Build both so I can try
keyboard navigation and see how they handle long names and error messages.
```

You do not need to remember every skill name.
The playbook selects the skills its steps need, while preserving skills that require an explicit request.
For a small, specific job, call the relevant skill directly.

## Choose your models

`/setup-son-skills` checks which models and reasoning controls the active application exposes.
It asks you to choose a budget, then shows assignments for planning, implementation, review, research, prose, and UI.
You can accept the table or change individual roles.
If the application cannot list your models, setup asks you for the available choices.

| Budget | Target reasoning effort |
| --- | --- |
| Small | Medium |
| Medium | High |
| Large | Extra high |
| Unlimited | Max |

These presets control reasoning effort, not spending or token limits.
For a selected model, setup chooses the highest supported effort at or below the target unless you explicitly choose another supported setting.
Choose `inherit-parent` to keep the current conversation's model and effort.

Run setup again when you want different assignments.
It saves them under `.local/` in this repository, separately for each application.
Changing the parent conversation's model still happens in the application's model picker.
Without a saved setup, Son mode inherits the current model.

## What son-mode does

Son mode reads your request and the project's instructions, then picks one primary playbook.
It turns the applicable steps into a task list, reads the relevant principles, and loads creator skills as the work calls for them.
Already-settled decisions do not need another planning loop.

For a bug, that means reproducing the failure, tracing the cause, fixing it, and checking the same behavior again.
For an investigation, it means answering the question with evidence.
A review request stays a review.

When delegation is available and allowed, Son mode assigns scoped work to `son-agent` and inspects the result.
Otherwise, it performs the passes in the current conversation and identifies self-review as such.
It finishes by reporting what changed, what was checked, and what remains unresolved.

### Playbooks

There are 29 playbooks: 23 from pstack and six that connect the other creators' skills.
A playbook describes the sequence for a task; each skill supplies the detailed instructions for a step.

<details>
<summary>Choose a playbook by the work you need done</summary>

| Playbook | Use it for |
| --- | --- |
| [Investigation](skills/son-mode/playbooks/investigation.md) | Answer a question about the code or a design decision |
| [Bug fix](skills/son-mode/playbooks/bug-fix.md) | Reproduce a defect, fix its cause, and verify the result |
| [Feature](skills/son-mode/playbooks/feature.md) | Build new behavior with a defined data shape and completion check |
| [Refactoring](skills/son-mode/playbooks/refactoring.md) | Change the structure while preserving behavior |
| [Performance](skills/son-mode/playbooks/perf-issue.md) | Measure a slowdown and compare the fix against that baseline |
| [Hillclimb](skills/son-mode/playbooks/hillclimb.md) | Improve one metric through repeated, measured experiments |
| [Runtime forensics](skills/son-mode/playbooks/runtime-forensics.md) | Investigate a live leak, CPU spike, or other runtime symptom |
| [Trace forensics](skills/son-mode/playbooks/trace-forensics.md) | Read a captured profile, trace, or heap snapshot |
| [Prototype](skills/son-mode/playbooks/prototype.md) | Try a disposable implementation to settle a design question |
| [Visual parity](skills/son-mode/playbooks/visual-parity.md) | Match an implementation to a reference interface |
| [Product planning](skills/son-mode/playbooks/product-planning.md) | Resolve requirements and terminology, then produce specs and tickets |
| [Interface design](skills/son-mode/playbooks/interface-design.md) | Explore layouts and interactions, then exercise the rendered interface |
| [Motion design](skills/son-mode/playbooks/motion-design.md) | Choose, build, or review animation for the target platform |
| [Agent automation](skills/son-mode/playbooks/agent-automation.md) | Identify repeatable work and design a bounded automation |
| [Learning and retrospective](skills/son-mode/playbooks/learning-and-retro.md) | Understand a change or examine what a session should teach you |
| [Upstream review](skills/son-mode/playbooks/upstream-review.md) | Compare your skills with the creators' latest versions |
| [Multi-phase plan](skills/son-mode/playbooks/multi-phase-plan.md) | Organize work across phases or dependent pull requests |
| [Authoring a skill](skills/son-mode/playbooks/authoring-a-skill.md) | Write or revise a skill and check its structure |
| [Evaluation](skills/son-mode/playbooks/eval.md) | Compare how a skill or prompt change affects actual agent behavior |
| [Opening a PR](skills/son-mode/playbooks/opening-a-pr.md) | Prepare ordered commits and a reviewable pull request |
| [Babysit](skills/son-mode/playbooks/babysit.md) | Resolve CI, conflicts, and review feedback until a PR is ready |
| [Shipping](skills/son-mode/playbooks/shipping.md) | Verify a stack and merge the approved work in order |
| [Autonomous run](skills/son-mode/playbooks/autonomous-run.md) | Continue a long task toward a stated completion condition |
| [Orchestrate](skills/son-mode/playbooks/orchestrate.md) | Coordinate a project across workers and multiple PRs |
| [Autopilot full](skills/son-mode/playbooks/autopilot-full.md) | Assign owners to independent PRs and carry authorized work through merge |
| [Autopilot stack](skills/son-mode/playbooks/autopilot-stack.md) | Build and verify a dependent PR stack for you to review and land |
| [Session pickup](skills/son-mode/playbooks/session-pickup.md) | Recover the evidence and current state of unfinished work |
| [Pause safely](skills/son-mode/playbooks/pause-safely.md) | Leave enough state for a clean continuation |
| [Worktree cleanup](skills/son-mode/playbooks/worktree-cleanup.md) | Inspect worktrees and remove those safe to retire |

</details>

Shipping and automation playbooks still follow the authority you gave the task.
Choosing a playbook does not grant permission to publish, merge, deploy, or send messages.

### The son-agent subagent

[`son-agent`](agents/son-agent.md) carries the same workflow into delegated work.
Before starting, it reads Son mode in full, the applicable principles, and the assigned playbook.
The parent gives it a bounded task, owned files, a model role, and completion checks.

For example, the parent can assign it to reproduce a scrolling bug and return a repeatable failing check before implementation starts.
The agent returns its artifacts and evidence; the parent reviews them before accepting the work.
The build includes a native definition for each supported application.

### Principles

Son mode indexes all 24 pstack principles and reads the full rules relevant to the task.
They affect decisions throughout the work.
For example:

- [Subtract before you add](skills/principle-subtract-before-you-add/SKILL.md) asks whether removing redundant code solves the problem.
- [Model the domain](skills/principle-model-the-domain/SKILL.md) puts the domain rules into the data structure.
- [Fix root causes](skills/principle-fix-root-causes/SKILL.md) requires tracing the symptom instead of hiding it with a guard.
- [Prove it works](skills/principle-prove-it-works/SKILL.md) requires evidence from the actual behavior or artifact.
- [Explain the number](skills/principle-explain-the-number/SKILL.md) checks what a benchmark measured before trusting the result.

Read the [full principles index](skills/son-mode/references/principles.md) for the rest.
Son's personal and repository instructions take precedence where a creator's defaults differ.
The [compatibility rules](policies/compatibility.md) explain how that applies to tests, models, tools, and task scope.

## Use a skill directly

Call a creator skill when you already know the job you want it to do.
These are a few useful starting points; the [catalog](docs/catalog.md) lists every original and whether it is active.

| Skill | Use it when |
| --- | --- |
| [/how](skills/how/SKILL.md) | You want to understand how a subsystem works |
| [/grilling](skills/grilling/SKILL.md) | A decision still has unanswered questions |
| [/domain-modeling](skills/domain-modeling/SKILL.md) | The team needs clear terms and domain boundaries |
| [/to-spec](skills/to-spec/SKILL.md) | The discussion is settled and needs a specification |
| [/diagnosing-bugs](skills/diagnosing-bugs/SKILL.md) | You have a failure to investigate |
| [/blast-radius](skills/blast-radius/SKILL.md) | A small change may affect other callers or systems |
| [/emil-prototype](skills/emil-prototype/SKILL.md) | You want to try different interface directions |
| [/animate](skills/animate/SKILL.md) | You need to implement motion in a web interface |
| [/break-ui](skills/break-ui/SKILL.md) | You want to see what realistic extreme data does to the UI |
| [/show-me](skills/show-me/SKILL.md) | A diagram or focused visual would explain the change better |
| [/create-verification-skill](skills/create-verification-skill/SKILL.md) | Your project needs a repeatable way to prove its behavior |
| [/retro](skills/retro/SKILL.md) | You want to find what should improve after a task |

Most skills keep their original command names.
Where names collide, the prefix tells you whose approach you are choosing: `matt-prototype` or `emil-prototype`, `matt-teach` or `pstack-teach`, and `matt-tdd` or `pstack-tdd`.

## Update your skills

Run [`/update-son-skills`](skills/update-son-skills/SKILL.md) whenever you want to see what the creators have changed.
You can narrow the request:

```text
/update-son-skills check Matt's latest changes. Show what affects my copies,
flag overlapping edits, and recommend which changes to adopt.
```

The command fetches the latest source and writes three comparisons for each active creator skill:

| Comparison | What it answers |
| --- | --- |
| Accepted original to latest original | What did the creator change? |
| Accepted original to your copy | What did we adapt or customize? |
| Your copy to latest original | How do they differ now? |

The report distinguishes the small compatibility edits from your later changes and flags files changed on both sides.
It includes supporting files and records the exact upstream commit.
Read the patches before adopting a change; applying the latest original wholesale would remove your customizations too.
The update command produces a review and leaves your skills unchanged.

You can run the same check from this checkout before installing anything:

```bash
python3 scripts/upstream.py check
python3 scripts/upstream.py check --source matt
```

By default, your copy means this repository's editable `skills/` directory.
Add `--installed-skills /absolute/path/to/skills` to compare an installed copy separately.
Reports go under `reviews/runs/`.
See the [saved comparison](reviews/originals-verified/report.md) for an example and [update review](docs/update-review.md) for the adoption steps.

The Codex automation runs this check every two weeks on Monday at 09:00 in the configured local timezone.
It reports meaningful new upstream changes and failed checks, and stays quiet on repeated pending diffs.
It also leaves updates for review.

## Make it yours

There are 95 active creator skills and three Son commands.
Their instructions, examples, scripts, templates, and licenses remain close to the originals.
The changes are a compatibility reference, application metadata, and renamed commands or links where needed.

| Creator | Active originals | What they contribute |
| --- | --- | --- |
| [Pstack](https://github.com/cursor/plugins/tree/main/pstack) | 48 | Engineering workflows, principles, verification, and delegation |
| [Matt Pocock](https://github.com/mattpocock/skills) | 27 | Questions, domain models, specs, tickets, implementation, and retrospectives |
| [Emil Kowalski](https://github.com/emilkowalski/skills) | 14 | Interface design, prototypes, motion, and UI stress testing |
| [HumanLayer](https://github.com/humanlayer/skills) | 6 | Visual explanation, React contracts, agent instructions, and automation |

Change a playbook when you want a different sequence.
Change [compatibility rules](policies/compatibility.md) when the same personal rule should apply across skills.
Edit an original skill when you want to change that creator's method for your own use.
The source mappings and saved originals let the update checker show those edits later.

Pstack's three control commands give way to Son's setup and mode.
Benny's three automations and Matt's 11 in-progress or miscellaneous skills remain inactive.
All 112 originals remain in the snapshots and [catalog](docs/catalog.md).
The [creator analysis](docs/creator-analysis.md) and [routing decisions](docs/decisions.md) explain the selection.

Some originals need tools outside this stack.
Pstack's `deslop`, `control-cli`, and `control-ui` are not bundled, and `no-comments` needs Comment Sicko.
Matt's tracker workflows need a real project configuration through [`setup-matt-pocock-skills`](skills/setup-matt-pocock-skills/SKILL.md).
Building this stack does not install those dependencies.

## Work on this repository

Requires Python 3.9 or newer and Git.
The repository tooling uses Python's standard library.

```bash
python3 scripts/stack.py validate
python3 -m unittest discover -s tests -v
python3 scripts/stack.py build --harness codex
```

Use `--harness claude` or `--harness cursor` for the other builds.
Outputs go under `.build/`, with complete skill folders and a native agent definition.
Setup and update commands locate this checkout through the generated `SON-RUNTIME.json`; rebuild if you move the repository.

[Verification records](reviews/README.md) show what has been checked.
Build and temporary-install checks passed, while fresh-session discovery and real-task quality still need the [pilot](docs/pilot.md) after installation.

<details>
<summary>Repository layout</summary>

```text
skills/                 Creator skills and the three Son commands
agents/                 Son-agent instructions
policies/               Shared compatibility rules
stack.json              Source mappings and imported file baselines
catalog.json            Generated inventory of all original skills
sources.lock.json       Accepted commits and file hashes
upstream/               Preserved creator snapshots
scripts/                Setup, build, validation, install, and diff tools
.local/                 Local model choices, ignored by Git
.build/                 Built skills and agents, ignored by Git
reviews/                Validation evidence and update reports
```

</details>

## License

Creator material retains its MIT licenses and [attribution](THIRD_PARTY_NOTICES.md).
The license for Son's original tooling remains undecided while this repository is local.

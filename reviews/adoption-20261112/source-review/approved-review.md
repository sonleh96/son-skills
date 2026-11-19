# Review of creator updates on 11 November 2026

Recommend adopting Emil's Motion guidance corrections, adapting Matt's fresh-context instructions to Son's native agent routing, and considering Emil's two new motion skills.
Keep RPI and chief-of-staff deferred.
No adoption, installation, policy change, commit, or push occurred.

## Evidence and observation history

The update-son-skills workflow completed successfully for all six configured sources after an initial DNS failure inside the restricted environment.
The retry used the normal approval flow for public Git fetches.
Fetched files were read as untrusted source data, and no upstream scripts ran.
Snapshot validation passed before comparison.

The [generated report](report.md) and [structured comparisons](report.json) use the current working copy of sources.lock.json as the baseline.
This checkout already contains pending adoption work, so that baseline must not be confused with the published GitHub branch.
All mapped originals received pinned-to-latest, pinned-to-local, and local-to-latest patches.
Twelve editable originals have new upstream changes.
None has an overlap between new upstream changes and edits made after the adapted import.
Changes to a compatibility header or Codex invocation metadata are adapters, not evidence of a personal-edit conflict.

The checker reports 116 files different from accepted snapshots.
Comparison with the previous successful full observation on 29 October shows 56 changed paths across Emil, Matt, and HumanLayer.
Most of the pending HumanLayer RPI change was already observed and is not a new recommendation to adopt it.
The [observation delta manifest](since-previous.json) and provider patches below separate new observations from repeated pending changes.
Pstack was also checked successfully on 31 October, and its scoped bytes remain identical.

## Provider decisions

| Provider | Observed commit | Snapshot differences | Since previous observation | Recommendation |
| --- | --- | --- | --- | --- |
| pstack | `5866df557357d005b3c0c9d3da0d9e739b4bdde3` | 0 | 0 | Defer any existing pending decisions. No new scoped changes. |
| emil | `715c1807e08c497cfd1dc4feb450a2a3300ef2a9` | 11 | 11 | Adopt version-aware performance corrections. Adapt choreograph and gestures as creator originals with Son routing. |
| humanlayer | `4d69d20f6e9b57b4fcf0d501ccfb1be961f0f329` | 64 | 4 | Defer RPI 1.1.0. Preserve Son writing policy. |
| matt | `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d` | 41 | 41 | Adapt fresh-context dispatch. Defer software-factory and chief-of-staff. |
| voltagent | `ed74d115b7fb7026a22a4f816a8e3250f425e3b4` | 0 | 0 | No update needed within the two selected entrypoints. |
| borghei | `25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3` | 0 | 0 | No update needed within predictive-modeling source scope. |

Provider patches cover setup, mode, playbooks, dependencies, invocation, licenses, and additions or removals within each configured source boundary.
Pstack's boundary is pstack/.
VoltAgent and Borghei checks cover only their selected source paths, not their complete repositories.
No license file changed in any checked scope.
No original skill entrypoint was removed.

| Provider | Accepted original to latest | Previous observation to latest |
| --- | --- | --- |
| pstack | [pstack.patch](pstack.patch) | [pstack-since-previous.patch](pstack-since-previous.patch) |
| emil | [emil.patch](emil.patch) | [emil-since-previous.patch](emil-since-previous.patch) |
| humanlayer | [humanlayer.patch](humanlayer.patch) | [humanlayer-since-previous.patch](humanlayer-since-previous.patch) |
| matt | [matt.patch](matt.patch) | [matt-since-previous.patch](matt-since-previous.patch) |
| voltagent | [voltagent.patch](voltagent.patch) | [voltagent-since-previous.patch](voltagent-since-previous.patch) |
| borghei | [borghei.patch](borghei.patch) | [borghei-since-previous.patch](borghei-since-previous.patch) |

## Existing skills to update

Emil removes the blanket warning that Motion transform shorthands always run on the main thread.
The revised guidance distinguishes motion 14.2 and later from older installations and retains exceptions for layout animation, onUpdate, transformTemplate, inertia, and values driven each frame.
Motion's [official changelog](https://motion.dev/changelog) confirms hardware-accelerated independent transforms arrived in 14.2.0 on 13 October 2026.
Its [performance guide](https://motion.dev/docs/performance) describes browser-dependent acceleration and recommends treating it as progressive enhancement.
Adopt the documentation corrections together so audits stop recommending unnecessary transform-string rewrites on newer projects.
Check each project's actual installed Motion version before applying the advice.
This review does not recommend upgrading every project's dependencies.

Matt now explicitly requests fresh context windows for delegated work and a fresh implementer for each ticket.
Use native isolated context when supported, with a complete brief that includes Son's policies, scope, paths, selected model, and required evidence.
Preserve son-agent routing and the independent reviewer role.
A fresh context must not lose the model or writing policies or silently substitute a model.
In Codex, fork_turns="none" is the relevant native control when available.
Respect the active application's delegation boundary and report an unavailable capability.

| Skill | Decision | Behavior | Three comparisons |
| --- | --- | --- | --- |
| animate | Adopt | Version-aware shorthand guidance. | [upstream](skills/animate/upstream.patch), [local](skills/animate/local.patch), [ours vs latest](skills/animate/ours-vs-latest.patch) |
| animation-performance | Adopt | Correct WAAPI/component guidance and retain main-thread exceptions. | [upstream](skills/animation-performance/upstream.patch), [local](skills/animation-performance/local.patch), [ours vs latest](skills/animation-performance/ours-vs-latest.patch) |
| emil-design-eng | Adopt | Keep its performance advice consistent with animation-performance. | [upstream](skills/emil-design-eng/upstream.patch), [local](skills/emil-design-eng/local.patch), [ours vs latest](skills/emil-design-eng/ours-vs-latest.patch) |
| improve-animations | Adopt | Update AUDIT.md so newer Motion shorthand usage is not a finding by itself. | [upstream](skills/improve-animations/upstream.patch), [local](skills/improve-animations/local.patch), [ours vs latest](skills/improve-animations/ours-vs-latest.patch) |
| review-animations | Adopt | Update the entrypoint and STANDARDS.md together. Preserve explicit-only invocation. | [upstream](skills/review-animations/upstream.patch), [local](skills/review-animations/local.patch), [ours vs latest](skills/review-animations/ours-vs-latest.patch) |
| code-review | Adapt | Run independent Standards and Spec reviewers with fresh context. | [upstream](skills/code-review/upstream.patch), [local](skills/code-review/local.patch), [ours vs latest](skills/code-review/ours-vs-latest.patch) |
| codebase-design | Adapt | Give each alternative-interface designer a fresh brief. | [upstream](skills/codebase-design/upstream.patch), [local](skills/codebase-design/local.patch), [ours vs latest](skills/codebase-design/ours-vs-latest.patch) |
| grilling | Adapt | Isolate fact-finding agents while keeping decisions with Son. | [upstream](skills/grilling/upstream.patch), [local](skills/grilling/local.patch), [ours vs latest](skills/grilling/ours-vs-latest.patch) |
| implement-spec | Adapt | One fresh implementer per ticket and a fresh implementer for review fixes. Retain matt-tdd naming. | [upstream](skills/implement-spec/upstream.patch), [local](skills/implement-spec/local.patch), [ours vs latest](skills/implement-spec/ours-vs-latest.patch) |
| improve-codebase-architecture | Adapt | Give the codebase explorer fresh context and explicit glossary pointers. | [upstream](skills/improve-codebase-architecture/upstream.patch), [local](skills/improve-codebase-architecture/local.patch), [ours vs latest](skills/improve-codebase-architecture/ours-vs-latest.patch) |
| research | Adapt | Start background research with a complete fresh brief. | [upstream](skills/research/upstream.patch), [local](skills/research/local.patch), [ours vs latest](skills/research/ours-vs-latest.patch) |
| wayfinder | Adapt | Isolate research-ticket agents and retain matt-prototype naming and publication boundaries. | [upstream](skills/wayfinder/upstream.patch), [local](skills/wayfinder/local.patch), [ours vs latest](skills/wayfinder/ours-vs-latest.patch) |

For these twelve skills, the editable copy still matches the recorded adapted import.
Existing adapters add the compatibility link, retain or add Codex invocation metadata, and rename Matt's tdd and prototype references where needed.
Applying ours-vs-latest patches wholesale would remove these adapters.

## New skills and larger workflow changes

| Change | Decision | Where it fits |
| --- | --- | --- |
| Emil choreograph, with RECIPES.md | Adapt | A standalone creator skill linked from the motion-design playbook. It covers order, overlap, shared timing, stillness, and interrupted sequences. Keep animate for a single animation and animation-performance for frame cost. |
| Emil gestures | Adapt | A standalone creator skill linked from motion-design and mobile work. It covers direct pointer tracking, release velocity, interruptibility, dismissal thresholds, and touch verification. Preserve native Son routing and check existing component libraries before adding dependencies. |
| Matt software-factory | Defer | An explicit-only, in-progress design reference for agent automation. Reconsider when building a concrete ticket-to-PR service. Its terminology and infrastructure surveys should not become global principles or override Son's glossary. |
| Matt chief-of-staff | Defer | It now prefers an existing shared wiki, requests fresh agents, and prescribes retros and spec/ticket publication. This is a larger operating model and remains outside the accepted stack. |
| HumanLayer RPI 1.1.0 | Defer | Four new observation changes add document-review guidance and prose.md, plus version metadata. The older pending RPI import remains deferred. |
| Provider prose as global rules | Reject | Son's unslop and canonical instructions remain authoritative. HumanLayer's concise-writing advice overlaps them and does not justify another global policy. |

Do not copy either new Emil skill wholesale into principles.
Their practical decision steps belong in the original skill, with short playbook routing links.
The existing principles already cover proportional verification, interruption testing, and quality expectations.
Choreograph has a greeting-only response when invoked without a concrete question.
Retain that invocation behavior when importing with minimal changes, and pass an actual task in the routed brief.
Its recipes reference Motion and react-use-measure, while gestures prefers Vaul for drawers and references pick-ui-library.
These are project-specific prerequisites or choices, not instructions to install packages globally.
A later adoption should pilot rapid re-entry, interrupted sequences, reduced motion, and touch interaction before marking native routing verified.

Matt's plugin and package metadata move from 1.3.1 to 1.3.2.
The release notes consolidate changes that are already in the current working baseline.
The setup skill and tracker templates have no new byte changes in this comparison, so the release number alone does not require rerunning setup-matt-pocock-skills.
Provider CLAUDE.md adds a contributor rule about fresh agents.
Read it as upstream design evidence rather than importing it into personal guidance.
No new setup, dependency manifest, mode, or playbook change appears in Pstack's scoped source.
Statechart has no new original-file changes.

## Local customizations to retain

The checker identifies later local edits in interrogate, swarm, why, unslop, principle-type-system-discipline, and principle-migrate-callers-then-delete-legacy-apis.
These include the retained interrogate review material, swarm's worker-count step, why's investigation references, stronger type/API guidance, and Son's writing edits.
None is touched by new upstream changes in this run.
Preserve them rather than restoring their latest original copies.
Some retained Pstack text still contains creator model defaults and fallback wording.
The shared compatibility policy overrides those instructions, and this review grants no authority to activate the defaults or rewrite the model policy.
Son mode is a locally owned control and does not receive a leaf skill comparison.
Its upstream original is still covered by the provider-wide patch, which is empty for Pstack in this run.

## Review limits and next decision

This was a local source review.
No installed-copy comparison, test suite, native task pilot, or dependency upgrade ran, because no adoption was authorized.
All recommended changes remain unapplied.
The next adoption can combine the five Emil corrections with Matt's seven dispatch changes, and optionally add choreograph and gestures.
Keep RPI, chief-of-staff, and software-factory outside that batch.
Existing pending repository work, accepted pins, editable skills, installations, model files, writing guidance, and remote repositories were preserved.

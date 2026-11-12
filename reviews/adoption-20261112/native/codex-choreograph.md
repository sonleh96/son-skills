Used `collaboration.spawn_agent` with `agent_type="son-agent"`, requested `gpt-6-astra` at `xhigh`, and `fork_turns="none"`. One fresh child completed the review without nested agents. The tool exposes neither actual child-model identity nor a service-tier selector.

Coordinate the swap as one simultaneous crossfade inside the stationary stage. Keep the existing CSS approach. These are proposed timings:

| Element | Role | Starts | Duration | Motion | Relationship |
|---|---|---|---|---|---|
| Incoming article | Lead | 0ms | 240ms travel, 180ms fade | 28px offset to center, opacity to 1 | Together with exit |
| Outgoing article | Support | 0ms | 160ms travel, 120ms fade | Travel opposite entry, opacity to 0 | Together with entry |
| Number, heading, paragraph | Support and decoration | With article | Inherited | No independent animation | Carried by article |

Next enters from the right and exits left. Back reverses this. An interrupted view should continue from its rendered position and opacity.

Keep these still:

- Stage and outer card, preserving the boundary around the swap.
- Back and Next, keeping controls available throughout.
- Section heading and status, retaining stable reference points while status text updates.
- Article children relative to their parent, with no separate entrance or stagger.

Two source-level risks need attention. Incoming direction depends on the article’s previous transform, and `showView` updates only the previous and next articles, allowing a third article to remain mid-fade during rapid input. See [pilot.css:126](/Users/sonle/Documents/work/son-skills/reviews/adoption-20261112/pilot/pilot.css:126) and [pilot.js:64](/Users/sonle/Documents/work/son-skills/reviews/adoption-20261112/pilot/pilot.js:64). Retarget the current pair and retire obsolete outgoing views.

Rapid-interruption checks:

- **Next, Next**, 40 to 80ms apart. Latest selection wins without a third fading view.
- **Next, Back** mid-fade. Reversal continues without resetting position or opacity.
- **Back immediately after load**, plus both wrap directions. Entry follows the requested direction.
- **Keyboard activation** during transitions. Focus stays on the control; exactly one article remains active and exposed through `aria-hidden="false"`.
- **Reduced motion mid-swap**, using both settings. Travel disappears and selection remains correct. The manual toggle uses 1ms durations; the system preference retains the view’s opacity duration. See [pilot.css:253](/Users/sonle/Documents/work/son-skills/reviews/adoption-20261112/pilot/pilot.css:253).

For the separate Motion 14.2 question, **a full transform-string rewrite is not mandatory**. Under the supplied exclusions, keep `animate={{ x: 100 }}`. The installed skill places HTML shorthand acceleration at version 14.2 onward; the string recommendation concerns older versions under main-thread load. Browser acceleration remains conditional. See [animation-performance:125](/Users/sonle/.codex/skills/animation-performance/SKILL.md:125).

This was local source reading only. No changes, installations, external access, or browser checks occurred. A later recording should scrub the first 120ms after the second click and the reversal frame to assess competing text, discontinuities, and whether the crossfade reads as one object. Frame cost remains unmeasured.



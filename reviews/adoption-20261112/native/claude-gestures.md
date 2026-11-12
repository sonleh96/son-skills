The goal, in my words: judge whether the pilot fixture's drag tile does what the `gestures` skill demands for the three behaviors you named, from code alone, and say what a production version would still need. No change ships from this task.

## Routing and capability report

- Route taken: I ran as `son-agent` and executed `gestures` directly, with no redispatch and no nested agent, per the motion routing contract.
- Reads completed: `son-mode/SKILL.md`, `SON-COMPATIBILITY.md`, `unslop-cc`, `references/principles.md`, `references/playbooks.md`, `references/motion-routing.md`, the `motion-design` playbook, `principle-prove-it-works`, and all four fixture files.
- Model: the environment reports `claude-fable-5-1`. I cannot observe my own effort setting from inside the agent, so "high" is the parent's claim, not something I verified.
- Model configuration: `SON-RUNTIME.json` points at `/Users/sonle/Documents/work/son-skills/.local/models.claude.json`, which does not exist. Setup has not run, so I inherited the session model with no role overrides, as Son mode step 2 prescribes.
- Nothing was served, rendered, or recorded. Every finding below is read from the source. I make no claim about smoothness, frame timing, or device feel.

## What the fixture gets right

Files: `/Users/sonle/Documents/work/son-skills/reviews/adoption-20261112/pilot/pilot.js` and `pilot.css`.

Direct tracking.
- `pointerdown` adds `is-dragging`, and `.drag-card.is-dragging { transition: none }` (css 225-228) beats the base 220ms transition on specificity, so every `pointermove` write lands without easing. The reduced-motion rules only override `transition-duration`, and `transition: none` already set `transition-property: none`, so tracking stays 1:1 in reduced mode too.
- Position comes from `startOffset + clientX - startX` (js 164), not from accumulated deltas, so a dropped move event cannot leave the tile behind the finger.
- `setPointerCapture` (js 155) keeps moves arriving when the pointer leaves the tile, and the `activePointer` guard (js 139, 162, 173) rejects a second pointer.
- No framework state per move; the tile is the only element written, and the written property only feeds `transform`, which is composite-only.
- `touch-action: none` on the tile (css 219) keeps the browser from stealing the gesture.

Bounded travel.
- `dragBounds` (js 118-123) derives the limit from live stage and card rects, so it is correct for the centered-grid layout at any width, and `clampDrag` is applied on every move, on keyboard steps, on catch, and on resize. The stage's `overflow: hidden` is a second fence.
- README checks 6 and 7 (narrow viewport, resize while offset) are implemented by `constrainDrag` on `resize` (js 203, 236).

Catch during release.
- This is the strongest part. `readRenderedX` (js 101-109) reads `getComputedStyle(...).transform`, which during a running CSS transition returns the interpolated value, and parses both `matrix` and `matrix3d`. `startDrag` then writes that value back and disables the transition, so the finger takes over from where the tile is drawn. That is the real rendered value, not a cached one, which is the right reading under prove-it-works.
- `settleToken` (js 95, 141, 184, 191) invalidates the pending settle timer on catch, so a stale timeout cannot flip the phase to idle mid-track.
- Release uses a CSS transition, never `@keyframes`, so it satisfies the skill's interruptibility rule.

## Defects found in the code

1. Fling direction ignores velocity when it is fast but the tile is not yet far (js 182-183). `direction = Math.sign(releaseX || velocity)` takes the sign from position whenever position is nonzero. Scenario at a 760px layout (stage about 710px, `bounds.max` about 279, `far` threshold about 153): drag to +100, flick left faster than 0.8 px/ms, release at +60. `fast` is true, `far` is false, direction is +1, target is +279. The tile flies right, against the flick. Fix: when `fast`, take direction from `velocity`; otherwise from `releaseX`.

2. Stale velocity after a pause (js 161-170, 178). `velocity` is only updated by `pointermove` and only reset by `startDrag`. Drag fast to +100, hold the pointer still for a second, then lift. No move events fire while stationary, so `velocity` still holds the earlier value, `fast` is true, and the tile flings to the side although the finger was stationary at release. Fix: at release, compare `performance.now() - previousTime` and treat velocity as zero past a short window (around 50 to 100ms), or keep a small ring buffer of samples.

3. Reduced motion changes the outcome, not just the motion (js 183). Under reduced motion the target is forced to 0, so a fast or far release lands at center instead of the side. The skill says tracking stays and the fling and bounce reduce; the landing state should remain. For a real dismissal gesture this would mean the sheet never dismisses under reduced motion.

4. Telemetry phase can stick at `release` (js 190-196). The settle timer requires `Math.abs(currentX - target) < 1`. Release toward the right bound, then shrink the window within 240ms: `constrainDrag` moves `currentX` to the new bound, the check fails, and `data-pilot-phase` stays `release` until the next interaction. Reset (js 205-212) also does not bump `settleToken`, so a release timer can overwrite the "Idle." status after Reset.

## Deviations from the gestures skill that matter for production

- Release is a fixed 220ms ease-out curve, not a spring seeded by velocity (css 222, js 185). Velocity is measured but only used as a boolean. Every release lands at the same pace whether it travels 5px or 250px. The skill's spring requirement is the main gap.
- Edges hard-clamp instead of rubber-banding (js 125-128). The skill asks for resistance past the boundary. The README's "stay within the stage" check is met, but the feel the skill describes is not.
- Position is written through a custom property on the tile (js 113, css 221). The property is set on the dragged element, not a parent, so the recalc is bounded to the tile and its two text children. Still, the skill's rule is to write `transform` directly, and the custom property would become the Vaul-style regression the moment the tile grows content.
- `syncTelemetry` runs on every `pointermove` (js 115, 35-49) and rewrites six data attributes on the stage, including a JSON string. For a pilot that is fine. It is per-move DOM churn a production build should not carry, and a code-grounded cost only; I have not shown it drops a frame.
- Release settle is a timer, not `transitionend`, so `data-pilot-phase = idle` is a schedule, not a rendered fact. During `release`, `data-pilot-x` reports the destination (js 185), not where the tile is drawn. Anyone using the DOM telemetry to verify tracking should pair it with `getComputedStyle`.
- Smaller items: `pointerdown` does not check `button` or `isPrimary`, so a right click starts a drag; `pointercancel` is treated as a normal release with the measured velocity rather than a snap back; `button:hover` (css 74) is not gated by `@media (hover: hover)`; buttons compute to roughly 40px tall against the 44px target; the tile has `role="button"` with no Enter or Space handling; stage width changes that are not window resizes (font load, layout shifts) are not caught, where a `ResizeObserver` on the stage would be.

## Verification limits

- No rendered check happened. The skill's real-device requirement stands: desktop pointer events can confirm event flow and the catch logic, and even that I did not run. Touch latency, hit-target feel, 60 versus 120Hz settle, and platform scrolling with `touch-action: none` on a horizontal drag all remain unverified.
- The two release bugs above are reasoned from code paths and should be reproduced in a browser before fixing, per the bug-fix rule in Son's instructions.
- Out of scope and not reviewed: the view-swap section.

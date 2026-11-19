Nothing further is needed; every file is read. Here is the choreography for the pilot's view swap, grounded in the fixture.

## Routing and limits

- Route: executed `choreograph` directly inside the native `son-agent` fork, no redispatch, no nested agents, no edits, no browser or server run.
- Model: this agent runs as Fable 5.1 (`claude-fable-5-1`). I cannot observe the effort setting from inside the agent; the parent states high.
- Role config: `SON-RUNTIME.json` points at `/Users/sonle/Documents/work/son-skills/.local/models.claude.json`, which does not exist. No role overrides are configured, so the agent inherits the session model.
- Evidence limit: everything below is code-grounded. No frame, duration, or visual claim has been observed on a recording.

## Part 1: timeline (Next, view 1 to view 2)

| Element | Role | Starts | Duration | Motion | Relationship |
| --- | --- | --- | --- | --- | --- |
| Entering view `.view.is-active` (pilot.css:140-144, pilot.js:71-74) | Lead | 0ms | transform 240ms, opacity 180ms | fade in, 28px slide from the right to rest | - |
| Leaving view `.view.is-leaving-left` (pilot.css:146-148, pilot.js:69-70) | Support | 0ms | transform 240ms, opacity 180ms | fade out, 28px slide left | Together with the lead (crossfade) |
| View number, h3, p (index.html:33-35) | Carry | - | - | ride inside the view | Carry |
| `.view-stage` (pilot.css:118-124) | Static | - | - | fixed min-height, overflow hidden | - |
| Back/Next buttons, `#view-status` (pilot.js:76) | Static | - | - | status text swaps synchronously | - |

Both views share one easing family (ease-out: `cubic-bezier(0.22, 1, 0.36, 1)` and `ease-out`), start on the same click, and finish by 240ms, inside the product budget. No stagger on a keyboard-reachable control. The relationship is right: this is a crossfade, not a queue, and I would not add anything to it.

## Part 2: what stays still, and why

- The stage: fixed box, absolute children (pilot.css:118-135), so the swap reads as one object and never hits the two-dimension resize case that would force `wait`.
- The view's children: one entrance per container; the article carries its number, heading, and paragraph.
- The buttons: the user is already reaching for Next again; nothing may delay them (hard rule 4).
- The status line: it is a readout of state, so it flips with the state.
- The drag section: different event, no shared beat.

## Defect: the entry side depends on history, not direction

`showView` sets the leaving side by direction (pilot.js:70) but never sets where the entering view starts. A hidden view rests wherever its last class left it: base `+28px` if it never left (pilot.css:135), `-28px` if it last left on Next, `+28px` if it last left on Back. CSS transitions start from the current computed value, so:

- Next, Next, Next (wrap 3 to 1): view 1 is parked at `-28px`, so it enters from the left while view 3 leaves left. Forward motion reads as backward.
- Back from view 1 to view 3 on first use: view 3 is at base `+28px`, so both views slide right together instead of passing each other.
- Simple Next then Back ping-pong is correct only by accident.

Fix shape (not applied, read-only task): before adding `is-active`, park the entering view on the side it should enter from with transitions suppressed, flush, then animate. Guard it with "only park when the view is at rest (computed opacity 0)", otherwise a mid-flight interruption would snap the view to the edge instead of retargeting from where it is.

## Interruption checks (from code)

1. Next then Back within 240ms: roles swap, both transitions retarget from computed values, nothing stacks. Expected pass; confirm on a recording.
2. Next, Next within 240ms: three views in flight. The oldest keeps exiting with `pointer-events: none` and `aria-hidden="true"` set synchronously (pilot.css:137, pilot.js:73), so no stale view is interactive. Passes the README check 1 requirement.
3. Wrap-around or Back after a cold start: the direction defect above.
4. Reduced-motion toggle mid-flight: `transition-duration: 1ms` and `transform: none` retarget the in-flight transition to a cut. Fine.
5. Two reduced-motion paths disagree: the toggle (pilot.css:259-262) cuts opacity to 1ms, while the system media query (pilot.css:264-269) removes transform only and keeps the 180ms opacity fade. The skill's preference is the media-query behavior (drop movement, keep opacity); the toggle should match it.

Unrelated note: `#view-stage` and `#view-status` both carry `aria-live="polite"` (index.html:25, 31), so each swap may announce twice.

## Part 3: feel check

Scrub these moments on a recording; code cannot settle them:

- About 100ms into Next: both views near half opacity in the same box. Does it read as one object sliding through, or as two paragraphs smeared over each other? If smeared, shorten the leaving view's opacity to about 120ms so the exit is simpler than the entry.
- Next, Next within 150ms: three texts overlapping. Decide whether that is acceptable for a control pressed this often, or whether the middle view should be cut rather than faded.
- Back from view 1 to view 3 versus Back from view 2 to view 1: the first has both views moving right, the second has them passing. The difference is the defect made visible.

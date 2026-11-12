# Motion adoption pilot

This dependency-free fixture gives the motion skills a small interface to inspect and exercise.

## Run it

Serve this directory with any local static server.

For example, run `python3 -m http.server 8765` from this directory and open `http://127.0.0.1:8765/`.

The page exposes `window.__motionPilot` for repeatable browser inspection.
Its `events` array records view changes, drag phases, catches, releases, and motion-mode changes.
Its `state()` method returns the current view, drag position, drag phase, catch count, and reduced-motion state.
The drag stage also exposes `data-pilot-phase`, `data-pilot-x`, `data-pilot-catches`, `data-pilot-reduced-motion`, `data-pilot-event-timestamps`, and `data-pilot-events` for browser surfaces limited to DOM inspection.

## Checks

1. Press Next and Back several times in quick succession.
   The latest choice should win without a stale view remaining interactive.
2. Drag the tile a short distance and release it.
   It should track the pointer directly while held and settle quickly after release.
3. Release the tile toward a side, then press it again before it settles.
   The tile should start tracking from its rendered position instead of jumping.
4. Turn on reduced motion and repeat the view and drag checks.
   The state change should remain visible, while travel and decorative motion collapse.
5. Use keyboard focus on the buttons and tile.
   The controls should remain reachable and visible.
6. Resize to a narrow viewport and press ArrowRight repeatedly.
   The tile should stay within the visible drag stage.
7. Resize while the tile is offset.
   The tile should clamp to the new stage and card geometry.

## Limits

This pilot does not prove performance on a real phone or tablet.
Desktop pointer events can exercise event flow and interruption, but they do not represent touch latency, hit-target feel, device refresh rate, or platform scrolling behavior.
The system reduced-motion media query should be checked with browser emulation and with a real device setting when the task reaches native verification.

No package, dependency, or global setting is required by this fixture.

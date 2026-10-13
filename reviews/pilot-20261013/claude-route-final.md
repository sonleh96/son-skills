Diagnosis complete. Read-only, nothing started or edited.

**Routing.** Primary playbook: `motion-design`, which sends frame-cost questions straight to `animation-performance`. Skipped `find-animation-opportunities`, `animate`, and `review-animations` because the task excludes new motion and design choice. Principles applied: prove-it-works and fix-root-causes, so each finding below is a code-grounded risk, not an observed dropped frame. No model-role overrides exist (`.local/models.claude.json` is absent), so the session model was used and no delegation occurred.

**Finding 1: `width` is in the transition.** `index.html:421-424` transitions both `transform` and `width` on the highlight pill. Width is a layout property, so each of the ~15 frames re-lays-out and repaints the pill. The pill is absolutely positioned with no children, which bounds the layout cost, but it sits inside a parent with `backdrop-filter: blur(12px) saturate(1.4)` at `index.html:395-396`. Every repaint of the pill region can force the backdrop blur to recompute. Hypothesis: paint cost dominates, not layout.

**Finding 2: the slide starts while the main thread is busiest.** `setActive` at `importer.js:1173-1186` calls `moveHighlight()` then `mount()`, which clears the stage and rebuilds the whole variant via `innerHTML` on the next frame (`importer.js:1168-1170`). The `transform` half can run on the compositor, but the `width` half needs the main thread every frame, exactly when a full-page parse and layout is running.

**Remaining verification.** A DevTools Performance recording of one picker click, checking for Layout and Paint events inside the 250ms window and long tasks from `mount`. Repeat on a mid-range phone. Confirm visually that a `scale()` swap keeps the pill shape before adopting it.

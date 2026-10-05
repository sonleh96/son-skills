# Motion defaults and checks

Adapted from Emil Kowalski's `animate`, `emil-design-eng`, `mobile-native`, and `review-animations` at the commit recorded in `sources.lock.json`.
These are design defaults to test in context, not universal performance claims.

## Decide whether to animate

| Situation | Default |
| --- | --- |
| Repeated keyboard actions or actions used hundreds of times daily | Immediate response |
| Frequent navigation or hover | Little or no motion |
| Occasional modal, drawer, or toast | Brief motion with a clear purpose |
| Rare onboarding or explanation | More room for expressive motion |

Name the purpose as feedback, state indication, spatial continuity, or explanation.
Keep important data steady while the user reads or acts on it.

## Starting values

Reuse the product's tokens when they already express the same intent.

| Interaction | Starting duration |
| --- | --- |
| Button press | 100 to 160 ms |
| Tooltip or small popover | 125 to 200 ms |
| Dropdown or select | 150 to 250 ms |
| Modal or drawer | Start below 300 ms; longer motion needs an interaction-specific reason |
| Decorative stagger | 30 to 80 ms between items, without delaying interaction |

| Motion | Starting curve |
| --- | --- |
| Enter or exit | `cubic-bezier(0.23, 1, 0.32, 1)` |
| Move or morph on screen | `cubic-bezier(0.77, 0, 0.175, 1)` |
| Drawer | `cubic-bezier(0.32, 0.72, 0, 1)` |
| Hover or color | `ease` |
| Constant progress | `linear` |

For a gesture that carries velocity, start with an existing spring token.
Emil gives `duration: 0.5, bounce: 0.2` as one motion-library starting point.
Verify that those properties mean the same thing in the installed library version.
Use subtle bounce only when the interaction benefits from it.

## Review checklist

- Prefer transform and opacity; profile layout, paint, clip-path, blur, and other exceptions.
- Start a scaled entrance near its final size, typically 0.9 to 0.97, rather than zero.
- Anchor popover scale to its trigger; centered modals have a different origin.
- Name transition properties instead of using `transition: all`.
- Use retargetable transitions or springs for repeated triggers and reversals.
- Preserve velocity through gesture interruption and handle cancellation and multiple pointers.
- Gate hover effects with actual hover and pointer capabilities.
- Honor reduced motion, including disabling motion when that is what the user or platform setting requires.
- Verify exit behavior, focus, and usability during motion.
- Inspect at normal speed and slowed playback, then test the relevant touch interaction on a real device when available.

The upstream duration table allows some drawers up to 500 ms while its general rule favors UI motion below 300 ms.
This stack uses the shorter range by default and requires a reason and rendered evidence for an exception.
Do not treat all CSS animation as compositor-only or all library shorthand as slow without checking the installed version and observing a trace.

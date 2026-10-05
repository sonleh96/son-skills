---
name: son-ui-stress
description: "Stress-test UI with realistic extreme data and capture visual failures. Use for long names, missing fields, empty collections, localized labels, large counts, and narrow layouts."
---

Read `references/working-agreements.md` before following this workflow.
Consult `references/sources.md` only when detailed creator examples or specialist guidance are needed.

# Try the worst realistic data

1. Map each rendered field to its source, type, validation limit, and optionality.
   Include labels, counts, dates, badges, images, and list length.
2. Derive plausible edge cases from real contracts.
   Use long names and email shapes, one-character names, zero and one item, large counts, missing optional media, Vietnamese and other non-Latin text, and longer translated labels.
   Use actual schema limits when available and report unbounded values.
   Do not widen production types to fit fabricated impossible data.
3. Feed the fixture through the component's actual data boundary.
   Use an isolated dev route or existing fixture system with a Demo / Worst case / Empty / One selector.
   Keep the control out of production and persist the choice in the URL when useful.
4. Render the real container width, a narrow viewport, and the widest supported layout.
   Check wrapping, clipping, spacing, pluralization, focus, image fallback, scroll behavior, and control reachability.
   Save the data, viewport, repeatable steps, and screenshots.
5. Report each failure and a proposed correction before fixing it.
   Distinguish a missing implementation from a product decision such as wrap versus truncate.
   Apply fixes only if requested.

A type error in a fixture is evidence to inspect the contract, not a reason to add optional props.
Keep legitimate missing-data states reachable through live behavior.

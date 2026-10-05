---
name: son-ui
description: "Build or polish a web interface using existing design tokens, accessible components, mobile behavior, and rendered verification. Use for layout, interaction details, touch behavior, or Sonner integration."
---

Read `references/working-agreements.md` before following this workflow.
Consult `references/sources.md` only when detailed creator examples or specialist guidance are needed.

# Build an interface that holds up in use

1. Read the product's existing components, tokens, breakpoints, and interaction patterns.
   Establish the actual task, user frequency, content, and supported devices.
   Extend the design system rather than installing a parallel one.
2. Get layout, typography, hierarchy, focus order, and empty and error states right before adding decoration.
   Prefer semantic controls with keyboard behavior and visible focus.
   Check content at its real container width.
3. Use animation only when it clarifies feedback, state, or spatial relationships.
   Frequent keyboard interactions should respond immediately.
   Keep motion interruptible and honor reduced-motion settings.
   Use the motion reference for exact default values when needed.
4. For mobile web, use capability queries for hover and pointer behavior.
   Use viewport units appropriate to stable content or a resizing app shell, safe-area insets, and deliberate overscroll behavior.
   Keep text selectable and browser zoom available.
   Do not infer input capabilities from screen width or user-agent strings.
5. For Sonner, inspect the installed version and existing Toaster placement first.
   Use stable toast IDs for updates and check loading, promise, dismissal, theme, portal stacking, and route lifetime.
   Verify a missing toast before adding a second Toaster.
6. Render the result and exercise keyboard, touch-equivalent actions, narrow layouts, long content, and reduced motion.
   Capture evidence and say which gesture or device checks still need physical hardware.

Do not install a library merely because a source recommends it.
Verify current official library documentation when version-sensitive behavior matters.
An audit request produces findings; it does not authorize a redesign.

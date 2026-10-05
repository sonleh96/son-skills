---
name: setup-son-skills
description: Detect the active application's available models, choose a reasoning budget and models by role, and save Son's skill configuration. Use for initial setup or changing the budget or role assignments.
---

# Set up Son's skills

Read `SON-COMPATIBILITY.md` and the adjacent `SON-RUNTIME.json` when installed.
Use the repository location in that file for the commands below.
This setup changes Son's stack configuration, not the application's parent-chat model or the canonical model policy.

1. Detect the active application's available models and their supported reasoning controls from its current native tools or documented model listing.
   Do not use another application's catalog, a provider's public model list, or a stale local cache as proof of access.
   If the session exposes no listing, ask for the user's available choices.
2. Read the existing `.local/models.<harness>.json`, if present, and `/Users/sonle/model-policy.md`, if present.
   Preserve previous role choices when they are still available.
   Explain any conflict with a policy default before recording an explicit override.
3. Ask for a budget, showing the current choice when one exists.

   | Budget | Target reasoning |
   | --- | --- |
   | Small | Medium |
   | Medium | High |
   | Large | Extra high |
   | Unlimited | Max, not a spending cap |

   These are reasoning presets, not dollar or token limits.
   Use the highest advertised effort at or below the target unless the user explicitly chooses another supported effort.
   Inherited models keep the parent settings.
4. Show the role table for planning, implementation, review, research, prose, and UI.
   Offer only detected models and `inherit-parent`.
   A comparison panel is optional; each entry adds a worker and must be chosen explicitly.
   Let the user accept the table or change specific roles.
5. Save the observed inventory and choices under `.local/`, using the schemas in `references/configuration.md`.
   Run the validator to preview the resolved model and effort table:

   ```bash
   python3 scripts/models.py --inventory .local/inventory.json --choices .local/choices.json --budget large
   ```

   Use the chosen budget, then repeat with `--save` after the user has accepted the table.
   Unsupported model and effort combinations must fail rather than silently selecting another family.
6. Report the saved path and actual choices.
   `son-mode` reads this file on its next task; no global instruction file needs rewriting.
   A model change for the parent conversation still requires the application's native model picker.

If the application cannot set reasoning effort or service tier through its delegation interface, state that limit.
Do not claim that saving a preference changed an unsupported runtime setting.

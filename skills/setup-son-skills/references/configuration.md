# Model configuration

Create the inventory from capabilities actually advertised in the active session.
The following model ID is an example placeholder, not an available model claim.

```json
{
  "harness": "codex",
  "observed_at": "2026-10-05T15:00:00Z",
  "evidence": "Current session native delegation tool model and effort list",
  "models": {
    "example-model": {"efforts": ["medium", "high", "xhigh"]}
  }
}
```

An empty effort list means no configurable effort is advertised.
Keep exact model IDs, including any provider-specific variant ID, as observed.
Do not construct new model slugs by appending an effort.

```json
{
  "roles": {
    "planning": "inherit-parent",
    "implementation": "inherit-parent",
    "review": "inherit-parent",
    "research": "inherit-parent",
    "prose": "inherit-parent",
    "ui": "inherit-parent"
  },
  "panel": []
}
```

A role may instead specify `{"model": "example-model", "effort": "high"}`.
The validator checks that explicit pair against the inventory.
Refresh the inventory and validate again when the active application's model access changes.
The saved config records preferences and evidence, not a guarantee of future availability.

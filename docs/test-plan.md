# Failure modes to verify

These failure modes were listed before writing the tooling tests.
Tests use real temporary Git repositories and filesystem operations, without mocking our own code.

| ID | Failure | Verification |
| --- | --- | --- |
| F1 | A changed accepted snapshot is silently treated as the baseline | Corrupt a snapshot and require validation to fail |
| F2 | Added, removed, renamed, modified, executable, or license files are missed | Change a real local upstream, run the CLI, and inspect the report and patch |
| F3 | Unrelated Cursor monorepo changes create false pstack alerts | Change a file outside a configured source scope and require zero scoped changes |
| F4 | A fetch failure is reported as unchanged or hides other successful checks | Use an unavailable local remote beside a working one and require a partial report plus nonzero exit |
| F5 | Installing the stack overwrites existing work or partially installs before detecting a collision | Pre-create a conflicting skill and require all other destinations to remain absent |
| F6 | Installed skills depend on the source checkout or lose licenses | Install into a temporary destination and check local references, copied rules, licenses, and repeat installation |
| F7 | Repeated checks alert again on the same unaccepted diff or move the accepted baseline | Run twice against the same change and compare observation state and accepted hashes |
| F8 | A malicious or malformed file path escapes its configured source directory | Reject absolute paths, parent traversal, and symlinks outside the snapshot |
| F9 | Skill discovery metadata changes manual invocation into automatic invocation | Flip one explicit-only metadata flag and require validation to fail |

The initial live check also verifies connectivity to all four real upstreams.
Structural checks do not establish that the skills improve real tasks.
The pilot scenarios in `docs/pilot.md` define that next evaluation.

## Original skill and update checks

Listed before adding tests for the original-skill redesign.

| ID | Failure | Verification |
| --- | --- | --- |
| F10 | A local edit disappears from a three-way review or the check overwrites it | Edit the same file locally and upstream, add a support file, and inspect all three patches and unchanged local bytes |
| F11 | An installed copy is mistaken for the editable source or missing copies look current | Compare a separate edited install directory and require its own patch and missing-skill state |
| F12 | Setup invents a model or selects an unsupported reasoning effort | Exercise unavailable choices, inherited settings, and supported effort boundaries |
| F13 | A custom agent points to the build directory after installation or bypasses collision preflight | Install the native agent with a real fixture, check its installed path, then pre-create a conflicting agent |
| F14 | A name collision rewires a creator's dependency to a different creator | Check explicit references, prose preservation, and relative link rewriting against fixed examples |

| F15 | Keeping a personal skill during installation overwrites it or hides an invalid selection | Install with an explicit keep-existing name, verify its bytes survive, and reject unknown names or missing skill entry points |

## F16: skill aliases leak into tracker vocabulary

A prototype ticket can be renamed to matt-prototype when the adapter treats a domain value as a skill reference.
Reproduce this with the real tracker template and wayfinder examples.
The regression check must preserve the literal prototype type while still mapping the explicit prototype skill call and tdd invocation.

## New specialist source checks

| ID | Failure | Verification |
| --- | --- | --- |
| F17 | A scoped upstream source silently expands to the whole repository or misses its explicitly selected license | Run the checker against a fixture with a scope, selected files, and a license outside that scope, then inspect the exact candidate file set |
| F18 | A creator skill whose source entry point is not named `SKILL.md` disappears from the generated catalog, loses its three-way comparison, or folds later frontmatter into its description | Map a fixture source file ending in `.md` with a folded description, generate the catalog, and require the mapped row, description, and local comparison to remain present |
| F19 | A selected source directory misses a new helper or includes an unrelated creator folder | Run the checker after adding one helper under the selected directory and one sibling file, then require only the helper in the candidate and change report |

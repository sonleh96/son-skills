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

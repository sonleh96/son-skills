# Pilot failure modes

- The accepted Pstack snapshot can drift in bytes, modes, symlink targets, or manifest paths.
- The statechart adapter can alter original supporting files or its original body beyond the required entrypoint metadata and routing paragraph.
- Explicit-only metadata can accidentally permit implicit invocation.
- Native routing can redispatch from inside `son-agent` or run directly when delegation is unavailable.
- The installer can mutate the destination before every destination conflict is known.
- The installer can overwrite an existing statechart skill instead of refusing the whole operation.
- A repeat installation can change destination bytes or report a new skill after the first successful installation.
- The correct TLA+ model can falsely pass an early-write counterexample or deadlock before reaching a terminal state.
- The checker can resolve an unpinned Java or TLC executable instead of the reviewed toolchain.
- A model counterexample can be mistaken for an actual installer defect when the real replay proves the guarded behavior.

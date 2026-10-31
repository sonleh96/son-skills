------------------------------ MODULE Installer ------------------------------
EXTENDS Naturals
CONSTANTS EARLY_WRITE, CONFLICT
VARIABLES phase, destinationWrites

vars == <<phase, destinationWrites>>

Init ==
    /\ phase = "start"
    /\ destinationWrites = 0

Preflight ==
    /\ phase = "start"
    /\ ~EARLY_WRITE
    /\ phase' = "preflight"
    /\ UNCHANGED destinationWrites

EarlyWrite ==
    /\ phase = "start"
    /\ EARLY_WRITE
    /\ phase' = "preflight"
    /\ destinationWrites' = 1

Resolve ==
    /\ phase = "preflight"
    /\ phase' = IF CONFLICT THEN "blocked" ELSE "ready"
    /\ UNCHANGED destinationWrites

Write ==
    /\ phase = "ready"
    /\ phase' = "done"
    /\ destinationWrites' = 1

Terminal ==
    /\ phase \in {"done", "blocked"}
    /\ UNCHANGED vars

Next == Preflight \/ EarlyWrite \/ Resolve \/ Write \/ Terminal

Spec == Init /\ [][Next]_vars

TypeOK ==
    /\ phase \in {"start", "preflight", "ready", "done", "blocked"}
    /\ destinationWrites \in 0..1

NoWriteBeforePreflight == phase \in {"start", "preflight"} => destinationWrites = 0

NoPartialWritesOnConflict == CONFLICT /\ phase = "blocked" => destinationWrites = 0

=============================================================================

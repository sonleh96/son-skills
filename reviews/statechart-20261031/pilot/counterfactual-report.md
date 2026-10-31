# Installer

TLC reached 3 states and 3 steps. The chart draws 3 states and 2 arrows.
The chart does not draw 1 steps that stay in one chart state.

## NoWriteBeforePreflight breaks
The shortest path has 1 step:
0. Waiting to check, destination unchanged
1. copy before checking: Checking destinations, destination changed

## NoPartialWritesOnConflict breaks
The shortest path has 2 steps:
0. Waiting to check, destination unchanged
1. copy before checking: Checking destinations, destination changed
2. reject conflicting install: Blocked by conflict, destination changed

## Rules that hold
TypeOK, NoDeadlock

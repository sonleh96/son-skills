---
name: update-son-skills
description: Fetch the latest creator sources and compare them with Son's pinned originals and current adapted skills. Use for an on-demand skill update review, local drift check, or upstream diff. Produce review artifacts before applying any change.
---

# Review updates to Son's skills

Read `SON-COMPATIBILITY.md` and the adjacent `SON-RUNTIME.json` when installed.
Use its repository path rather than the current product repository.

1. Run the read-only update checker from the Son skills repository:

   ```bash
   python3 scripts/upstream.py check
   ```

   Use `--source matt`, `--source pstack`, `--source emil`, or `--source humanlayer` to narrow a requested review.
   To compare a particular installed copy as well, add `--installed-skills /absolute/path/to/skills`.
   Never replace the editable repository source with an installed copy.
2. Open the returned report and inspect all three comparisons:

   - Pinned original to latest original, showing what the creator changed.
   - Pinned original to the current repository skill, showing the minimal adapter and Son's edits.
   - Current repository skill to latest original, showing the remaining differences.

   Optional installed-copy comparisons are reported separately.
   Source ownership in `stack.json` identifies the exact original, including duplicate names.
   Compare HEAD of the tracked source and report its exact commit, not a vague latest-version claim.
3. Separate expected compatibility changes from local edits made since import.
   Inspect files changed both locally and upstream before recommending adoption.
   Those overlaps need review; they are not automatically proven merge conflicts.
4. Summarize changes to behavior, references, invocation policy, dependencies, licenses, and added or removed skills.
   Recommend adopt, adapt, defer, or reject for changes that matter.
   Show incomplete fetches explicitly and retain successful partial results.
5. Return links to the report and patches.
   The plain `/update-son-skills` invocation is a review and does not modify skills, accepted pins, installations, model choices, or global instructions.
   If the user also requests applying selected updates, use the reviewed commit and the procedure in the repository's `docs/update-review.md`, preserving local edits.

Use the same checker for scheduled and on-demand reviews.
Always return the current diff when invoked by the user, even when the scheduled monitor would suppress a repeated notification.

---
name: son-writing
description: "Write or edit concise agent instructions, technical documentation, or decision notes with specific triggers, source references, and completion criteria."
---

Read `references/working-agreements.md` before following this workflow.
Consult `references/sources.md` only when detailed creator examples or specialist guidance are needed.

# Write instructions that change behavior

Apply the installed `unslop` skill as the final editorial pass.
This skill adds document structure; it does not replace Son's canonical prose rules.

1. Identify the reader and the job the document must help them complete.
   Choose a tutorial, task guide, reference, or explanation rather than mixing all four without a reason.
2. Lead with the outcome and give concrete steps in dependency order.
   Ground a term before relying on it.
   Remove filler, repeated rules, unsupported claims, and instructions already enforced by tooling.
3. For agent instructions, specify when the rule applies, what evidence to read, the action, and a checkable completion condition.
   Keep uncommon detail in a clearly linked reference.
   Preserve essential commands and real authority boundaries.
4. Keep shared guidance, repository-specific rules, skill behavior, and tool configuration in their canonical owners.
   Do not rewrite shared instructions into Claude-specific XML by default.
5. Verify paths, commands, examples, and links against the actual environment.
   Preserve generated content and unrelated user edits.
   For a substantial Markdown edit, put each complete sentence on its own line.
6. Read the result aloud in your head and remove inflated language and needless headings.
   Use a table or diagram only when it makes the information easier to compare or understand.

Editing a document is not permission to publish it or change the user's global instructions.

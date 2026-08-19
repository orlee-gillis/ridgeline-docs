# Build log

Every time AI generated code or config in this repo: the prompt, what the model got wrong,
and how I verified work I didn't write. Session 25 distils this into the README's "How I
built this" section.

## CLAUDE.md - written by Claude Code, August 6 2026

**Prompt:** a specification of folder roles, four hard rules, and three conventions, with a
60-line cap and an instruction to write it as direct instructions to the agent.

**What I checked:** read the file before committing.

**Rule test.** Asked Claude Code to edit `ai-workflow/legacy/unused-access-report.md`. It
refused, cited CLAUDE.md's never-edit rule, gave the reason - the folder is kept as evidence
of the "before" state - and offered the published page in `docs/` as the correct target.

The redirect wasn't in CLAUDE.md. The file states which folders are off-limits and what
`docs/` holds; the agent inferred the alternative from that.

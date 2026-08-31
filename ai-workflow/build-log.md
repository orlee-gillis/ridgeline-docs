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

## README - updated by Claude Code, August 31 2026

**Prompt:** revise the README's skills section (count and routing), CI gates section (coverage gap), and repo layout table based on expanded skill suite and gate coverage analysis.

**What I checked:** read GATES.md and GATES-CHANGELOG.md to understand current gate implementation and coverage; listed actual skills in ai-workflow/skills/ directory; verified against CLAUDE.md's statement that new validator skills haven't been through rubric audit; confirmed that reference documentation (API/MCP/LLM) has validators designed as skills but not yet wired into CI gates (deterministic checks only, per CLAUDE.md); reviewed the approval step requirement.

**Changes made:** corrected skills count from "four" to "growing suite"; listed actual skill names and roles; clarified that baseline skills (ridgeline-doc-writer, unused-access-expert) were audited with rubric but new skills haven't been; added coverage gap statement (reference docs get deterministic checks, validators designed but not yet implemented as gates); added approval step as distinct manual control preceding merge; added ai-workflow/skills/ row to repo layout table.

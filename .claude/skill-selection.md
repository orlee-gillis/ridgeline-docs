# Skill selection

Fuller reference for the trigger table in `CLAUDE.md`. Three skills exist under `ai-workflow/skills/`;
this is how to pick between them.

## `ridgeline-doc-auditor`

Audits a finished page. Does not write or rewrite one.

Load it when the user:
- Hands over a page (or points at one) and asks what's wrong with it, whether it's any good, or asks
  for a review/audit/assessment.
- Says something like "review this page," "what's wrong with the report page," "audit these two
  articles," or pastes a page and asks for an opinion with no other framing.
- Is deciding whether a page is ready to ship.

Do not load it for:
- Punctuation, banned words, casing, frontmatter presence, broken links, or heading structure - Vale,
  the CI script, and markdownlint already own these. Re-checking them by hand produces noise.
- Drafting or rewriting. This skill hands approved problems to `ridgeline-doc-writer`; it never
  produces the replacement text itself, because the pass that decides what's wrong shouldn't also
  decide what replaces it.

This is also the skill `audit-report.js` loads as its audit context (see `prompt-patterns.md`,
pattern 3) - the gate script and the interactive skill use the same method and severity framework, so
a finding a human would raise interactively is the same finding the gate raises in CI.

## `ridgeline-doc-writer`

Drafts or rewrites a page.

Load it when the user:
- Asks for a new page to be written, or an existing one rewritten.
- Hands over approved problems from an audit and asks for the fix.

**Frozen** until the Phase F baseline eval is recorded (see `CLAUDE.md` Hard rules). If you're asked
to draft something and this skill is frozen, say so and ask before editing it or working around the
freeze - don't assume the freeze has lifted.

## `unused-access-expert`

Factual knowledge base for the Unused Access feature specifically - not a general skill, and not
loaded on its own for a generic drafting or audit request.

Load it (in addition to whichever of the two skills above applies) when:
- The page or claim under discussion is about Unused Access, and a factual claim needs verifying
  against the knowledge base rather than accepted at face value.
- `ridgeline-doc-auditor` is auditing an Unused Access page - its own instructions say to pair with
  this skill before judging any factual claim, not to judge facts from memory.

## When nothing matches

If the request doesn't clearly match one of these - for example, a structural question about the repo
itself, or something about CI configuration - don't force-load a skill. Answer from the repo's actual
files (`CLAUDE.md`, `GATES.md`, the workflow files) instead of guessing which skill might apply.

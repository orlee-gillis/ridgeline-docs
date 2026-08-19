# Skill selection

Fuller reference for the "Skill triggers" table in `CLAUDE.md`. Three skills exist under
`ai-workflow/skills/`; this is how to pick between them when a request could plausibly match more
than one.

## `ridgeline-doc-auditor`

Audits a finished page. Does not write or rewrite one.

Load it when the user:

- Hands over a page (or points at one) and asks what's wrong with it, whether it's any good, or
  asks for a review/audit/assessment.
- Says something like "review this page," "what's wrong with the report page," "audit these two
  articles," or pastes a page and asks for an opinion with no other framing.
- Is deciding whether a page is ready to ship.

Do not load it for:

- Punctuation, banned words, casing, frontmatter presence, broken links, or heading structure -
  Vale, the CI gates, and markdownlint already own these. Re-checking them by hand produces
  noise, not findings.
- Drafting or rewriting. This skill hands approved problems to `ridgeline-doc-writer`; it never
  produces the replacement text itself, because the pass that decides what's wrong shouldn't also
  decide what replaces it.

This is also the skill `gate_common.py` loads as its audit context for the three CI gates (see
`prompt-patterns.md`, pattern 2) - the gate scripts and the interactive skill use the same
checklist and severity framework, so a finding a human would raise interactively is the same
finding a gate raises in CI.

## `ridgeline-doc-writer`

Drafts or restructures a page - a feature overview, a report deep-dive, a reference page, a
release note, or a glossary entry.

Load it when the user:

- Asks for a new page to be written, or an existing one restructured.
- Hands over approved problems from an audit and asks for the fix.
- Names a feature or pastes raw notes that need to become a page, even without saying "page,"
  "article," or "doc."

**Ambiguity to watch for**: this skill's own description lists "review" and "audit" among its
triggers too, alongside drafting. Don't let that pull a pure review/audit request here instead of
`ridgeline-doc-auditor` - if the user just wants to know what's wrong with a page and hasn't asked
for a rewrite, `ridgeline-doc-auditor` is still the right skill. Route here once the ask becomes
"now fix it" or "write this."

**Frozen** until the Phase F baseline eval is recorded (see `CLAUDE.md` Hard rules). If asked to
draft something and this skill is frozen, say so and ask before editing it or working around the
freeze - don't assume the freeze has lifted.

## `unused-access-expert`

Factual knowledge base for the Unused Access feature specifically - not a general skill, and not
loaded on its own for a generic drafting or audit request.

Load it (in addition to whichever of the two skills above applies) when:

- The page or claim under discussion is about Unused Access, and a factual claim needs verifying
  against the knowledge base rather than accepted at face value.
- `ridgeline-doc-auditor` is auditing an Unused Access page - its own instructions say to pair
  with this skill before judging any factual claim, not to judge facts from memory.
- `ridgeline-doc-writer` is drafting or restructuring an Unused Access page - same reasoning,
  drafting shouldn't invent facts either.

## When nothing matches

If the request doesn't clearly match one of these - for example, a structural question about the
repo itself, or something about CI configuration - don't force-load a skill. Answer from the
repo's actual files (`CLAUDE.md`, `GATES.md`, the workflow files) instead of guessing which skill
might apply.

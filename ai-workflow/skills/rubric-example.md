# Rubric - Worked Example

Shows what a filled-in entry looks like, using a small invented example - not
`ridgeline-doc-writer` or `unused-access-expert`, so it doesn't pre-empt your own independent pass
against the real skills. See `rubric.md` for the full seven dimensions and scoring scale.

---

**Invented skill for this example:** `changelog-writer` - a hypothetical skill that drafts release
changelog entries from merged-PR titles.

### Dimension 2: Findability

**Score: 1 (partial)**

**Reason:** The skill's trigger description says "use this when writing about a release." That
overlaps with a hypothetical sibling skill, `release-notes-writer`, which also claims "release"
language - nothing in either description distinguishes "changelog entry" (terse, one line per PR)
from "release notes" (prose, grouped by theme, written for end users). A person or another skill
reading just the two descriptions could reasonably route a request to either one.

**What would move this to a 2:** Add one clause to each skill's description naming the other and
the boundary - e.g., "terse, PR-title-driven entries; for prose release notes grouped by theme,
see `release-notes-writer`" - the same reciprocal-pairing pattern Dimension 4 asks for, applied to
the trigger line specifically instead of just the body.

**What would move this to a 0:** If the two skills' descriptions were identical, or if there were
no second skill to conflict with but the description was still too vague to predict what "writing
about a release" would and wouldn't catch (e.g., would it fire for a blog post announcing the
release? Unclear.).

---

That's the shape every dimension entry should take: a score, a specific reason grounded in the
actual file (a quote, a missing line, a concrete test), and - where it's not a 2 - what evidence
would change it. A score with no reason attached isn't usable for the Session 26 re-measurement,
because there'd be nothing to check whether the same problem is still there.

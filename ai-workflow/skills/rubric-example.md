# Rubric - Worked Example

What a filled-in row looks like, using a small invented example - not `ridgeline-doc-writer` or
`unused-access-expert`, so it doesn't pre-empt your own independent pass against the real skills.
See `rubric.md` for the full seven dimensions and scoring scale.

**Invented skill for this example:** `changelog-writer` - a hypothetical skill that drafts release
changelog entries from merged-PR titles.

| # | Dimension | Score | Reason | What would change the score |
| --- | --- | --- | --- | --- |
| 2 | Findability | **1 — Partial** | Trigger description says "use this when writing about a release." A hypothetical similar skill, `release-notes-writer`, also claims "release" language - nothing in either description distinguishes "changelog entry" (terse, one line per PR) from "release notes" (prose, grouped by theme). A person or another skill reading just the two descriptions could reasonably route a request to either one. | **To a 2:** add one clause to each description naming the other and the boundary - e.g., "terse, PR-title-driven entries; for prose release notes grouped by theme, see `release-notes-writer`" - the reciprocal-pairing pattern from Dimension 4, applied to the trigger line. **To a 0:** if the two descriptions were identical, or too vague to predict what "writing about a release" would and wouldn't catch even without a second skill to conflict with. |

That's the shape every row should take: a score, a specific reason grounded in the actual file (a
quote, a missing line, a concrete test), and - where it's not a 2 - what evidence would change it.
A score with no reason attached isn't usable for the Session 26 re-measurement, because there'd be
nothing to check whether the same problem is still there.

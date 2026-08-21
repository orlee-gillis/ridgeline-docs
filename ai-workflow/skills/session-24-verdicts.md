# Session 24 - Rubric Verdicts

Scored independently per `rubric.md`'s "you first, then together" process - your pass happened
first, without seeing Claude's, then Claude scored separately. Disagreements are written up as
ADRs in `ai-workflow/decisions/session-24-rubric-disagreements.md`, linked inline below.

## `ridgeline-doc-writer` - your total 6/14, Claude's total 7/14

| # | Dimension | Your score | Your reason | Claude's score | Claude's note |
| --- | --- | --- | --- | --- | --- |
| 1 | Source hierarchy | 1 | Present (lines 73-76) but not labeled "Source hierarchy" like `unused-access-expert` - easy to miss on a skim | 2 | Content is explicit and ranked, which is what the rubric asks for; the labeling gap is real but belongs under a different concern - see [ADR #1](../decisions/session-24-rubric-disagreements.md#1) |
| 2 | Findability | 0 | The skill's own description includes "review" and "audit" language that also matches `doc-auditor`'s entire job; `CLAUDE.md` needs a separate table to disambiguate | 0 | Agree |
| 3 | Progressive disclosure | 1 | Does the job, but headings should be labeled better and sections should be more bulleted | 1 | Agree |
| 4 | Boundaries and routing | 1 | Points at other skills, but the pointer isn't reciprocal - the skills it refers to don't point back | 1 | Same score, different reason: the `unused-access-expert` pairing *is* reciprocal; the real gap is `doc-auditor`, unacknowledged in either skill file |
| 5 | Controlled vocabulary | 1 | Bundled glossary copy currently matches `unused-access-expert`'s, but nothing enforces that - no canonical file exists | 1 | Agree |
| 6 | Grounding discipline | 2 | - | 2 | Agree |
| 7 | Output correctness | 0 | Current routing genres don't map to the real `template:` values the gates check for - a fresh draft wouldn't carry a `template:` tag at all | 0 | Agree |

## `unused-access-expert` - your total 8/14, Claude's total 7/12 (Dimension 7 excluded)

| # | Dimension | Your score | Your reason | Claude's score | Claude's note |
| --- | --- | --- | --- | --- | --- |
| 1 | Source hierarchy | 2 | Dedicated heading with a 5-row ranked table (lines 29-37) - the concrete example of a 2 | 2 | Agree |
| 2 | Findability | 0 | Same overlap as `doc-writer`'s Dimension 2 | 0 | Agree |
| 3 | Progressive disclosure | 0 | "High-risk sections" restates facts directly in the body instead of only citing the section - body acting as source of truth, not just a summary | 1 | Real, but a small deliberate repeat of only the 3 highest-stakes facts, not the whole knowledge base - see [ADR #2](../decisions/session-24-rubric-disagreements.md#2) |
| 4 | Boundaries and routing | 1 | Points to `doc-writer`, but the pointer isn't reciprocal | 1 | Agree (same `doc-auditor` gap noted above applies symmetrically) |
| 5 | Controlled vocabulary | 1 | Same shared fact as `doc-writer` | 1 | Agree |
| 6 | Grounding discipline | 2 | - | 2 | Agree |
| 7 | Output correctness | 2 | The Source hierarchy table's rigor supports factually correct output when paired with `doc-writer`, even though this skill never produces a page alone | N/A | The rubric's own wording presupposes the skill produces a page - this one structurally never does alone, so the dimension doesn't apply; scoring it anyway makes the two skills' totals look comparable when they aren't - see [ADR #3](../decisions/session-24-rubric-disagreements.md#3) |

## Standalone findings (not rubric scores, bugs to fix during revision) - all fixed

- ~~`unused-access-expert/SKILL.md` has a stray line above its real frontmatter~~ - removed.
- ~~`ridgeline-doc-writer`'s "Route first: pick the genre" section still uses five old genres that
  don't map to the three real `template:` genres~~ - rewritten to use `parent-report`,
  `child-report`, `workflow-methodology` (with `reference page`, `release note`, `glossary entry`
  kept as non-gate-checked options). New templates `child-report.md` and
  `workflow-methodology.md` added, grounded in the real pages' structure; `report-page.md` renamed
  to `parent-report.md`.

## Revisions made (this session)

- `ridgeline-doc-writer`: routing genres fixed (Dimension 7), frontmatter description no longer
  claims "review"/"audit" as its own triggers (Dimension 2), added `## Source hierarchy` heading
  (Dimension 1 disagreement resolution).
- `unused-access-expert`: stray frontmatter line removed, "High-risk sections" de-duplicated to
  citations only (Dimension 3 disagreement resolution).
- `.claude/skill-selection.md` and `docs/meta/skill-architecture.md` updated to match the real
  genre names.

Re-scoring against the revised skills happens in Session 28 (The Defense, deferred to the very
end), per `rubric.md`'s own instructions.

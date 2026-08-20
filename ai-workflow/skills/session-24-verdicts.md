# Session 24 - Rubric Verdicts

Your scores first, independently, per `rubric.md`'s "you first, then together" process. Claude's
pass and any resulting ADRs come after both skills are scored here.

## `ridgeline-doc-writer`

| # | Dimension | Your score | Reason |
| --- | --- | --- | --- |
| 1 | Source hierarchy | 1 | Present (lines 73-76, "Precedence when sources conflict") but not labeled "Source hierarchy" the way `unused-access-expert` labels its own - should be consistent across skills |
| 2 | Findability | 0 | The skill's own description includes "review" and "audit" language that also matches `ridgeline-doc-auditor`'s entire job; `CLAUDE.md` needs a separate table to disambiguate, meaning the description alone doesn't reliably route the request |
| 3 | Progressive disclosure | 1 | Does the job, but could do it better - headings are accurate and rules are clear, but headings should be labeled better and sections should be more bulleted |
| 4 | Boundaries and routing | 1 | Points at other skills, but the pointer isn't reciprocal - the skills it refers to don't point back |
| 5 | Controlled vocabulary | 1 | Bundled glossary copy currently matches `unused-access-expert`'s copy, but nothing enforces that - no canonical file exists (score applies to the pair, not this skill alone) |
| 6 | Grounding discipline | 2 | - |
| 7 | Output correctness | 0 | Current routing genres (Feature overview, Report deep-dive, Reference page) don't map to the real `template:` values the gates check for (`parent-report`, `child-report`, `workflow-methodology`) - a fresh draft wouldn't carry a `template:` tag at all, so no gate could ever run on its output |
| **Total** | | **6 / 14** | |

**Standalone findings (not rubric scores, but bugs to fix during revision):**
- `unused-access-expert/SKILL.md` has a stray line above its real frontmatter -
  `# SKILL.md - Paste into ridgeline-docs/ai-workflow/skills/unused-access-expert/SKILL.md` - an
  H1 heading with no `description:` field, clearly a leftover copy-paste artifact, not part of the
  actual frontmatter block.
- The "Source hierarchy" heading/label should appear consistently in both skills - see Dimension 1.

## `unused-access-expert`

*Pending - your independent pass not yet done.*

## Claude's pass

*Pending - happens after both skills above are scored.*

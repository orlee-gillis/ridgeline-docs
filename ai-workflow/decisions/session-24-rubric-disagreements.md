# Session 24 - Rubric Scoring Disagreements

Three places where the independent rubric passes (yours and Claude's) landed on different scores
for the same skill and dimension. Per `ai-workflow/skills/rubric.md`'s own instructions, the
disagreement is the interesting part - recorded here rather than just averaged away.

## 1. `ridgeline-doc-writer`, Dimension 1 (Source hierarchy): 1 vs. 2

**The disagreement.** The precedence rule at lines 73-76 ("verified product behavior wins, then
`unused-access-expert`'s knowledge base... then the glossary... then the style guide, then this
body") is explicit and ranked, covering a real conflict case (style guide vs. glossary casing).
Your score of 1 weighed that it isn't under its own labeled heading, unlike `unused-access-expert`'s
"## Source hierarchy" section - easy to miss on a skim. Claude's score of 2 weighed the rubric's
literal wording, which asks whether precedence is stated explicitly and unambiguously, not how it's
labeled.

**Decision:** both concerns are real, but they're different questions. The rubric measures whether
the precedence *exists and is unambiguous* - it does, so the content clears a 2. Whether it's
*labeled consistently and easy to find* is a real, separate finding, folded into Dimension 3
territory (progressive disclosure / findability-within-the-document) instead of penalizing
Dimension 1 twice for one root cause.

**Action for revision:** add a `## Source hierarchy` heading to `ridgeline-doc-writer` around line
73, matching `unused-access-expert`'s labeling, so the same content is easier to find on a skim -
independent of which dimension's score it affects.

## 2. `unused-access-expert`, Dimension 3 (Progressive disclosure): 0 vs. 1

**The disagreement.** The "High-risk sections" block (lines 21-27) restates three facts directly in
the body (e.g., "§3 - Usage classification. Undetermined is not Unused...") instead of only citing
the section number and pointing to `knowledge-base.md`. Your score of 0 treated this as the body
acting as a second source of truth. Claude's score of 1 treated it as a small, deliberate repeat of
only the three highest-stakes safety facts - not the whole knowledge base - which is a defensible
technical-writing choice for the facts where a wrong answer causes the most damage.

**Decision:** both readings are legitimate, and the real question underneath is whether "deliberate
redundancy for the highest-stakes facts" is an exception to progressive disclosure or a violation of
it. Landing on **0** for this round: even a deliberate, narrow duplication is still a second copy of
the same fact that can drift from `knowledge-base.md`'s own wording over time, and this rubric
dimension is specifically about drift risk, not about whether the duplication was well-intentioned.

**Action for revision:** replace the restated facts in "High-risk sections" with section citations
only (e.g., "§3 - see `knowledge-base.md` for why this is the highest-risk section"), removing the
duplicate copy entirely rather than deciding whether the duplicate is currently accurate.

## 3. `unused-access-expert`, Dimension 7 (Output correctness): 2 vs. N/A

**The disagreement.** Your score of 2 reasoned that the skill's rigorous source hierarchy supports
factually correct output whenever it's paired with `doc-writer`, even though it never produces a
page by itself. Claude's position: the rubric's own wording ("when this skill produces or edits a
page, does the result satisfy...") presupposes the skill produces a page - this one structurally
never does, alone, so scoring it on this axis measures something the skill was never built to do.

**Decision:** this dimension doesn't apply to `unused-access-expert` scored in isolation - mark it
**N/A**, not a number, and total this skill's score out of 12 (six scored dimensions), not 14. Retro-
fitting a number onto a dimension that doesn't structurally apply would make the two skills' totals
look directly comparable when they're not measuring the same thing for both.

**Action for revision:** none needed on the skill itself - this is a scoring-methodology fix, not a
skill defect. If a future dimension is added to measure "quality of facts supplied to a paired
skill's output" specifically, this is the skill it would apply to; Dimension 7 as written is not
that dimension.

## Updated totals

| Skill | Your total | Claude's total |
| --- | --- | --- |
| `ridgeline-doc-writer` | 6/14 | 7/14 |
| `unused-access-expert` | 8/14 | 7/12 (Dimension 7 excluded as N/A) |

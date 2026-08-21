# Skill Quality Rubric

Seven dimensions for scoring a Claude Skill (its instruction file, references, and the output it
produces) - used to audit `ridgeline-doc-writer` and `unused-access-expert` in Session 24. This
file didn't exist before Session 24, despite being referenced in `TRACKS.md` and
`docs-as-code/roadmap.md` as if it already did - written now, as the actual first step, before any
scoring happens.

**Grounding.** Dimensions 1-5 come from the NN/g context-architecture framework and Anthropic's
skill-authoring guidance, both already named (but never formally scored) in
`docs-as-code/roadmap.md`'s "Where the course learning shows up" table. Dimensions 6-7 are new
here, added because they're the two places this project has *already* produced concrete,
measurable evidence about skill quality - the `[VERIFY]` convention (Module 3) and the three real
genre gates (Sessions 22-23) - and a rubric that ignores its own project's existing data would be
worse than one that uses it.

## The rubric

| # | Dimension | 0 — Fails | 1 — Partial | 2 — Meets the bar |
| --- | --- | --- | --- | --- |
| 1 | **Source hierarchy** — what wins when sources conflict | No stated precedence at all | Precedence stated but vague, or only for some source pairs | Explicit, ranked precedence; unambiguous for a realistic conflict case |
| 2 | **Findability** — can the right skill get picked from its description alone | Two skills could plausibly both claim the same request | Description narrows it down, but a real ambiguity remains | A wrong selection, reading the description alone, would be surprising |
| 3 | **Progressive disclosure** — lean body, detail one level down | Body tries to be both the summary and the source of truth | Some facts pushed to `references/`, some still duplicated in the body | Body reads in a couple of minutes; every checkable fact has a clear reference |
| 4 | **Boundaries and routing** — what this skill explicitly doesn't cover | Scope only implied by what's absent | One-directional scope note (says what it's not, no pointer back) | Explicit, reciprocal pairing: each skill names the other and when to switch |
| 5 | **Controlled vocabulary** — one term, one meaning | The two bundled glossary copies (one per skill) disagree with each other, or a skill's own body defines a term differently from its glossary copy | Copies currently agree, but nothing enforces that - no canonical file exists, just two copies that happen to match | Same as "1" - there is no way to reach a real "2" here until a single canonical glossary exists; see the note below |
| 6 | **Grounding discipline** — flags what it doesn't know instead of inventing | No instruction to flag uncertainty at all | Flags inconsistently; some confident inventions surfaced in `[VERIFY]` resolution | `[VERIFY]` instruction is specific; invented-and-uncaught inaccuracies are rare to absent in the resolved set |
| 7 | **Output correctness** — does its output pass the real genre gate | Gate severity `blocker`, or the page is missing the `template:` tag the gate needs | Gate severity `should-fix` | Gate severity `none` on a representative sample |

**Scoring scale:** 0 / 1 / 2 per dimension, 14 total. The number matters less than being able to
justify each score with a specific line or example from the skill file - a rubric that just
produces a number without a reason isn't more rigorous than a vibe, it's just a vibe with a number
attached.

## Notes on specific dimensions

- **Dimension 1** has a concrete real example already in `unused-access-expert/SKILL.md`'s
  "Source hierarchy" table (a 5-row ranked list) - that's what a 2 looks like.
- **Dimension 6** should use real evidence, not a reading of the prose alone: check how many
  `[VERIFY]` flags in `docs/` turned out to be legitimate gaps vs. confident inventions the flag
  convention still caught (Session 24's own resolution pass, recorded in
  `ai-workflow/decisions/UAX-2841.md`, is the data source).
- **Dimension 7** is the one dimension with a hard, already-built measurement tool: run the
  relevant gate (`validate-parent-report` / `validate-child-report` / `validate-workflow-methodology`)
  against a page the skill produced or edited, and read its severity directly.
- **Dimension 5 has no real path to a 2 right now.** There is no canonical glossary file - only
  two bundled copies, one per skill (`ridgeline-doc-writer/references/glossary.md` and
  `unused-access-expert/references/glossary.md`), confirmed byte-for-byte identical as of Session
  24 but with nothing enforcing that going forward. This is the same drift risk already flagged in
  `docs-as-code/roadmap.md`'s "glossary reconciliation" TODO. Creating a single upstream copy both
  skills point to (rather than bundle) is the fix that would unlock an actual 2 - worth raising as
  a finding/ADR from this audit, not something to silently work around in the score.

## How to use this

1. **You score both skills first**, independently, before reading Claude's pass - that's the whole
   point of "you first, then together": two independent reads catch more than one read plus an
   echo of it.
2. For each dimension, write the score and the one-line reason (a quote, a missing line, a gate
   result) - not just the number.
3. Claude scores next, same seven dimensions, same skills.
4. Where scores disagree, that disagreement is the interesting part - write it up as a short ADR
   (`ai-workflow/decisions/`), not just an averaged number.
5. Re-run this same rubric in Session 28 (The Defense, deferred to the very end) against the
   revised skills. The comparison is the before/after evidence - this is why the scale and
   dimensions need to stay fixed between the two runs, not be redesigned each time.

See `rubric-example.md` for what a filled-in row looks like in practice.

# Skill Quality Rubric

Seven dimensions for scoring a Claude Skill (its instruction file, references, and the output it
produces) - used to audit `ridgeline-doc-writer` and `unused-access-expert` in Session 24. This
file didn't exist before Session 24, despite being referenced in `TRACKS.md` and
`docs-as-code/roadmap.md` as if it already did - written now, as the actual first step, before any
scoring happens.

**Grounding.** The first five dimensions come from the NN/g context-architecture framework and
Anthropic's skill-authoring guidance, both already named (but never formally scored) in
`docs-as-code/roadmap.md`'s "Where the course learning shows up" table. The last two are new here,
added because they're the two places this project has *already* produced concrete, measurable
evidence about skill quality - the `[VERIFY]` convention (Module 3) and the three real genre gates
(Sessions 22-23) - and a rubric that ignores its own project's existing data would be worse than
one that uses it.

**Scoring scale**, per dimension: **0 = fails** (absent or actively wrong) · **1 = partial** (present
but incomplete, inconsistent, or unclear) · **2 = meets the bar** (clear, complete, consistently
applied). Total out of 14. The number matters less than being able to justify each score with a
specific line or example from the skill file - a rubric that just produces a number without a
reason isn't more rigorous than a vibe, it's just a vibe with a number attached.

## The seven dimensions

### 1. Source hierarchy
What wins when sources conflict (the skill's own instructions vs. a feature note vs. the glossary
vs. the model's own knowledge)? Score 2 if the skill states this explicitly and the precedence is
unambiguous for a realistic conflict case. Score 0 if there's no stated precedence at all.

### 2. Findability
Does another skill (or a person skimming `CLAUDE.md`'s skill-triggers table) know when to reach for
this skill vs. a sibling, from the name and description alone - without opening the file? Score 2
if the trigger description is specific enough that a wrong selection would be surprising. Score 0
if two skills could plausibly both claim the same request.

### 3. Progressive disclosure
Is the skill body lean, with facts and detail pushed one level down into `references/`? Score 2 if
the body reads in under a couple of minutes and every fact a reader might need to double-check has
a clear reference to check it against. Score 0 if the body is trying to be both the summary and the
source of truth at once.

### 4. Boundaries and routing
Does the skill say what it does *not* cover, and where to go instead? Score 2 if there's an
explicit, reciprocal pairing line (this skill says "not X, see Y," and Y says "not this, see this
skill"). Score 0 if scope is only implied by what's absent.

### 5. Controlled vocabulary
Is there one term for one concept, consistently, and does the skill point at the glossary as the
enforcement mechanism rather than restating its own copy of the terms? Score 2 if the skill has no
terminology that conflicts with `ai-workflow/glossary.md`. Score 0 if the skill bundles its own
copy of terms that could drift from the public glossary (the exact failure mode already flagged in
`docs-as-code/roadmap.md`'s glossary-reconciliation TODO).

### 6. Grounding discipline
Does the skill's own instructions tell the model to flag what it doesn't know (`[VERIFY: ...]`)
rather than invent an answer, and is that instruction specific enough to actually produce that
behavior? Score this using real evidence, not a reading of the prose alone: look at how many
`[VERIFY]` flags in `docs/` turned out to be legitimate gaps vs. confident inventions the flag
convention still caught (Session 24's own `[VERIFY]` resolution pass, recorded in
`ai-workflow/decisions/UAX-2841.md`, is the data source). Score 2 if invented-and-uncaught
inaccuracies are rare to absent in the resolved set. Score 0 if the skill's instructions don't
mention flagging uncertainty at all.

### 7. Output correctness against genre requirements
When this skill produces or edits a page, does the result actually satisfy the real genre gate it
should be checked against (`validate-parent-report`, `validate-child-report`, or
`validate-workflow-methodology`)? This is the one dimension with a hard, already-built measurement
tool: run the relevant gate against the skill's output. Score 2 if gate severity is `none` on a
representative sample. Score 1 if `should-fix`. Score 0 if `blocker`, or if the page doesn't carry
the `template:` tag the gate needs to run at all.

## How to use this

1. **You score both skills first**, independently, before reading Claude's pass - that's the whole
   point of "you first, then together": two independent reads catch more than one read plus an
   echo of it.
2. For each dimension, write the score and the one-line reason (a quote, a missing line, a gate
   result) - not just the number.
3. Claude scores next, same seven dimensions, same skills.
4. Where scores disagree, that disagreement is the interesting part - write it up as a short ADR
   (`ai-workflow/decisions/`), not just a averaged number.
5. Re-run this same rubric in Session 26 against the revised skills. The comparison is the
   before/after evidence - this is why the scale and dimensions need to stay fixed between the two
   runs, not be redesigned each time.

See `rubric-example.md` for what a filled-in dimension entry looks like in practice.

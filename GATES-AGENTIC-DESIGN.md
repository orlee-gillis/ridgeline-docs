# Agentic Gates - Design Sketch (Phase H, not built)

Session 23, Part C. A plan for Phase H's stretch idea - gates that fix issues automatically,
not just report them - written as a decision doc so Phase H starts from a design, not a blank
page. Nothing here is implemented; this is deliberately a sketch, not a build.

## The idea

The three genre gates (`validate-parent-report`, `validate-child-report`,
`validate-workflow-methodology`) currently do one thing: read a page, compare it against a written
standard, and report a severity (`none` / `should-fix` / `blocker`) with a suggestion per issue.
A human reads the report and makes the edit. An agentic gate would go one step further: propose
the actual fix as a diff, not just a description of what's wrong.

## What it would need

**Write access, scoped to a proposal, not a commit.** The gate never pushes a fix to `main` or
even to the PR's own branch directly - it opens its own branch and PR (or posts the diff as a
suggested-change comment on the existing PR) so the fix is a proposal, exactly like a human
contributor's would be. This is the same blocking-vs-advisory reasoning Module 4 already applies
to the read-only gates, carried one level further: a gate that can write code is a gate that can
introduce a bug, so its output stays advisory until a human merges it.

**A review step, always.** No auto-merge, ever, regardless of the gate's confidence score. The
gate's own confidence is not a substitute for a second reader - that's the exact lesson Session 22
already taught the hard way (the original `audit-report-pages` gate was built and merged on an
unverified premise, and stayed broken silently for a full session before anyone checked it against
real content). A fix-capable gate that can also merge itself removes the one check that catches
that kind of failure.

**A rollback path.** If a merged fix turns out wrong (misreads the page, "fixes" a legitimately
flagged `[VERIFY]` placeholder by inventing an answer, etc.), reverting it needs to be a single
`git revert` of a clean, isolated commit - never squashed into unrelated changes. This is free if
the fix always ships as its own PR (see write access, above) rather than folded into whatever PR
triggered the gate.

**A narrow confidence/scope gate before it proposes anything.** Only propose a fix for issue
classes the gate can fix mechanically and safely - e.g., a missing required section header, a
known-wrong fact that has exactly one correct value elsewhere in the docs. Never propose a fix for
anything that requires judgment the gate doesn't have grounds for - an open `[VERIFY]` placeholder
is the clearest example of a "problem" that should never get an invented fix; the honest-limitations
convention this whole project runs on (flag, don't smooth over) applies to the gate's own behavior
too, not just to human-facing drafts.

## What it would look like, concretely

1. A genre gate runs as today and finds an issue with a mechanically-fixable class (e.g., missing
   the "Data freshness" section a parent-report requires).
2. Instead of only reporting it, the gate drafts the missing section using the same structured-
   output call, but scoped narrowly (fill in this one section per the checklist, don't touch
   anything else).
3. It opens a new branch + PR containing only that section addition, with a PR description stating
   what triggered it, which gate proposed it, and a link back to the PR/commit it was proposed for.
4. A human reviews and merges (or closes) that PR like any other. The original PR that triggered
   the gate is unaffected until the fix PR is merged separately.

## Non-goals

- No auto-merge, under any confidence threshold.
- No fixes for anything the gate would otherwise report as `should-fix` or `blocker` due to a
  missing judgment call (an open `[VERIFY]`, an ambiguous factual claim) - those stay
  human-authored.
- No expansion of what a gate looks at - an agentic gate proposes fixes only within the same
  genre-checklist surface its read-only version already checks, not a general-purpose editor.

## Why this is Phase H, not now

Getting the blocking-vs-advisory boundary right for a *read-only* gate took two real sessions
(21, then the Session 22 correction) to get right, and that gate can only be wrong in one
direction - a bad report a human then double-checks. A write-capable gate can be wrong in two
directions - a bad report, or a bad fix that looks plausible enough to merge without enough
scrutiny. That's a materially higher-risk surface, and it deserves the same slow, verify-against-
real-content rigor Session 22 needed, not a rush to ship code. Phase H is explicitly optional and
post-capstone for exactly this reason - it's pure upside if the pipeline is already stable, not a
dependency of anything before it.

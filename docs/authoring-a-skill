---
title: Writing a documentation skill, and finding out what was wrong with it
description: Three Claude skills written for this documentation set, what the first run of them exposed, and what changed as a result.
sidebar_position: 95
---

I wrote two Claude skills to work on this documentation set, ran them against two finished pages, and
found that most of what went wrong was in how I had written the skills rather than in what the model
did with them. This is the record.

> Skills were specified, scoped, and reviewed by me; the files were drafted with Claude. The
> conclusions below are mine.

## The two skills

| Skill | Job |
|---|---|
| `unused-access-expert` | Keep factual claims about the product correct |
| `ridgeline-doc-writer` | Keep the page's genre, structure, and style correct |

They were written to be used together on one request, with each description naming the other. That part
worked: both loaded on a single prompt, and their findings barely overlapped - `unused-access-expert`
returned 14 problems, `ridgeline-doc-writer` returned 44, and one problem appeared on both lists.

## What the first run exposed

58 problems across two pages, in one flat list, with no severity and no ordering. Three things were
wrong, and two of them were mine.

**I used drafting skills to audit.** Both skills were written to produce pages. Auditing appeared in
each description as a trailing clause and nowhere in either body. So the run had no cap, no ranking, and
no citation requirement - none of which had been written, because auditing had never been specified.

**One reported rule did not exist.** `ridgeline-doc-writer` reported a style violation citing a rule
absent from its own style guide. Its knowledge-base equivalent could not have done this: that file's
sections are numbered, so every factual claim came back as *"§8 says…"* and could be checked in seconds.
The style guide had no numbering, so a rule cited from it could not be traced - and one turned out to be
invented.

**The volume defeated the review.** 58 unranked problems is more than a reviewer will rule on
individually, so I approved the mechanical ones as a class. That is a reasonable strategy, but it means
the invented rule was caught by scepticism rather than by process. One question stood between it and
shipping.

## What changed

**A third skill, written for auditing.** `ridgeline-doc-auditor` has the output contract as part of its
specification: at most 20 problems per page, three defined severity levels, a required source line per
problem, and a rule that a problem with no source is deleted before returning. It also declares what it
does not check.

**Countable rules moved out of the skill and into the build.** Banned terms, Latin abbreviations,
punctuation, and required frontmatter fields are now Vale rules and CI checks that block a pull request.
A skill can paraphrase a rule; a linter runs it. Because the auditor was written after that decision, it
excludes those classes by design rather than discovering the overlap later.

## Result of the second run

Same two pages, same model, purpose-built skill.

| | First run | Second run |
|---|---|---|
| Problems reported | 58 | 25 |
| Problems with no cited source | 1 | 0 |
| Severity assigned | No | 8 blockers, 13 should-fix, 4 optional |
| Statement of what the page is for | None - I wrote both by hand | 2, one per page, required by the skill |

The 33 problems that disappeared were not dropped. They moved: 14 to Vale, 7 to the build's link
checking, 5 to markdownlint, 2 to a frontmatter check, and 5 were draft hygiene rather than audit
findings.

This is not a blind comparison - the same model produced both runs and the skill between them, and most
of the reduction is the intended effect of exclusions rather than better judgment. What it does show is
that the output contract holds.

## The rule worth keeping

Countable rules belong in a build gate, because a gate executes them. Judgment stays with the writer,
because nothing executes it.

Both pages audited here are still organised by interface layout - panel, summary, graph, table - rather
than by the order a reader works through the task. No rule in the gate detects that, and no skill raised
it. That question is the reason for moving everything else out of the way.

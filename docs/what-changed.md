---
title: What changed, and why
description: A before-and-after account of two documentation pages, the audit that drove the rewrite, and what the two passes caught differently.
sidebar_position: 90
---

These pages are fictionalized from documentation I wrote and published professionally. The structure
and the flaws are real; the product and its vocabulary are not.

The earlier versions are preserved in `ai-workflow/legacy/`. I audited them unaided first, then ran
two Claude skills over the same pages - one carrying the feature's subject-matter knowledge, one
carrying the style guide, glossary, and page templates. The merged findings drove the rewrite.

## The biggest changes

**A safety guarantee that was missing from both pages.** Access rights the activity logs cannot
audit are classified **Undetermined**, and the product treats them as *used* - remediation never
removes them. Both pages named the classification and neither explained that. For a security
feature, a reader who reads **Undetermined** as "probably unused" draws the opposite conclusion from
the truth, and might approve a change that breaks a production workload. It now appears on both
pages, as an admonition, in the same words.

**The report page didn't say what to do next.** It explained the report thoroughly and then stopped.
The single failure on my own purpose checklist, and the most consequential structural problem: a
prioritization report whose reader doesn't know where to go next has done half its job. There is now
a numbered path from a row to the surface where you act on it.

**One page stopped depending on another.** The Access tab page linked out for four concepts -
category, scope, JIT grants, inheritance. Those links pointed at a page now out of scope, so rather
than repointing them I explained each concept in place. The page got longer and became
self-sufficient. Deferring an explanation is only free when the target actually exists.

**A factual error the fictionalization introduced.** Translating "entity" to "integration" is correct
almost everywhere, but the rewrite applied it to a sentence where the referent was a *resource* -
producing "expandable nodes containing underlying integrations," which is wrong about what the
interface does. Mechanical vocabulary substitution creates errors that read perfectly fluently. It
is now recorded as a defect in the translation method, not a typo.

**Terminology that changed a claim.** The report page said rows sort by "unused access rights" when
they sort by unused *grants*. A grant is a container holding many rights, so the two produce
different orderings. This is exactly the distinction the glossary exists to hold, and it shows how a
terminology slip stops being cosmetic.

**Reference links that pointed nowhere.** Five cross-page anchors resolved to headings that did not
exist - the target page's headings generated different anchor text. All five are gone.

## What the two passes caught differently

| Page | I found | Skills found | Both |
| --- | --- | --- | --- |
| Unused Access report | 10 | 14 | 7 |
| About the Access tab | 12 | 22 | 1 |

The overlap collapsed on the second page, and the reason matters. Its problems were mostly invisible
when reading: broken anchors, a column named two different things across two pages, a factual error
introduced in translation. No amount of careful reading surfaces those. The first page's problems
were editorial - dense paragraphs, confusing headings, missing structure - and there the two passes
largely agreed.

Which is a concrete argument for automating the second class. Broken links and terminology
consistency are countable, so they belong in a build gate rather than in a reviewer's attention.
Judgment about whether a page does its job is not countable, and stays with the writer.

## What I left alone

The legacy pages are unedited and stay that way. They are the "before", and tidying them would
remove the evidence.

I also left the deeper structural question open on both pages: each is still organized around *what
the interface contains* rather than *what the reader is trying to decide*. Fixing that means
rewriting rather than revising, and the revision needed to be comparable against the original to be
worth anything.

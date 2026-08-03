---
title: About the <Report name> report
description: What the <Report name> report includes, how it is ordered, and what to do with a finding.
sidebar_position: <10 / 20 / 30 ...>
---

<!-- REPORT DEEP-DIVE TEMPLATE
     Purpose: a reader looking at this report right now, deciding whether a row deserves their
     attention and what to do about it.
     The three questions this genre must answer, in this order: why is this row here, why is it near
     the top, and what do I do next. Inclusion criteria before columns - a reader who does not know
     what puts a row in the report cannot interpret any column in it.
     Delete every comment block before handing over the draft. -->

<Opening paragraph: what the report shows and the decision it supports. One or two sentences.>

`[SCREENSHOT: the report with several representative rows, columns visible]`

## What the report includes

<The inclusion criteria: what puts a row here. Be specific about the unit of the row - an
integration, a grant, a finding - because every column reads differently depending on it.>

<Then the exclusions, if any are non-obvious. A reader hunting for something absent needs this
before they file it as missing data.>

## How the report is ordered

<The sort, and the score or metric behind it. Name the score exactly as the glossary names it. If the
feature deliberately has no score of its own, say so - it prevents readers from inventing one.>

<If a score can be empty or null, say what that means. An unexplained blank reads as a defect.>

## Columns

| Column | What it shows |
| --- | --- |
| | |
| | |

<Note any column whose value is relative rather than absolute, and say what it is relative to. A
count that legitimately differs between two rows that look identical generates support questions
unless the page explains it.>

## Filters and views

<The filters worth knowing, and any generic controls - column configuration, export - covered with a
pointer rather than a walkthrough. Do not describe a column set you have not confirmed.>

## Working a finding

<What the reader does after a row catches their attention: which surface to open, what to look at
there, what to act on. Link to the investigation surface; do not duplicate its walkthrough here.>

1. <Step>
2. <Step>
3. <Step>

:::important
<A risk of failure, confusion, or a messy outcome. Use this for a safety guarantee the reader must
not misread - state the guarantee positively and unambiguously.>
:::

## Data freshness

<How often the data recalculates, and therefore when a change made elsewhere appears here. This is
the answer to "why don't I see my change yet," and its absence is a reliable ticket generator.>

## Related

- [<Investigation surface page>](<relative-path>.md)
- [<Parent or sibling page>](<relative-path>.md)

## Open items for SME review

<!-- Collect every flag from above. -->

- [ ] `[VERIFY: ...]`

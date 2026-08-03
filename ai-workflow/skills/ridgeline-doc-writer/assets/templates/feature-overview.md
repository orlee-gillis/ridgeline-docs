---
title: <Feature name>
description: <One sentence a reader would recognize as answering their question. Not a summary of the page.>
sidebar_position: <10 / 20 / 30 ...>
---

<!-- FEATURE OVERVIEW TEMPLATE
     Purpose: a reader who has heard the feature named and wants to know what it is, whether it
     applies to them, and what it cannot do.
     Order is deliberate: value before mechanism, limits before actions. A reader who bails after
     two paragraphs should still have the right expectations.
     Delete every comment block before handing over the draft. -->

<Opening paragraph: what the feature does, in the reader's terms and in one or two sentences. Lead
with the outcome, not the machinery. Name the problem it removes.>

<Second paragraph: where it lives in the product and what surfaces it has. Link the first mention of
each surface that has its own page.>

## Who this is for

<The audience and their job. If the feature serves two audiences with different jobs, say both and
say which surface serves which - do not average them into one imagined reader.>

## Prerequisites

<What must be true before the feature returns anything useful: connections, data age, permissions.
If nothing is required, say so explicitly - "no additional platform permissions are required" is an
answer readers actively look for, and its absence reads as an omission.>

## How it works

<The mechanism, at the depth needed to trust the output and interpret an unexpected result. Not the
implementation. If a design decision looks like a bug from the outside, explain it here.>

<Use a table when two or more criteria organize the rows. Categories, states, and classifications
almost always want a table:>

| <Criterion> | <Criterion> | <Criterion> |
| --- | --- | --- |
| | | |

## What you can do

<The key actions, in the order a reader would take them. One bullet or short subsection per action,
each linking to the page that covers it in full. This section routes; it does not instruct.>

## Limits and known gaps

<Not optional for a security feature. What the feature does not cover, what it cannot see, and where
its data has boundaries. A reader who over-trusts a security page makes worse decisions than a reader
who read nothing.>

:::note
<Supplementary information a reader can skip. If the fact is load-bearing, move it into the prose.>
:::

## Related

- [<Sibling page>](<relative-path>.md)
- [<Sibling page>](<relative-path>.md)

## Open items for SME review

<!-- Collect every [VERIFY: ...], [SCREENSHOT: ...], [CHILD URL: ...], and [UNRELEASED] flag from
     above. Delete this section only when it is genuinely empty. -->

- [ ] `[VERIFY: ...]`

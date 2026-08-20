---
title: <Verb the action> - <object>
description: What it takes to <action>, what happens at each stage, and where it stops short.
sidebar_position: <10 / 20 / 30 ...>
template: workflow-methodology
---

<!-- WORKFLOW-METHODOLOGY TEMPLATE
     Purpose: a reader about to carry out one action from start to finish, who needs to know what
     it takes to begin, what happens at each stage, and what it cannot undo.
     Order is deliberate: prerequisites before scope, scope before mechanics, mechanics before
     limits. A reader who starts before checking prerequisites fails partway through instead of
     before starting.
     Delete every comment block before handing over the draft. -->

<Opening paragraph: what this workflow does and the outcome it produces, in the reader's terms.>

## Prerequisites

<What must be true before the workflow can be started - permission, connection state, data
freshness. A reader who doesn't meet them needs to know before attempting, not after failing.>

### <Prerequisite that has its own failure mode, if any>

<A single prerequisite complex enough to need its own explanation - e.g., what happens if it isn't
met, or how to satisfy it - gets its own subsection rather than a single bullet.>

## What you can do

<The scope of the workflow, stated plainly - what it covers and, as importantly, what it does not.
Without this, a reader can't tell whether this workflow covers their situation.>

## How <the action> runs

<The mechanics, in the order they actually happen. Each stage a reader would recognize as a
distinct step gets its own subsection below - do not compress multiple stages into one paragraph
just because they happen quickly.>

### <Stage>

<What happens at this stage, at the depth needed to trust the outcome.>

### How to reverse <the action>

<!-- BLOCKER if this section is missing or vague for a hard-to-reverse or destructive step. A
     reader may act without knowing what it can't undo. -->
<The guarantee attached to this action, stated positively and unambiguously: is it reversible, for
how long, and what the reader does to reverse it. If it is not reversible, say so as plainly as if
it were.>

### When changes appear

<How soon the result of this action is visible elsewhere - the same "why don't I see my change yet"
question a parent-report's data-freshness section answers, applied to this action's outcome.>

### When <the action> fails

<What a reader sees on failure, and how failure differs from a successful-but-reversed outcome, if
the two could be confused.>

## Limits and known gaps

<What this workflow does not cover, cannot do, or does not yet handle. A reader who over-trusts an
incomplete workflow makes worse decisions than one who read nothing.>

## Related documents

- [<Parent or sibling page>](<relative-path>.md)

## Open items for SME review

<!-- Collect every flag from above. -->

- [ ] `[VERIFY: ...]`

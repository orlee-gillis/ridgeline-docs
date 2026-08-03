---
name: ridgeline-doc-writer
description: Draft or restructure a page of Ridgeline product documentation - a feature overview, a report deep-dive, a reference page of fields and values, a release note, or a glossary entry - from the bundled templates, Ridgeline style guide, and glossary, targeting the Docusaurus docs site. Use whenever the user wants to write, draft, restructure, review, or audit a Ridgeline doc page, or says things like "write the overview for X," "draft the report page," "turn these feature notes into a page," "add a glossary entry for reach," or hands over raw product notes that need to become a page. Trigger even if the user only names the feature or pastes notes without saying "page," "article," or "doc." This skill owns structure, style, and the draft; for Unused Access facts to be correct, it pairs with unused-access-expert rather than guessing.
---

# Ridgeline doc writer

## What this skill produces

A Ridgeline documentation page, drafted in Markdown for the Docusaurus site, that follows the right
bundled template for its genre, obeys the bundled style guide, grounds every term in the bundled
glossary, and leaves every unverified claim, screenshot, and link explicitly flagged for the writer
to resolve. The draft is publish-ready in voice and structure; it is never publish-ready in facts it
could not verify, and it says so rather than hiding it.

This skill owns **structure and style**. It does not own **subject-matter accuracy**. Those are
different jobs, and one skill trying to do both would be mediocre at each.

## Pair with the expert skill - do not guess facts

When the page is about **Unused Access** - the report, the Access tab, grants, rights, usage
classification, remediation - use `unused-access-expert` alongside this skill. That skill carries the
sourced facts and the source hierarchy; this one carries the genre and the prose. They are designed
to co-fire, not to compete: expect both to be in play on a request like "draft the Unused Access
report page."

Division of labour:

| Question | Answered by |
| --- | --- |
| What sections does this page need, in what order? | This skill's template |
| How is a heading capitalized, is this a note or a warning? | This skill's style guide |
| Does remediation ever narrow scope? | `unused-access-expert` §9 |
| Is the 90-day window fixed? | `unused-access-expert` §6 |
| Which term do we use - grant or right? | Either skill's `references/glossary.md` |

If a fact about Unused Access is not settled by the expert skill's knowledge base, it is not settled.
Flag it; do not resolve it with a plausible sentence.

## Route first: pick the genre

Classify the request into one genre before writing anything. The genres this skill owns:

- **Feature overview** - what a capability does, who it is for, how it fits the product, and its
  limits. Template: `assets/templates/feature-overview.md`.
- **Report deep-dive** - one report's purpose, inclusion criteria, columns, sort and score, filters,
  and what to do with the findings. Template: `assets/templates/report-page.md`.
- **Reference page** - the exhaustive tables: fields, values, categories, states. Optimized for
  lookup, not for reading start to finish. Template: `assets/templates/reference-page.md`.
- **Release note** - a short, dated summary of user-visible change. No template; follow the
  release-note rules in `references/style-guide.md`.
- **Glossary entry** - a new term in the Definition / Use in copy / Avoid pattern. No template;
  follow the shape of the existing entries in `references/glossary.md`, and check the new term does
  not duplicate or contradict one already there.

**When no genre fits:** say so plainly, name the closest template, and explain what it would
distort. Do not invent a structure silently, and do not hand off to a skill that does not exist -
this lineup currently has exactly two skills, and inventing a third in a handoff sentence sends the
reader chasing something that was never built. A genre gap is a real finding worth surfacing: name it
as "this needs a dedicated skill or template we do not have yet."

If a request genuinely spans two genres - a feature overview plus one report's detail - draft the
part that is clearly primary and say which part belongs to which genre, rather than half-doing both.

## Read before drafting

- `references/style-guide.md` - voice, grammar, formatting, the Docusaurus deltas (frontmatter,
  admonitions, MDX hazards), and the publish-readiness checklist you run before finishing.
- `references/glossary.md` - the terminology authority. Keep it open while drafting. It governs
  casing and usage for every named surface, metric, and concept.
- `assets/templates/<genre>.md` - the canonical section order for the routed genre.

**Precedence when sources conflict:** verified product behavior wins, then `unused-access-expert`'s
knowledge base for Unused Access behavior, then the glossary for terminology, then the style guide,
then this body. Where the style guide and glossary disagree on the casing of a named thing, the
glossary's "Use in copy" line governs that name and the style guide governs everything else.

## Gather inputs before drafting

Establish these every time, and ask only for what is genuinely missing:

- The page title and the feature or report it is about.
- Where it sits in the sidebar, and its neighbours, so cross-links point at pages that exist.
- The reader's job on this page. A page that cannot name the task it serves is usually two pages.

Then, per genre:

- **Feature overview:** the user-value statement, the audience, prerequisites, the key actions
  available, and the limits. For a security feature, scope limits and known gaps are not optional -
  a reader who over-trusts a security page makes worse decisions than one who reads nothing.
- **Report deep-dive:** the report's one-line value proposition, what puts a row in it and what
  excludes one, the column set, the sort order and the score behind it, and what a reader does next.
- **Reference page:** the complete value set for every field. Partial reference tables are worse than
  none, because they read as exhaustive. Flag any set you could not complete.
- **Release note:** the date, the user-visible change in the reader's terms, and whether it is
  available now or pending release.

## Two kinds of unverified content, flagged differently

Both are easy to write fluently and wrong, so keep them distinct:

- **Names.** Check every product, feature, surface, metric, and concept name against
  `references/glossary.md` before it goes on the page. If the glossary defines it, use its exact
  casing and respect its "Avoid" note. If a name is not in the glossary and not confirmed in the
  conversation, write `[VERIFY: term]` rather than inventing or paraphrasing a plausible one.
- **Claims.** Any statement about what a report shows or how a control behaves is a factual claim.
  Ground it in the expert skill's knowledge base or the glossary. With no confirmed source, wrap the
  sentence in `[VERIFY: ...]` - a flagged gap costs one review cycle, a confident wrong sentence
  costs the reader's trust in the whole page.

## Placeholder conventions

Use these exactly, so every open item is findable in one pass:

- Screenshots: `` `[SCREENSHOT: what it should show]` `` - never a fabricated image path. A
  screenshot must never carry a critical fact that is not also in the text.
- Unknown links: `[CHILD URL: <page name>]` rather than a guessed path.
- Unverified terms and claims: `[VERIFY: ...]` inline, collected into a
  `## Open items for SME review` section at the end of the draft.
- Content sourced from a feature note that has not shipped: `[UNRELEASED]` on the claim, per the
  source hierarchy in `unused-access-expert`.

## Workflow

1. **Route.** Classify the genre. If nothing fits, say so and name the gap.
2. **Pair.** If the page touches Unused Access, bring in `unused-access-expert` and read its
   knowledge base before drafting - not after, when the prose is already committed to a shape.
3. **Read.** The routed template, then the style guide. Keep the glossary open.
4. **Gather.** Pull inputs from the conversation; list assumptions and gaps rather than filling them.
5. **Draft.** Follow the template's section order, apply the style rules, use the placeholder
   conventions.
6. **Ground terms.** Check every named thing against the glossary; apply its casing and usage
   guidance. Flag what neither the glossary nor the knowledge base confirms.
7. **Check.** Run the publish-readiness checklist in `references/style-guide.md`. List what is still
   open - missing screenshots, unconfirmed links, terms to verify, unreleased content.
8. **Hand over.** Present the draft in Markdown with the open-items section intact. Publishing is the
   writer's separate, deliberate step: this skill produces drafts, and a draft that publishes itself
   removes the review that makes the pipeline trustworthy.

## Notes on judgment

- **Reuse sibling conventions** - heading names, table column order, screenshot placement - over
  introducing new ones. Consistency across a page family is worth more than local cleverness.
- **When source material is thin, ship a clean skeleton with explicit placeholders** rather than
  padding it with invented specifics. The skeleton plus honest gaps is a usable draft; the padded
  version is a liability that reads as finished.
- **The routing decision and the pairing decision are the highest-value judgments here.** Getting
  the genre wrong wastes a draft. Guessing facts instead of pairing with the expert skill publishes
  something wrong.

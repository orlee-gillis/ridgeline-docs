# UAX-2841 review

Written against the Jira story alone, before any draft of the page existed.

- `[mine]` - found in that first read
- `[added]` - found in a second pass, with my published pages open next to the story

This file is committed before the draft. The commit dates show which came first, so the order is
checkable rather than something I have to claim.

**Status note:** the story is In Review. Rollback is In Progress and the re-consent banner is To Do.
Nothing here has shipped, so anything drafted from this story carries `[UNRELEASED]` until the status
changes.

---

## Contradicts a published page

Both of these mean something already live on the site becomes wrong.

| Contradiction | Published page says | Story says |
|---|---|---|
| **Scope preservation** `[mine, reclassified]` | *"Scope is never narrowed. The replacement applies at the grant's original scope."* - Access tab page | An applied remediation *can* narrow scope, if the user chooses a tighter one. M. Bell, 29 Jul |
| **Platform permissions** `[added]` | *"Unused Access requires no additional platform permissions. It reuses the permissions granted when each integration was connected."* - report page | Write access is now required, to modify role definitions and assignments |

The scope one is the more serious. A reader who has internalised an absolute guarantee and then
narrows scope by accident was misled by the documentation.

## Missing

| Gap | |
|---|---|
| Safety window has no stated duration | `[mine]` |
| The in-scope section is incomplete - reads as a list that stopped rather than a boundary | `[mine]` |
| Partial failure and the safety window are two different mechanisms with one name between them. M. Bell says so, the PM defers it | `[added]` |
| Success state is a toast with no summary of what changed, and the summary is explicitly out of this release | `[added]` |
| Inherited grants are internally contradictory - the description says TBD, the acceptance criteria list them as required | `[added]` |

## Ambiguous

| Item | |
|---|---|
| Final terminology unsettled - one-click remediation, apply flow, Apply, guided apply | `[mine]` |
| JIT position raised twice and never answered. Not documentable either way until someone decides | `[mine]` |
| *"Without write permission everything else still works and Apply is unavailable"* - unclear what the reader sees. Disabled, hidden, or absent | `[mine]` |
| Limits section gives a number with no reasoning, and the enterprise exception is undecided | `[mine]` |
| *"Handles failure gracefully"* as an acceptance criterion is not testable and not documentable | `[mine]` |
| *"One grant at a time"* is a UI constraint, not a product one - the API accepts a list. Changes how the limit should be phrased | `[added]` |

## Routing questions

Not content gaps - these decide who to ask and who else needs to know.

- Which team owns this in the tracker `[mine]`
- Which customer-facing team needs briefing, for example Customer Success `[mine]`
- Whether this is a new page or a section on the existing Access tab page - the story leaves it to
  the writer `[mine]`

## What I would ask the PM first

1. Does an applied remediation narrow scope? If yes, the published guarantee has to change, and that
   is a bigger edit than this feature.
2. How long is the safety window?
3. What happens on partial failure, and what is it called?
4. Are inherited grants in this release?

---

## What the split shows

*Written by me, in my own words - not drafted.*

My findings all came from reading the Jira story as a document: is it clear, is it decided, is it
testable. Almost all of the added ones came from comparing the story against something else - the
published pages, or the comment thread against the description.

That is not a difference in judgment. It is a difference in what each reader had open. I read the
story cold; the second pass had my published pages alongside it.

The same split showed up in the legacy audit. Reading finds judgment problems. Comparison finds
consistency problems.

**Checklist change:** before finishing a review, check the story against every published page it
touches, and name those pages in the review.

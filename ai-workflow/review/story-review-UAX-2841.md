# UAX-2841 review

A working review of an incoming Jira story - not a customer-facing page. Written from the story
alone, before any draft existed, and committed before the draft so the order is checkable in the
history.

**None of this is available to customers yet.** Status is In Review, rollback is In Progress, the banner is To
Do. Anything drafted from it carries `[UNRELEASED]`.

---

## Findings

Ranked. The first two mean something already published becomes wrong.

| # | Finding | Type | Found by |
|---|---|---|---|
| 1 | **Scope.** Published page: *"Scope is never narrowed."* Story: an applied remediation can narrow it, if the user picks a tighter scope | Contradiction | Writer |
| 2 | **Platform permissions.** Published page: *"requires no additional platform permissions."* Story: write access is now required | Contradiction | Claude |
| 3 | Partial failure and the safety window are two mechanisms with one name between them. Raised in a comment, deferred | Missing | Claude |
| 4 | Safety window has no stated duration | Missing | Writer |
| 5 | Inherited grants: the description says TBD, the acceptance criteria list them as required | Missing | Claude |
| 6 | Success state is a toast with no summary of what changed - and the summary is out of this release | Missing | Claude |
| 7 | The in-scope section reads as a list that stopped, not a stated boundary | Missing | Writer |
| 8 | Terminology unsettled - one-click remediation, apply flow, Apply, guided apply | Ambiguous | Writer |
| 9 | JIT position raised twice, never answered. Not documentable either way | Ambiguous | Writer |
| 10 | *"Without write permission... Apply is unavailable"* - unclear whether it is disabled, hidden, or absent | Ambiguous | Writer |
| 11 | Limits give a number with no reasoning, and the enterprise exception is undecided | Ambiguous | Writer |
| 12 | *"Handles failure gracefully"* is not testable and not documentable | Ambiguous | Writer |
| 13 | *"One grant at a time"* is a UI constraint, not a product one - the API accepts a list | Ambiguous | Claude |

## What happens with each finding

| | |
|---|---|
| **Ask the PM before drafting** | Findings 1, 3, 4, 5 |
| **Draft with a `[VERIFY]` flag** | The rest |
| **Raise with the team** | Which team owns UAX-2841, so the questions above have somewhere to go. And a warning: a published page states that no additional platform permissions are required, so it becomes wrong on the day version 4.7 reaches customers. I need that release date so the page is corrected before 4.7 goes out, and someone needs to confirm support has been told |
| **My call** | Whether this becomes a new page or a section on the Access tab page |

---

## Why Claude found things I didn't

| How the problem was found | Writer | Claude |
|---|---|---|
| Reading the story on its own | 10 | 1 |
| Comparing the story to another document | **0** | **5** |

The zero is the finding. Claude's five comparisons were:

| Story compared with | What it showed | Count |
|---|---|---|
| My published pages | The story describes behaviour those pages say cannot happen | 2 |
| The story's own description | A comment records a decision, and nobody updated the description to match | 3 |

Both are comparisons I could have made and did not. A step I skipped, not a judgment I got wrong -
and the same thing happened in my legacy audit.

---

## My checklist for reviewing an incoming Jira story

Steps 6 and 7 are new, from this review.

1. Read the story once through without taking notes
2. List what is unclear, undecided, or untestable
3. Read the comment thread separately - decisions live there, and the description goes stale
4. Compare the acceptance criteria with the description and look for contradictions between them
5. Separate content gaps from routing questions
6. **Compare the story with every published page it touches, and name those pages here**
7. **List any contradiction with a published page at the top of the findings, and label it a contradiction** - it means a page that is live now becomes wrong, which is more urgent than a gap in the story
8. Mark what must be answered before drafting, and what can go into the draft flagged
# `apply-a-remediation.md` - proposed structure

## Current order

| # | Heading | Level |
| --- | --- | --- |
| 1 | Who this is for | h2 |
| 2 | Prerequisites | h2 |
| 3 | How applying a remediation works | h2 |
| 4 | What Ridgeline changes | h3 |
| 5 | Scope | h3 |
| 6 | Reverse an apply | h3 |
| 7 | When an apply fails | h3 |
| 8 | What you can do | h2 |
| 9 | Limits and known gaps | h2 |
| 10 | Related | h2 |

## Proposed order

| # | Heading | Level | Form |
| --- | --- | --- | --- |
| 1 | What you need | h2 | What you ... |
| 2 | What you can do | h2 | What you ... |
| 3 | How an apply runs | h2 | How / when |
| 4 | How the role changes | h3 | How / when |
| 5 | How to narrow a grant's scope | h3 | How / when |
| 6 | How to reverse an apply | h3 | How / when |
| 7 | When the change appears | h3 | How / when |
| 8 | Limits and known gaps | h2 | Template |
| 9 | Related | h2 | Template |

"Who this is for" is removed as a heading. Its one remaining sentence moves into the opening paragraphs,
which is where the template puts unheaded orientation.

## What changes, and why

| Change | Reason |
| --- | --- |
| "What you can do" moves above the mechanism | The reader needs to know what can be applied before how an apply runs |
| "What Ridgeline changes" is renamed "How the role changes" | The old heading does not name its subject. The section covers custom-role edits and built-in role substitution |
| Scope is lifted out of that section and renamed "How to narrow a grant's scope" | Ridgeline does not change scope; the reader selects it. A heading naming Ridgeline as the actor asserts the opposite of the guarantee, and headings are what a reader scans |
| "Reverse an apply" is renamed "How to reverse an apply", stays h3, and stays prose | The story describes the reversal window as part of the apply flow - preview, confirm, write, then a window in which the change can be rolled back. It is the last phase of one lifecycle, not a separate topic. It stays prose rather than becoming a note, because the 24-hour window decides how carefully a reader reviews before selecting **Apply** - `style-guide.md`, Notes and warnings |
| Role, scope, reversal, and timing become h3 under "How an apply runs" | Eleven headings at one level is a list, not a hierarchy. Four of them are aspects of a single apply. The parent heading does not name Ridgeline as the actor, so the scope heading stays accurate beneath it |
| "Prerequisites" is renamed "What you need" | Pairs with "What you can do" as the page's opening two sections, and states the key concept. A second deviation from `feature-overview.md` - track it with the first |
| "When an apply fails" moves to a second page, `troubleshoot-applying-a-remediation.md` | Error reference is a different genre with a different reader task, reached by searching an error rather than by reading an overview. Splitting now rather than later avoids restructuring, re-pointing links, and renumbering the sidebar twice |
| The data-refresh fact gets its own h3, "When the change appears" | Currently mid-paragraph and unfindable by scanning. It is the answer to "why has my change not appeared" |
| "Who this is for" is removed as a heading and its content moves into the opening paragraphs | "This" is ambiguous - the page or the feature - and the heading addresses the document rather than its subject, which no other heading on the page does. Once the invented authority claim is cut, one sentence remains, which is too little to carry a heading |
| "Related" is kept | Required by `feature-overview.md`, and it is the page's only route to the report and Access tab pages |
| A mechanism section is retained as "How an apply runs" | The five-step sequence, the confirmation step, and the history record need a home. Removing the section leaves them unplaced |

## Heading levels

Every heading is h2 or h3, and no level is skipped. `markdownlint-cli2` blocks a skipped level, so an h4
directly beneath an h2 fails the build.

## Heading form

Three groups, each internally consistent:

| Group | Form | Why it is fixed |
| --- | --- | --- |
| Template headings | As written in `feature-overview.md` | Changing them breaks consistency with every sibling page in the family |
| The opening pair | "What you need", "What you can do" | Parallel with each other, and each states the key concept of its section |
| Headings for behaviour and reader actions | "How ..." or "When ..." | Matches the explanatory register of a feature overview. "How to ..." names the reader as the actor without stating it, which is what keeps the scope heading accurate |
| Troubleshooting and Write failures | Section labels | Conventional labels readers scan for, in the same class as Prerequisites |

Rejected: gerunds ("Choosing a narrower scope", "Reversing an apply"). They read as procedure headings, and
"When the change appears" has no gerund form, so the set could not be made uniform.

## "Who this is for" and "Prerequisites"

Both sections currently mix three separate access questions. Separating them:

| Layer | What it governs | Section it belongs in | Status |
| --- | --- | --- | --- |
| The reader's role in Ridgeline | Whether this person can select **Apply** | Prerequisites | Not documented. UAX-2841 does not say |
| Ridgeline's platform permissions | Whether Ridgeline can write the change to the platform | Prerequisites | Documented |
| The integration's role and its scope | What the apply changes | "How the role changes" and "How to narrow a grant's scope" | Documented |

**"Who this is for" - what changes.** Removed as a heading; see above. The current text also claims that
reading a recommendation and applying one are separately gated levels of authority. UAX-2841 does not say
that. It says Ridgeline needs an additional platform permission, which is a statement about Ridgeline's
access, not the reader's. Cut the claim. The section then states the reader's job only: who is accountable
for reducing an integration's access.

**"What you need" - what changes.** Renamed from "Prerequisites". Restructure as one table, one row per
layer, so a reader who cannot select **Apply** can tell which layer is stopping them:

| Requirement | Detail |
| --- | --- |
| The reader's role in Ridgeline | `[VERIFY: which role can select Apply - UAX-2841 does not say]` |
| Ridgeline's platform permissions | Read, plus permission to change role definitions and the grants that attach roles. Granted at connection time, or by re-consenting an existing connection |
| The grant | **Platform** category, assigned directly to the integration, and carrying a recommendation |

## New open question

| Question | Owner | Blocking |
| --- | --- | --- |
| Which role in Ridgeline can select **Apply**? A write path with no documented actor permission leaves the reader unable to tell whether they are blocked by their own role or by a missing platform permission | D. Reyes, PM | Yes |

## Terminology decision needed

The three layers above are a role-based access control model, and naming it that way would let one
sentence carry what currently takes a paragraph. "Role-based access control" and "RBAC" are not in
`glossary.md`, and `style-guide.md` prohibits inventing abbreviations for names that do not have one.
Decide whether the term enters the glossary before it enters a page. Using it in internal notes is not
affected.

## For later: the same heading in the template

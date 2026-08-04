# Audit checklist - required sections by page type

What each page genre must contain to do its job. A missing required section is **should-fix**. A missing
safety statement is **blocker**.

Cite this file as the source when reporting a genre problem, naming the page type - for example
`audit-checklist.md, report page`.

---

## Report page

A page about one report, read by someone looking at that report now.

| Required | Why it is required |
| --- | --- |
| What puts a row in the report | Every column reads differently depending on the unit of the row. Without this, no column can be interpreted |
| What is excluded | A reader hunting for something absent files it as missing data |
| How the report is ordered, and the metric behind it | Otherwise the reader cannot tell whether the top row deserves attention |
| What an empty or null value in the sort metric means | An unexplained blank reads as a defect |
| A column table | |
| What to do with a finding | Without it, a prioritization report has done half its job |
| Data freshness | Answers "why has my change not appeared" |

Order matters: inclusion criteria before columns. Reversed, the reader meets the columns without knowing
what a row is.

## Investigation surface page

A page about a tab, panel, or card where a reader investigates one thing.

| Required | Why it is required |
| --- | --- |
| Orientation - what the surface is for, and what decision the reader is here to make | A reader arriving from a report needs to know why they are here before what is on screen |
| What each part of the surface shows | |
| How to read the primary view, not only what its elements are named | An element glossary does not tell a reader how to reach a decision |
| The action the surface leads to | |
| Any guarantee attached to a recommendation | **blocker** if absent. A reader may act on the recommendation |

## Hub page

A page whose job is to route a reader to child pages.

| Required | Why it is required |
| --- | --- |
| What the area covers, in one or two sentences | A hub that opens with a bare list of links orients nobody |
| One line per child page saying what it answers | Link titles alone do not tell a reader which to open |
| Where to start | A hub with no recommended entry point makes the reader choose blind |

A hub page of only links and no orientation fails its genre even when every sentence in it is correct.
This is the most commonly missed genre requirement, because nothing in the page is wrong.

## Reference page

Tables of values, read by lookup rather than start to finish.

| Required | Why it is required |
| --- | --- |
| Complete value sets | A partial table reads as exhaustive and misleads silently. Flag any set you could not complete |
| One heading per field or field group | Lookup depends on the anchor and the search result landing on the right row |
| Behavioural consequences in the table, not in a note below it | A reader scanning one row does not read the note |

## Any page type

| Required | Severity if missing |
| --- | --- |
| Every classification the page names has its consequence stated | **blocker** |
| Every column or label the page names is explained somewhere | should-fix |
| Every term matches the glossary's "use in copy" form | Left to Vale - do not report |

---

## Order-of-sections test

For any genre, ask: does the section order follow the reader's task, or the interface's layout?

An interface-ordered page moves panel, then summary, then primary view, then secondary view - the order
things appear on screen. A task-ordered page moves orientation, then decision inputs, then the decision,
then the action.

Interface order is not automatically wrong. It is wrong when the reader's task runs in a different
sequence, and the page never says so. Report as **should-fix** with the class *(order)*, and say which
sequence the page follows.

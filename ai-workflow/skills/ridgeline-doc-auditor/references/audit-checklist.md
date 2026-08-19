# Audit checklist - required sections by page type

What each page genre must contain to do its job. A missing required section is **should-fix**. A missing
safety statement is **blocker**.

Cite this file as the source when reporting a genre problem, naming the page type - for example
`audit-checklist.md, parent-report`.

**Genre names match the `template:` frontmatter value the page declares** (`parent-report`,
`child-report`, `workflow-methodology`) - the same tag `validate-parent-report.py`,
`validate-child-report.py`, and `validate-workflow-methodology.py` key off. A page with no `template:`
tag isn't audited against any genre here; it only gets the general advisory review.

---

## parent-report

A page introducing a report or feature as a whole, read by someone deciding whether and how to use it.
Real example: `docs/unused-access-report.md`.

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

## child-report

A page about a tab, panel, or card where a reader investigates one thing within a parent-report's
feature. Real example: `docs/about-the-access-tab.md`.

| Required | Why it is required |
| --- | --- |
| Orientation - what the surface is for, and what decision the reader is here to make | A reader arriving from a report needs to know why they are here before what is on screen |
| What each part of the surface shows | |
| How to read the primary view, not only what its elements are named | An element glossary does not tell a reader how to reach a decision |
| The action the surface leads to | |
| Any guarantee attached to a recommendation | **blocker** if absent. A reader may act on the recommendation |

## workflow-methodology

A page walking through how to carry out one action from start to finish - what it takes to begin, what
happens at each stage, and where it stops short. Real example: `docs/apply-a-remediation.md`.

| Required | Why it is required |
| --- | --- |
| Prerequisites - what must be true before the workflow can be started | A reader who doesn't meet them needs to know before attempting, not after failing |
| What you can do - the scope of the workflow, stated plainly | Without it, a reader can't tell whether this workflow covers their situation |
| The mechanics, in the order they actually happen | A reader trusts the outcome only if they understand how it was produced |
| Any guarantee attached to a hard-to-reverse or destructive step | **blocker** if absent - a reader may act on the workflow without knowing what it can't undo |
| Limits and known gaps | A reader who over-trusts an incomplete workflow makes worse decisions than one who read nothing |

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

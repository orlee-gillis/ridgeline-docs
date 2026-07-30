---
name: ridgeline-doc-auditor
description: Audit a finished Ridgeline documentation page and report what is wrong with it - genre fit, section order, facts asserted without a source, undefined terms, cross-page inconsistency, and whether the page serves the reader's task. Returns a ranked list of problems, each with a source line, plus a judgment on the page's purpose. Use whenever the user wants a page reviewed, audited, assessed, or checked, hands over a finished page and asks what is wrong with it, or says things like "review this page", "what's wrong with the report page", or "audit these two articles". Trigger even if the user only pastes a page and asks for an opinion. Does NOT draft or rewrite - approved problems go to ridgeline-doc-writer. Does NOT check punctuation, banned words, casing, or frontmatter presence, which Vale and the build already enforce. For Unused Access facts, pairs with unused-access-expert.
---

# Ridgeline documentation auditor

Audits a finished page. Does not write one.

This skill exists because auditing and drafting are different jobs, and a drafting skill asked to audit
returns an unbounded, unranked list. Everything below is an output constraint as much as a method.

## What this skill does not check

Declare this in every audit, so nobody reads the result as complete:

| Not checked here | Enforced by |
| --- | --- |
| Banned terms, Latin abbreviations, "please", curly quotes | `vale`, blocking on pull request |
| Required frontmatter fields | CI script |
| Skipped heading levels, malformed tables | `markdownlint-cli2` |
| Dead links and anchors | The Docusaurus build |
| Glossary copies matching upstream | CI diff step |

Re-checking any of these produces noise, not findings. If a gate is not yet live for one of them, say so
and still leave it out - the fix is to turn the gate on, not to audit by hand forever.

## What this skill checks

1. **Genre fit.** Does the page have the sections its type requires? See
   `references/audit-checklist.md`.
2. **Section order.** Does the order serve a reader working through a task, or does it follow the
   interface's layout?
3. **Facts asserted without a source.** Any claim about product behavior that no reference supports.
   For Unused Access, pair with `unused-access-expert` and cite its knowledge-base section.
4. **Unstated safety guarantees.** A page naming a classification or a remediation must state the
   guarantee attached to it.
5. **Terms used but never defined.** A column or label the page names and never explains.
6. **Cross-page inconsistency.** The same thing called two different names across pages in scope.
7. **Purpose.** Mandatory, and answered last - see below.

## Output format

Return exactly these three parts, in this order.

### Part 1 - Purpose

Two sentences per page, always, even when there are no other problems:

> **What this page is for:** ...
> **Does it do that:** ...

This is the only judgment in the audit that no gate can replace, so it goes first and is never omitted.
If the page's purpose cannot be stated in one sentence, that is itself the finding.

### Part 2 - Problems

| # | Problem | Severity | Source | Where on the page |
| --- | --- | --- | --- | --- |

Rules, all binding:

- **Maximum 20 rows per page.** If more exist, report the 20 highest-severity and state how many were
  omitted.
- **Every row needs a source** - the file and section that establishes the rule or fact, for example
  `knowledge-base.md §8` or `audit-checklist.md, report page`. **If you cannot cite one, do not report
  the problem.** A problem with no source is either a preference or an invention.
- **Sort by severity**, blockers first.
- **Group by class.** Mark each row's class in the Problem cell: *(fact)*, *(genre)*, *(order)*,
  *(term)*, *(consistency)*.

### Part 3 - Not checked

One line listing the classes above that were left to the gates, so the reader knows the audit's edges.

## Severity

| Severity | Means | Examples |
| --- | --- | --- |
| **blocker** | Factually wrong, or a safety guarantee is missing. A reader could act on this and be harmed | A sort order described in terms of the wrong entity; a page naming Undetermined without stating it is treated as used |
| **should-fix** | The page fails its genre or leaves a term undefined. The reader is not harmed but cannot finish the task | No section telling the reader what to do with a finding; a column named and never explained |
| **optional** | A preference with a defensible alternative | Section could be split; a table might read better as a list |

If a problem does not fit one of these, it is not a problem this skill reports.

## Method

1. Identify the page's genre. If none of the types in `references/audit-checklist.md` fits, say so and
   audit only for facts, terms, and purpose - do not invent a genre standard.
2. For Unused Access content, load `unused-access-expert` and read its knowledge base before judging
   any factual claim. Do not judge facts from memory.
3. Work the seven checks in order. Collect problems as you go, with a source for each.
4. Answer purpose last, once you have read the whole page, then put it first in the output.
5. Before returning: delete every row with no source. Count rows, cap at 20, sort by severity.

## What to do with the result

Hand the problem list to the reader for approval or rejection. Rejections are expected and are part of
the record - an audit whose every row is accepted has probably reported preferences as rules.

Approved problems go to `ridgeline-doc-writer` for the rewrite. This skill never rewrites the page
itself: the same pass that decides what is wrong should not also decide what replaces it, or the
judgment and the draft become impossible to review separately.

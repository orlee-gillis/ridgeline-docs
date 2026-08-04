# Audit - `apply-a-remediation.md` (flagged draft)

Run with `ridgeline-doc-auditor`, paired with `unused-access-expert`.

**Genre note.** `audit-checklist.md` has no entry for the feature-overview genre. Its four genres are
report page, investigation surface page, hub page, and reference page. Per the skill's method, a genre
with no checklist entry is not audited against an invented standard, so genre findings below cite
`feature-overview.md` (the drafting template) instead. The missing checklist entry is itself a gap - see
the note at the end.

## Part 1 - Purpose

**What this page is for:** A reader who has a remediation recommendation in front of them and wants to
know whether Ridgeline can carry it out, what it will change, and how to undo it.

**Does it do that:** Yes for the facts, no for the shape. Every fact the reader needs is present, but the
capability list sits below the full mechanism, and two post-apply states are nested inside the section
describing how an apply runs.

## Part 2 - Problems

| # | Problem | Severity | Source | Where on the page |
| --- | --- | --- | --- | --- |
| 1 | *(genre)* "What you can do" repeats four facts already stated above it: Platform grant only, scope selection, 24-hour reversal, history. The template intends this section to route to pages that cover each action in full; there are no such pages, so it became a summary | should-fix | `feature-overview.md`, "What you can do" | `## What you can do` |
| 2 | *(order)* Section order presents the mechanism before the capability list. The order-of-sections test asks for orientation, then decision inputs, then the decision, then the action - the reader meets the two-write sequence, the role logic, and the failure states before learning what can be applied at all | should-fix | `audit-checklist.md`, order-of-sections test | Sections 3 to 8 |
| 3 | *(order)* "Reverse an apply" and "When an apply fails" are subsections of "How applying a remediation works". Both describe states that exist after an apply has run, not steps within one | should-fix | `audit-checklist.md`, order-of-sections test | `### Reverse an apply`, `### When an apply fails` |
| 4 | *(term)* "What Ridgeline changes" does not name its subject. The section is about how the role is rewritten - custom role edited, built-in role substituted | should-fix | `style-guide.md`, Structure and headings | `### What Ridgeline changes` |
| 5 | *(term)* "an apply" is used as a countable noun throughout and is not in the glossary. The page flags the feature's name as unverified but not this | should-fix | `ridgeline-doc-writer/SKILL.md`, Two kinds of unverified content | Throughout |
| 6 | *(order)* The data-refresh fact - an applied change appears in the report after the nightly run - sits mid-paragraph inside the mechanism section with no heading. It is the answer to "why has my change not appeared" and is unfindable by scanning | optional | `style-guide.md`, Structure and headings | `## How applying a remediation works` |

Six rows, none omitted.

**Checked and clean:** the Undetermined guarantee is stated where the role change is described, and no
sentence leaves open that an undetermined right might be removed (`knowledge-base.md` §8). Scope is
attributed correctly - Ridgeline preserves it, the reader may reduce it (§9, invariant 1, as amended by
the SME answers). Usage data is attributed only to Platform grants (§7). Every template section is
present.

## Part 3 - Not checked

Banned terms, Latin abbreviations, curly quotes, frontmatter fields, skipped heading levels, malformed
tables, dead links and anchors, and glossary copies matching upstream - all left to Vale,
markdownlint-cli2, the Docusaurus build, and the CI diff step.

Two of those gates do not exist yet: the glossary diff step, and any Vale rules in `styles/Ridgeline/`.
Per the skill, the fix is to turn the gate on, not to audit those classes by hand.

## Gap found in the auditor itself

`audit-checklist.md` defines required sections for four genres. `ridgeline-doc-writer` routes to three
templates, one of which - feature overview - has no checklist entry. Any page drafted from that template
therefore has no genre standard to be audited against, and a missing or misplaced section in it cannot be
reported as a genre finding.

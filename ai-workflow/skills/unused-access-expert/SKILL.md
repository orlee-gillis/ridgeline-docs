---
name: unused-access-expert
description: Subject-matter expert on Ridgeline's Unused Access feature - the Unused Access report in the Access Center, the integration card Access tab (grant graph and grant table), Used/Unused/Undetermined usage classification, access grant concepts (Direct and Inherited, Platform/Directory/App-level categories, JIT grants, the scope ladder), and the least-privilege remediation engine. Use whenever a task needs Unused Access facts to be right - answering how integrations are prioritized, how usage is measured, how the graph, table, or remediation behaves, or supplying subject-matter accuracy to a page being drafted, reviewed, or audited. Trigger even if the request only says "Unused Access", "unused grants", "least privilege", "Access tab", "access grant", "JIT", "Reach score", or names a feature note. This skill supplies accuracy, not page structure - for genre, template, and style, pair with ridgeline-doc-writer, which owns the drafting.
---

# Unused Access feature and methodology expert

This skill makes you an accurate subject-matter expert on Ridgeline's **Unused Access** feature, so
that documentation about it is factually right and its safety guarantees are never blurred. It
covers the Unused Access report in the Access Center, the integration card **Access** tab as the
investigation surface, the Used/Unused/Undetermined usage model, access grant concepts, and the
least-privilege remediation engine - including internal engine mechanics that must inform answers
but never reach a published page.

It carries facts and judgment, not page structure. Pair it with `ridgeline-doc-writer` (or a more
specialized genre skill) whenever the output is a page.

## Read the references first

The sourced facts live in the bundled references. Pull from them rather than from intuition -
Unused Access has several plausible-sounding wrong answers, and fluent confidence is the failure
mode this skill exists to prevent.

- `references/knowledge-base.md` - the Unused Access facts, numbered by section and sourced per
  section. **Read before writing or reviewing anything substantive.** Snapshot date is in §13.
- `references/glossary.md` - the Ridgeline terminology authority (Definition / Use in copy / Avoid
  per term). Check every feature, surface, metric, and concept name against it before writing it.

### The three sections with the highest error risk

- **§8 - Usage classification.** Undetermined is not Unused. Undetermined rights are ones the
  activity logs cannot audit, and the engine strictly treats them as Used, so they are never
  removed. Conflating the two, or implying remediation might strip an undetermined right,
  misrepresents the feature's core safety guarantee. This is the most damaging error possible here.
- **§7 - Category asymmetry.** Only **Platform** grants get scopes, accessible services, and full
  usage analysis. **Directory** and **App-level** grants get posture-based or best-practice
  guidance, because their usage is not log-correlated. Attributing usage data to them is wrong in a
  way that reads as correct.
- **§9 - Remediation invariants.** Scope is preserved and team membership is preserved, always.
  Inherited-grant remediation analyzes every team member's usage so no active member loses access.
  Never describe a remediation as narrowing scope or removing anyone from a team.

## Source hierarchy - what wins when sources conflict

Ridgeline's upstream sources are the published pages in `docs/` and the dated feature notes in
`ai-workflow/inputs/`. They disagree often, and which one is authoritative depends on the note's
status, not on the fact that one is published:

| Rank | Source | Condition | Rule |
| --- | --- | --- | --- |
| 1 | Verified product behavior | Always | Beats every document |
| 2 | Published page in `docs/` | The relevant feature note is **Shipped** | The page is the current, reviewed statement - prefer it |
| 3 | Feature note in `ai-workflow/inputs/` | The note is **In development** | The note is newer than the page - prefer it, and flag the content `[UNRELEASED]` |
| 4 | `knowledge-base.md` | Always | Authoritative for behavior the two above do not settle; check §13 for the snapshot date |
| 5 | Feature note marked **Planned** | Always | Historical or speculative context only - never write it as current behavior |

A note that has not shipped describes behavior a reader cannot see yet, so anything sourced from it
carries `[UNRELEASED]` until the note flips to Shipped. If a published page and a Shipped note
disagree, the page has probably gone stale: flag the discrepancy rather than silently picking one.

## Guardrails, and why each exists

- **Name things exactly.** The report is the **Unused Access report**; the card surface is the
  **Access** tab. "Unused Access" is never abbreviated - the feature deliberately has no acronym.
- **Hold the internal boundary.** The engine configuration flags, the internal data model, and the
  API surface (§10) are engineering facts. Use them to answer behavior and support questions
  accurately; never publish them on a page for readers.
- **The 90-day window is a default, not a law.** Write "by default, 90 days." The threshold is
  configurable internally.
- **The graph has a display condition** (§5). Omitting it produces "where is my graph" questions.
- **Nested teams are hidden deliberately.** Only the team holding the direct assignment appears,
  because that is where remediation happens (§7). Describe it as design, not as a limitation.
- **Access right counts are scope- and inventory-relative** (§5). The same role at two scopes
  legitimately shows different counts. Never present a count as the role definition's absolute size.
- **Usage on deleted resources counts as usage** (§6). It is deliberate, so create-use-delete
  workflows keep the access they need. Never call it noise to filter out.
- **Access risk, not integration posture** (§1). Unused Access covers integrations holding
  excessive access; stale credentials and unreviewed external integrations are a different pillar.
  Do not blur them.
- **Reach score drives sorting, and Unused Access has no score of its own** (§3). Connect
  prioritization to the existing score vocabulary rather than inventing a feature-specific score. A
  null Reach score means no scenarios are defined, not a bug.
- **Ridgeline needs no additional platform permissions** to run Unused Access - it reuses what was
  granted at connection time (§11). Readers ask constantly; state it proactively in overviews.
- **Data refreshes daily** (§3). Recent platform-side changes appear after the next run.

## Working with feature notes

When the knowledge base does not settle a question, read the feature notes in
`ai-workflow/inputs/`. Each note carries a `status:` field (`Planned`, `In development`, `Shipped`)
and a date - both are load-bearing for the hierarchy above, so read them before reading the body.

Fold confirmed answers back into `knowledge-base.md` in the same session, with the source and date,
so the next task does not re-litigate a settled fact.

## Known gaps

Open questions live in `knowledge-base.md` §12 - the Highly privileged label's definition, the CSV
column set, and whether the 90-day window is reader-configurable. When one surfaces, say it is
unconfirmed and flag it for SME verification rather than answering definitively. A flagged gap costs
one review cycle; a fluent guess in a security product costs trust.

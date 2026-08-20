---
name: unused-access-expert
description: Subject-matter expert on Ridgeline's Unused Access feature — the report, the Access tab investigation surface, access grant concepts, usage classification, and remediation behavior. Supplies factual accuracy for documentation. Pair with doc-writer for drafting.
---

# Unused Access expert

This skill makes you an accurate subject-matter expert on Ridgeline's **Unused Access** feature, so documentation about it is factually right and its safety guarantees are never blurred.

It carries facts and judgment, not page structure. Pair it with `doc-writer` whenever the output is a page.

## Read the references first

The sourced facts live in the bundled references. Pull from them rather than from intuition — Unused Access has several plausible-sounding wrong answers, and fluent confidence is the failure mode this skill exists to prevent.

- **Knowledge base:** https://github.com/orlee-gillis/ridgeline-docs/blob/main/ai-workflow/skills/unused-access-expert/references/knowledge-base.md — Unused Access facts, numbered by section and sourced. **Read before writing or reviewing anything substantive.** Snapshot date is in §8.
- **Glossary:** https://github.com/orlee-gillis/ridgeline-docs/blob/main/ai-workflow/skills/unused-access-expert/references/glossary.md — the terminology authority (Definition / Use in copy / Avoid per term). Check every feature, surface, metric, and concept name against it.

## High-risk sections

These sections have the highest error risk - read them in full in `knowledge-base.md` before
writing or reviewing anything that touches them, rather than relying on a summary here:

- **§3 - Usage classification.** The most damaging error possible if conflated.
- **§2 - Category asymmetry.** Wrong in a way that reads as correct if misattributed.
- **§6 - Remediation invariants.** Never describe remediation as narrowing scope or removing anyone
  from a team.

## Source hierarchy — what wins when sources conflict

| Rank | Source | Condition | Rule |
| --- | --- | --- | --- |
| 1 | Verified product behavior | Always | Beats every document |
| 2 | Published page in `docs/` | Feature note is **Shipped** | Page is current and reviewed — prefer it |
| 3 | Feature note in `ai-workflow/inputs/` | Note is **In development** | Note is newer — prefer it, flag as `[UNRELEASED]` |
| 4 | `knowledge-base.md` | Always | Authoritative for behavior the two above do not settle |
| 5 | Feature note marked **Planned** | Always | Historical/speculative only — never write as current behavior |

Content sourced from a note that has not shipped carries `[UNRELEASED]` until it ships.

## Guardrails for accuracy

- **Name things exactly.** The report is the **Unused Access report**; the card surface is the **Access** tab. "Unused Access" is never abbreviated.
- **Hold the internal boundary.** Engine configuration, internal data model, and API surface inform your answers but never reach a published page.
- **Surface unconfirmed questions.** If the knowledge base does not settle a question, flag it as `[VERIFY: ...]` rather than answering definitively. A flagged gap costs one review cycle; a fluent guess costs trust.
- **Preserve safety guarantees.** Misrepresenting a safety guarantee is the highest-risk error.

## Workflow

1. **Read the knowledge base** (§1-8) before answering anything substantive about Unused Access
2. **Check the glossary** before writing any term
3. **Apply the source hierarchy** if sources conflict
4. **Surface unconfirmed questions** rather than guessing
5. **Pair with doc-writer** if the output is a page

## Known gaps

See `knowledge-base.md` §7 for open questions. When they surface in your work, flag them as `[VERIFY: ...]` and list them in the page's "Open items for SME review" section.

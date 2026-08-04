# AI-assisted authoring

The four stages from source material to published page: the AI techniques used at each, what each technique
is for, and the file that holds it. Lessons are listed separately, because not every technique taught me
something.

---

## Stage 1 - Gathering the source material

Folder: `ai-workflow/inputs/`

### Techniques used

| Technique | What it is for | Where it lives |
| --- | --- | --- |
| Ranked source hierarchy | Decides which document wins when two disagree, so the choice is not remade on every page | `skills/unused-access-expert/SKILL.md` |
| Knowledge base numbered by section | Lets a draft cite `§8` instead of asserting, so a reader can check the claim | `skills/unused-access-expert/references/knowledge-base.md` |
| List of unanswered questions | Stops an unsettled fact being closed by a plausible sentence | `knowledge-base.md` §12 |
| Status field on the source file | Produces an `[UNRELEASED]` page automatically from the source's own metadata | `inputs/UAX-2841-apply-remediation.md` |

### What I learned

<!-- One or two sentences. Candidate: the decisions were in the story's comment thread, not its
description, and the description had gone stale. A rule for ranking documents does not help when the
contradiction sits inside one document. -->

---

## Stage 2 - Writing the prompt

Folder: `ai-workflow/prompts/`

### Techniques used

| Technique | What it is for | Where it lives |
| --- | --- | --- |
| Prompt saved as a repo file | Makes the drafting instruction repeatable and reviewable instead of disposable | `prompts/uax-2841-drafting.md` |
| Provenance header on that file | Ties the draft to the model, skills, and input files that produced it | `prompts/uax-2841-drafting.md` |
| Written reason for the model choice | Makes a cost-quality tradeoff defensible rather than a default | `conventions.md` |
| Repo instructions for any AI agent | Gives an agent the repo's rules without being told them in chat | `AGENTS.md` |

### What I learned

<!-- What the prompt file makes possible that a chat log does not. -->

---

## Stage 3 - Generating the draft

Folder: `ai-workflow/drafts/`

### Techniques used

| Technique | What it is for | Where it lives |
| --- | --- | --- |
| Flag conventions - `[VERIFY]`, `[SCREENSHOT]`, `[CHILD URL]`, `[UNRELEASED]` | Forces the model to report a gap instead of filling it, and collects every gap in one section | `skills/ridgeline-doc-writer/SKILL.md` |
| Two skills paired, with a written split of responsibilities | Keeps facts and structure separately reviewable, so a wrong fact and a wrong section order are different findings | `ridgeline-doc-writer/SKILL.md` |
| One template per page type | Fixes section order before writing starts, so genre is a decision rather than an accident | `ridgeline-doc-writer/assets/templates/` |
| Glossary with one meaning per term | Keeps a name identical across every page, and records which words are banned | `references/glossary.md` |
| Private list of real-product words | Stops real product vocabulary reaching a public repo | Fictionalization map, practice repo |
| Audit skill with a capped output | Keeps findings ranked and sourced instead of an unbounded list of preferences | `skills/ridgeline-doc-auditor/SKILL.md` |
| Required sections per page type | Defines what a missing section means, so genre problems are reportable | `skills/ridgeline-doc-auditor/references/audit-checklist.md` |

### What I learned

`[VERIFY]` catches what the model reports as unknown. It does not catch a claim the model states
confidently and does not flag. The draft's one factual error - that reading a recommendation and applying
one require different levels of reader permission - carried no flag. Recorded as a third flag category in
`decisions/UAX-2841.md`.

Two skills pointed at files that were never committed: `audit-checklist.md`, and two of three templates. A
skill can name a path that does not exist, and nothing catches it.

---

## Stage 4 - Editing it into the published page

Folder: `docs/`

### Techniques used

| Technique | What it is for | Where it lives |
| --- | --- | --- |
| Publish-readiness checklist | Makes the review repeatable rather than dependent on what I notice that day | `ridgeline-doc-writer/references/style-guide.md` |
| My own problem list written before the audit runs | Tests my judgment against the skill's instead of anchoring on it | `audits/audit-apply-a-remediation.md` |
| Restructure written down separately from the edit | Records reasoning a diff cannot show | `audits/restructure-apply-a-remediation.md` |
| Decision record including rejected suggestions | Shows which AI recommendations were overruled, and why | `decisions/UAX-2841.md` |
| Draft committed at its final path, then edited in a second commit | Makes the editorial change readable as a diff in the pull request | Session 15 branch |

### What I learned

<!-- The split: no facts needed correcting, every structural decision changed. Why, and what it changes
about where review time goes on the next page. -->

---

## Gaps this module exposed

| Gap | Tracked in |
| --- | --- |
| The audit checklist covers four page types. The doc-writer skill routes to a fifth, feature overview, which has no entry - a page built from that template cannot be checked for missing sections | `TODO.md` |
| No template exists for a task page, so a how-to cannot be routed | `TODO.md` |
| The Vale rules in `styles/Ridgeline/` do not exist. The ban on "auto-remediation" and the fictionalization word list are enforced by memory | `TODO.md` |
| `glossary.md` exists as two copies and no CI step compares them | `TODO.md`, `decisions/UAX-2841.md` |
| No CI step checks that the file paths named inside a skill exist | `TODO.md` |

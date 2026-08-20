# Skill architecture

How I structure AI skills for documentation work, and why each decision is the way
it is.

**Scope of this document.** These patterns were developed across fifteen skills, most
of them for a proprietary product whose subject matter is not reproduced here. What
transfers is the architecture, not the content. Every example below points at a skill
in this repo, because a pattern I can only describe is a pattern you have no reason to
believe.

---

## 1. Separate subject-matter accuracy from structure and style

**Problem.** A single skill that knows both the product and the page format will
silently trade one against the other. Asked for a report page, it produces plausible
structure containing invented facts, and there is no seam at which to check either.

**Mechanism.** Two skills, with ownership stated in the skill file rather than implied.
`ridgeline-doc-writer` opens by declaring that it owns structure and style and does not
own subject-matter accuracy. `unused-access-expert` carries the facts and owns nothing
about page shape. Neither can complete a page alone.

The handoff is not a suggestion. The writer skill carries a lookup table mapping
specific questions to specific sections of the expert skill — "does remediation ever
narrow scope?" resolves to a numbered section, not to a general instruction to check.
A pointer with an address gets followed; "consult the expert skill" does not.

**Where it lives.** `ridgeline-doc-writer/SKILL.md` (ownership statement and the
question-to-source table), `unused-access-expert/`.

**Cost.** Two files to maintain, and a fact that changes may need editing in one place
and re-checking in another. Worth it only when the subject matter is deep enough that
guessing is a real risk.

---

## 2. Auditing and drafting are different skills

**Problem.** A skill that drafted a page and is then asked to audit it will rationalize
what it produced. The judgment and the draft become impossible to review separately.

**Mechanism.** `ridgeline-doc-auditor` audits a finished page and does not write one.
It returns a ranked list of problems with a source line for each, plus a judgment on
whether the page serves its reader's task. Approved problems route to the writer skill
as a separate step, which means a human decides which findings are real before any text
changes.

**Where it lives.** `ridgeline-doc-auditor/SKILL.md`.

**Cost.** Two invocations where one felt sufficient, and a manual gate between them.
The gate is the point.

---

## 3. Declare what the skill does not check

**Problem.** Review tooling that overlaps produces duplicate findings, and reviewers
learn to skim all of it. A skill that reports missing frontmatter alongside a genre
misdiagnosis has flattened a trivial problem and a serious one into one list.

**Mechanism.** The auditor carries an explicit table of what it does not check and what
enforces each item instead — banned terms, Latin abbreviations, curly quotes, and
similar all belong to the linter, which blocks on pull request. The skill closes the
category deliberately: if a problem does not fit one of its named types, it is not a
problem this skill reports.

This makes the division of labor between linter, AI review, and human judgment a
written decision rather than an accident of what each tool happened to catch.

**Where it lives.** `ridgeline-doc-auditor/SKILL.md`, "What this skill does not check".

**Cost.** The table goes stale when the linter's rules change. It needs an owner.

---

## 4. Route to a genre before writing anything

**Problem.** One flexible template produces pages that are all slightly wrong. A
navigation hub, a parent-report, a troubleshooting page, and a glossary entry have
different section orders because they answer different questions, and averaging them
serves none.

**Mechanism.** The writer skill classifies the request into a named genre first, then
loads that genre's canonical section order from a template file. Genres it does not own
route to a more specialized skill. Two guardrails matter: do not invent a structure
silently, and do not hand off to a skill that does not exist. The second exists because
a confident handoff to a nonexistent skill produces a convincing dead end.

**Where it lives.** `ridgeline-doc-writer/SKILL.md` (routing), `assets/templates/`.

**Cost.** Adding a genre means adding a template and a routing entry. Genres
proliferate if nobody says no.

---

## 5. State source precedence explicitly

**Problem.** Sources conflict routinely — a template says one thing, the style guide
another, the observed product behavior a third. Without a stated order, the resolution
is whichever source was read most recently.

**Mechanism.** An ordered chain, written in the skill: verified behavior wins, then the
expert skill's knowledge base, then bundled reference material, then the style guide.
Where a bundled reference is known to lag a live source, the skill says which one wins
rather than leaving it to inference.

**Where it lives.** `ridgeline-doc-writer/SKILL.md`, precedence statement.

**Cost.** None worth naming. This is the cheapest pattern here and the one most often
skipped.

---

## 6. Allowlist sources, do not just name them

**Problem.** A skill told to ground its work in a knowledge base will accept adjacent
material that a search happens to return — draft pages, staging content, a superseded
copy. Adjacent material is the most dangerous kind, because it is plausible.

**Mechanism.** Name the permitted source and exclude the near neighbours by name, with
an instruction not to use them even when a search returns one. The exclusion has to be
explicit; "use the official documentation" does not rule out a draft titled identically.

**Where it lives.** Applied throughout the skill set; the mechanism travels without the
source names.

**Cost.** The allowlist needs updating when sources move, and a stale allowlist blocks
legitimate material.

---

## 7. Treat a bundled knowledge base as a dated snapshot

**Problem.** A knowledge base bundled into a skill file is frozen at the moment it was
written, while the product it describes moves. A snapshot that does not announce itself
as one gets treated as current indefinitely.

**Mechanism.** State that the knowledge base is a snapshot, and give it a verification
path — what to do when a task needs current state rather than encoded knowledge. Stamp
it with a date.

**Honest note.** I got the first half of this right and the second half wrong. My expert
skills declared themselves snapshots and named a verification route, but did not carry
dates. That was survivable while live verification was available and became a real
defect the moment it was not. Snapshots need dates, not just disclaimers.

**Cost.** Refresh discipline. A snapshot nobody refreshes is worse than no snapshot,
because it is trusted.

---

## 8. Flag unverified claims in the output, not in the process

**Problem.** A draft containing one confident invention among forty correct statements
is more dangerous than a draft that is visibly incomplete, because nothing marks where
to look.

**Mechanism.** An inline flag — `[VERIFY: ...]` — on any claim the skill could not
ground. The flag ships in the draft, so the reviewer sees it at the point of use rather
than in a summary they may not read. A draft with no flags is a claim in itself: every
statement was grounded.

This is the same finding as the editorial pass logged in this repo's decision records,
where an unflagged confident invention was categorised as its own class of defect
alongside factual error and structural failure.

**Cost.** Only works if flags are honest. A skill that under-flags is worse than one
that does not flag at all.

---

## 9. Progressive disclosure: SKILL.md plus references

**Problem.** Everything a skill knows cannot be in front of the model at once, and the
material a skill needs varies by task.

**Mechanism.** A short `SKILL.md` carrying the decision logic — routing, ownership,
precedence, what not to do — plus reference files loaded when the routed task needs
them: a style guide, a terminology reference, a findability checklist, one template per
genre. The description field is what determines whether the skill fires at all, so it
names concrete trigger phrasings rather than describing the skill's purpose abstractly.

**Where it lives.** The file layout of every skill in this repo.

**Cost.** Under-triggering is the common failure — a skill that never fires is
indistinguishable from one that does not exist. Trigger descriptions need testing
against the requests they should catch, and I have not built a systematic way to do
that.

---

## 10. Fictionalization as a portability method

**Problem.** Skills built against proprietary subject matter cannot be shown to anyone.
Rebuilding them from scratch for a portfolio discards the architecture along with the
content.

**Mechanism.** Keep the architecture, replace the subject matter. `unused-access-expert`
and `ridgeline-doc-writer` are structurally the same pair as their work equivalents —
same ownership split, same handoff table, same precedence chain — describing a fictional
product instead of a real one. The mapping is recorded, so the fiction stays internally
consistent across pages.

This is the pattern that made this document possible: when the proprietary source became
unavailable, nothing about the method was lost, because the method had already been
reproduced in a form I own.

**Cost.** The fictional product needs enough depth to exercise the architecture. A thin
fiction produces skills that look like templates.

---

## What is still missing

- **No trigger-reliability testing.** Skill descriptions are written carefully and
  never measured. Under-triggering is the known failure mode and I have no evidence
  about my own rate.
- **No staleness mechanism.** Pattern 7 prescribes dated snapshots; nothing enforces a
  refresh, and nothing detects that a snapshot has drifted.
- **Genre coverage was demand-driven.** Genres exist because a task needed one, not
  because the set was designed. There is probably a missing genre and a redundant pair.
- **The linter boundary in pattern 3 has no owner.** When linter rules change, the
  auditor's exclusion table silently becomes wrong.

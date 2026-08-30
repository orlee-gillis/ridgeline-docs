# Ridgeline Docs-as-Code Roadmap: TRACKS.md

The syllabus says what each module teaches; this document says when things happen, in what order, and whose move it is. It's organized as numbered working sessions, not calendar weeks - a session is one sitting of 15-60 minutes, and the pace is yours. A comfortable cadence is 2-3 sessions per week, which lands the whole project in roughly 8-10 weeks.

Each session ends with a Next line: the exact thing that happens after it, and whether the move is yours or Claude's. When you come back after a break and don't remember where you were, find the first unchecked box and read its Next line.

**Legend**: [x] done · [~] in progress · [ ] not started · (You) your move · (Claude) say the word and it's generated

---

## Resume here

**Last worked**: Session 25 (README rewritten as a guided tour) — **DONE** [x]

**Then**: Session 26 - Defense (interview practice)

**Also outstanding** (not part of the Session 26 flow, deferred separately): Session 29 - ground
and build 3 gates left half-finished by unplanned Aug 19-23 work. See the Phase H addendum.

---

## Roadmap overview

This is a portfolio project demonstrating system-level thinking about AI-assisted documentation. Each phase builds infrastructure; later phases showcase it.

**Phases A-F** (Sessions 1-24): Build the system
- A: Foundations (writing in Docusaurus)
- B: Legacy content (editorial judgment, before/after)
- C: Docs-as-code (CI pipeline, PR loop)
- D: AI authoring (drafting with prompts)
- E: Quality gates (deterministic + advisory validation)
- F: Skills automation (measure, freeze, validate through CI, audit and improve)

**Phase G** (Sessions 25-26): Capstone - Package and explain the system
- **Essential**. Not more building—narrative and defense.
- Proves you can explain and defend the system you built.

**Phase H** (Sessions 27+): Stretch - Apply or extend
- **Optional**. After Phase G succeeds, choose one of these paths.
- Path 1: Scale to real professional work (apply gates system professionally)
- Path 2: Build tooling (audit script, interactive components)
- Path 3: Skip—capstone is complete at Session 26

---

## Phase A - Foundations (Module 0) - sessions 1-4

Setup and basic Docusaurus authoring. Learn the writing environment.

- [x] Session 1 - Setup. Private practice repo created, six kit files uploaded, syllabus renamed to README, answer keys foldered.
- [x] Session 2 - Scenario 1 (hub page). Formatted, previewed, committed. Learned: frontmatter fencing, plain-paragraph rules, screenshot placeholder, sidebar_position.
- [x] Session 3 - Scenario 2 (report page). ~30 min. New elements: navigation path, pipe table, nested bullets, fenced code block with language identifier.
- [x] Session 4 - Scenario 3 (reference page). ~45 min. New elements: admonitions, H2/H3/H4 nesting, inline code for angle-bracket patterns, the Note vs. Important call.

**Module 0 complete.** You can author and preview Docusaurus pages, commit to main, and watch the CI pipeline run.

---

## Phase B - Legacy content (Module 1) - sessions 5-8

Fictionalize your real documentation. Demonstrate editorial judgment.

Two before pages, two after pages, one short note on what changed. That's the whole deliverable - it's the only artifact in the repo that proves editorial judgment rather than tooling, and the only one a non-technical reader can judge in two minutes.

- [x] Session 5 - Before pages land. (Claude) generated the fictionalized legacy articles in ai-workflow/legacy/ - your real structure, Ridgeline vocabulary, rough spots preserved. They are the "before", so they don't get edited. Plus the private fictionalization map, which stays out of the public repo.
- [x] Session 6 - Your audit. ~15 min, no AI. Read the two pages and list what's wrong.
- [x] Session 7 - Claude adds what you missed. One combined list, no scoring. You approved or rejected each item - rejecting things is part of the evidence.
- [x] Session 8 - After pages. Improved versions in docs/, plus docs/what-changed.md. Provenance sentence: These pages are fictionalized from documentation I wrote and published professionally; the structure and the flaws are real, the product is not.

**Module 1 complete.** Your before/after pages prove you can edit for clarity and structure, and you understand what makes docs fail.

---

## Phase C - Docs-as-code live (Module 2) - sessions 9-12

Build the publishing pipeline. Learn the full PR loop.

- [x] Session 9 - The site skeleton. Docusaurus scaffolding into ridgeline-docs, CI off.
- [x] Session 10 - First deploy. GitHub Pages enabled, deploy action watched, live URL open.
- [x] Session 11 - The PR loop: where doc editing begins. Open the page's .md file, edit, commit to a new branch, open the PR, review your own diff, merge, watch the site redeploy. Every content change from here on happens through this exact loop.
- [x] Session 12 - Break it on purpose. A PR with a broken relative link and a skipped heading level; read the build failure; fix; merge.

**Module 2 complete.** You now have the full publish loop. Every page is authored, validated, and deployed through CI.

---

## Phase D - AI authoring (Module 3) - sessions 13–15

Use AI to draft pages from product requirements. Prove you can prompt and edit.

- [x] Session 13 - Feature notes. (Claude) produced a Jira story for one new Unused Access capability not covered by the legacy pages. You read it as you would a real story: what's missing, what's ambiguous, what contradicts a published page.
- [x] Session 14 - The flagged draft. The drafting prompt run against the story; AI first draft with [VERIFY] flags. You resolved every flag with invented SME answers, and noted which flags were legitimate gaps, which were model timidity, and which were confident invention - a third category the session surfaced.
- [x] Session 15 - The human edit. Draft committed at its docs/ path, then the editing pass as a second commit, so the diff in the pull request is the editorial story. Notes, prompt, and draft in ai-workflow/; the final in docs/. Merged: PR #5, Session 15: human edit of Apply a remediation recommendation.

**Module 3 complete.** You can draft with AI and edit the output. Your PR diff proves the editorial work.

---

## Phase E - Quality gates (Module 4) - sessions 16-18

Build deterministic and advisory validation gates. Automate quality checks.

- [x] Session 16 - Deterministic gates on. Enable Vale + markdownlint + link check + build as blocking checks. Open a PR containing a planted "please," a curly quote, and a dead link; watch three gates fail; fix; merge.
- [x] Session 17 - The AI reviewer. Add the ANTHROPIC_API_KEY secret; enable the advisory review workflow; open a real PR and read the model's comment. Decide whether you agree with each point - disagreeing is allowed, because it's advisory.
- [x] Session 18 - Tune one rule. Pick one Vale rule that annoyed you, change it via a PR to the rule file itself. The style guide is now living infrastructure.

**Module 4 complete.** The pipeline is whole: authoring → validation → deployment.

---

## Phase F - Skills automation - sessions 19-24

The portfolio's differentiating stage: not "I used AI to write docs" but "I built the AI's instructions, measured them through automated gates, and improved them on evidence."

Sits here because it needs Vale (Module 4), the PR loop (Session 11), and real drafting experience (Module 3).

### Session 19: Setup

- [x] AGENTS.md and Vale committed and running
- [x] CLAUDE.md extended with directory roles and frozen-skills rule
- [x] Test: Claude Code refuses to edit files in ai-workflow/legacy/

**Next**: Session 20 - Define templates and baselines

### Session 20: Templates & Baselines

- [x] Define templates in ai-workflow/skills/templates/:
  - parent-report.md (structure, purpose, sections)
  - child-report.md (structure, purpose, sections)
  - workflow-methodology.md (structure, purpose, sections)
- [x] Update skill-architecture.md with Templates section
- [x] Add classification logic to ridgeline-doc-writer (Step 1: Classify the article type)
- [x] Create decisions/phase-f-skills-eval-scope.md (scope, success criteria)
- [x] Freeze baseline snapshots in ai-workflow/skills/baseline/:
  - baseline/ridgeline-doc-writer.md
  - baseline/unused-access-expert.md
- [x] Write eval cases to eval-cases/phase-f-eval-cases.md (4 test prompts for report overviews)
- [x] Create template compliance advisory scripts:
  - validate-parent-report.py
  - validate-child-report.py
  - validate-workflow-methodology.py
  - Add to .github/workflows/docs-ci.yml (advisory, non-blocking)

**Branch**: session-20/skills-eval-setup

**Success criteria**: All templates defined, classification logic added, baseline frozen, eval cases written, advisory gates working.

**Next**: Session 21 - Design audit gate + validate baseline

### [x] Session 21: Design Audit Gate + Validate Baseline

Measure your frozen baseline skills using CI gates as the validation mechanism.

**What you're doing:**
- Complete the 4 eval cases from Session 20
- Design an audit gate for report structure validation
- Use Claude Code to refine the audit rubric interactively
- Establish pass/fail criteria for baseline measurement

**Deliverable:**
- GATES-DESIGN.md (audit gate purpose, criteria, cost estimate)
- gates-test.json (your 4 eval cases as gate test cases)
- GATES-CHANGELOG.md (first entry)
- Baseline metrics recorded

**Templates provided**: See GATES-DESIGN.md, gates-test.json, GATES-CHANGELOG.md in your current directory (ready to fill in and commit)

**Branch**: session-21/audit-gate-design

**Status**: Done - GATES-DESIGN.md, gates-test.json, and GATES-CHANGELOG.md committed and merged
(PR #45). Baseline metrics were recorded in the `docs-as-code` repo instead
(`ai-workflow/eval-results/session-20-baseline-scores.md` there), not this one.

**Next**: Session 22 - Build gate infrastructure + CLAUDE.md

### [x] Session 22: Build Gate Infrastructure + Skill Selection

Build the GitHub Actions workflow, gate script, and automatic skill selection system.

**Completed, diverged from plan below - see `GATES-CHANGELOG.md`'s Session 22 entry for the full
story.** Items 1-2 as originally scoped (`audit-report-pages.yml` / `audit-report.js`) were dropped
partway through: the "Report page" genre they were built to check turned out not to correspond to
any real page in `docs/`. In the process of figuring that out, found that three *other*, older
gates (`validate-parent-report.py`, `validate-child-report.py`,
`validate-workflow-methodology.py`) had existed in the repo but never actually run - no real page
had ever carried the `template:` tag they looked for, and one had a live authentication bug.
Fixed and activated those three instead. Items 3, 4, 6, 7 below were completed as planned (4 took
two passes - `.claude/skill-selection.md` was missed initially and added afterward). Item 5 (test
locally) was completed with 6 cases across the 3 real gates (a real tagged page + a synthetic
fixture each) rather than 4 synthetic-only cases.

**What you'll do:**
1. ~~Create `.github/workflows/audit-report-pages.yml` (GitHub Actions workflow)~~ - dropped, see above
2. ~~Create `audit-report.js` (Node.js gate script)~~ - dropped; built `gate_common.py` + 3 real gates instead
3. Create `CLAUDE.md` at repo root with skill triggers for automatic loading
4. Create `.claude/` folder with infrastructure documentation:
   - `.claude/gates-architecture.md` — system structure, cost model, conventions
   - `.claude/prompt-patterns.md` — templates for audit/validation/generation gates
   - `.claude/skill-selection.md` — how Claude Code automatically loads skills
   - `.claude/testing-patterns.md` — how to test gates locally
5. Test gate locally on your 4 eval cases
6. Create GATES.md inventory (first gate documented)
7. Create GATES-CHANGELOG.md (gate creation dated and reasoned)

**Hands-on**: Use Claude Code to generate the workflow + script from the design. Test locally. Iterate on the prompt if needed. Once precision >80%, move to next session.

**Deliverable:**
- ~~Working audit gate in GitHub Actions~~ - three working gates instead (`validate-parent-report`, `validate-child-report`, `validate-workflow-methodology`), fixed rather than newly built
- CLAUDE.md with all skills + `load_when` triggers
- `.claude/` documentation suite
- GATES.md (first gate: audit-report-pages) - GATES.md documents all three real gates instead
- GATES-CHANGELOG.md

**Time**: ~2–2.5 hours (actual: significantly longer - most of the time went into discovering and correcting the wrong premise, not building against the original design)

**Next**: Session 23 - Validate gates + agentic-gates design

### [x] Session 23: Validate Gates + Agentic-Gates Design

Prove the three real genre gates work and sketch (not build) Phase H's agentic-gates idea.
Rewritten from the original Part A/B/C plan below, which assumed a single "audit gate" and a
still-to-build second gate - both stale after Session 22 replaced that premise with three working
gates (`validate-parent-report`, `validate-child-report`, `validate-workflow-methodology`). The
LLM-ready-docs work originally planned as Part C is dropped from this session: it now belongs to
`documenting-the-agentic-stack.md` Week 3 in `docs-as-code`, not a second build here - see that
file and `docs-as-code/TRACKS.md` row 10.

**Part A: Validate the three real gates** ✅ - `GATES-METRICS.md`
- Ran all three genre gates via `./verify.sh`'s `--test-file` mode: 6/6 test cases passed (2 per
  gate - the real tagged page and a deliberately-broken synthetic fixture)
- Precision 100% (3/3), recall 100% (3/3) on this test set - clears the >80%/>70% bar, though the
  sample is small (n=2 per gate); see `GATES-METRICS.md`'s sample-size caveat and follow-up
- Corroborated by two real findings the gates already caught in production before this metrics
  run existed (the `unused-access-report.md` data-freshness contradiction, the correctly-flagged
  `apply-a-remediation.md` `[VERIFY]` item) - see `docs/meta/ci-gates.md`

**Part B: MCP exploration - interactive skills only** ⏸ Deferred, not dropped
- Turned out not to prove what it was meant to: fetching a reference doc live via MCP demonstrates
  *using* a connector, not *documenting* one - "documenting MCP connectors" as a portfolio claim is
  already covered by `docs-as-code`'s `documenting-mcp.md` track
- The narrower thing this would actually test - whether a skill fetching a live reference doc is a
  viable fix for the glossary/knowledge-base drift already noted in `docs-as-code/roadmap.md`'s
  "Glossary reconciliation" TODO (bundled copies in both skills going out of sync with the public
  copy) - is still worth trying eventually, just not gating Session 23
- Parked as a nice-to-have, no session number assigned - pick it up anytime, or fold it into
  Session 24 if the skills audit there surfaces the drift problem directly
- Original scope, for whenever this happens: MCP for the `unused-access-expert`/
  `ridgeline-doc-auditor` skills at chat time only (not CI gates); explore fetching the glossary or
  `unused-access-expert` knowledge base via MCP instead of a static bundled file; document the
  pattern in `.claude/mcp-integration.md`

**Part C: Sketch Phase H's agentic gates (plan only, don't build)** ✅ - `GATES-AGENTIC-DESIGN.md`
- Design sketch covers: write access scoped to a proposal PR (never a direct commit), a mandatory
  review step with no auto-merge at any confidence level, a rollback path (isolated commits, clean
  revert), and a narrow confidence/scope gate so it never proposes a fix for anything requiring
  judgment (e.g. an open `[VERIFY]`)
- Stays a plan for Phase H; nothing here is implemented

**Deliverable:**
- GATES-METRICS.md with precision/recall for all three gates
- A short agentic-gates design note (Phase H planning, not an implementation)
- Updated GATES-CHANGELOG.md
- (Deferred, not delivered this session: `.claude/mcp-integration.md` - see Part B above)

**Time**: ~1.5 hours total (Part B's ~1 hour deferred)

**Branch**: session-23/gates-validation-mcp

**Success criteria**:
- All three gates: precision >80%, recall >70%
- Agentic-gates idea has a written design note, not an implementation

**Next**: Session 24 - Audit and improve the skills

---

### [x] Session 24: Audit and Improve the Skills ✅

Audit the two frozen baseline skills (`ridgeline-doc-writer`, `unused-access-expert`) against the
full seven-dimension rubric, then improve them. This session was originally tracked in
`docs-as-code`'s `roadmap.md` as its own "Session 22," before gate infrastructure work got
reprioritized into Session 22 here - see `GATES-CHANGELOG.md`'s Session 22 entry and
`docs-as-code/TRACKS.md`'s Session 24 for the full renumbering story. Folds in a separate
verification pass that `roadmap.md` tracked as "Session 23b."

**What you'll do:**
1. Your rubric verdicts first, then Claude's pass, then the revisions and the ADRs. **You first,
   then together.**
2. Resolve every `[VERIFY]` flag across all pages in `docs/`. For each: the invented SME answer,
   and a category - legitimate gap, model timidity, or confident invention. Record the categories
   in `ai-workflow/decisions/UAX-2841.md`.
3. Fix image sizing on `docs/apply-a-remediation.md` and remove its `[UNRELEASED]` block once its
   flags are closed.

**Rubric**: `ai-workflow/skills/rubric.md`. Worked example: `rubric-example.md`. Neither file
existed before Session 24, despite being referenced here as if they did - written as this
session's actual first step, seven dimensions grounded in `docs-as-code/roadmap.md`'s framework
table plus two new ones tied to this project's existing evidence (`[VERIFY]` resolution, the
genre gates). Score both skills yourself against `rubric.md` before reading Claude's pass.

**Delivered:**
- Rubric written (`ai-workflow/skills/rubric.md`, `rubric-example.md`) - didn't exist before this
  session despite being referenced as if it did
- Rubric verdicts for both skills, independently scored, then compared: `ridgeline-doc-writer`
  6/14 (yours) vs. 7/14 (Claude's); `unused-access-expert` 8/14 vs. 7/12 (Dimension 7 excluded as
  not applicable) - see `ai-workflow/skills/session-24-verdicts.md`
- Three scoring disagreements written up as ADRs, each with a concrete revision action - see
  `ai-workflow/decisions/session-24-rubric-disagreements.md`
- Both skills revised: `ridgeline-doc-writer`'s stale five-genre routing replaced with the three
  real genres (fixing a bug where drafts wouldn't carry a `template:` tag at all), its findability
  overlap with `doc-auditor` fixed, a `## Source hierarchy` heading added; `unused-access-expert`'s
  stray frontmatter artifact removed, its duplicated "High-risk sections" facts replaced with
  citations. Two new templates built (`child-report.md`, `workflow-methodology.md`), one renamed
  (`report-page.md` → `parent-report.md`)
- All 18 `[VERIFY]` flags across `docs/` resolved and categorized in `ai-workflow/decisions/UAX-2841.md`
  (legitimate gap / model timidity / confident invention) - including renaming the "Highly
  privileged" label to "High-impact" with a real definition, since the original term is real
  professional terminology that doesn't belong in this public repo
- Page titles fixed: dropped "About the..." from `unused-access-report.md` and
  `about-the-access-tab.md`'s titles and navbar labels (was never intended)
- `apply-a-remediation.md`'s `[UNRELEASED]` notice reformatted as a `:::warning` callout - **kept**,
  not removed, since the feature's name is still marketing's open call
- Added `stop-slop` as a 4th interactive skill (vendored, MIT-licensed, third-party) for catching
  AI writing tells in prose - documented in `.claude/skill-selection.md`
- **Follow-up, added after Session 25:** the revisions above were scored and reviewed statically
  but never actually run - the same gap that let Session 21's gate design stay broken for a full
  session. Fixed: three concrete functional tests confirm the routing fix, the findability fix, and
  `unused-access-expert`'s frontmatter all work in practice, not just on paper - see
  `ai-workflow/skills/session-24-functional-test.md`.

**Not done this session** (genuinely out of scope, not silently dropped): image sizing on
`apply-a-remediation.md` - no concrete issue was ever described anywhere for what "sizing" needed
fixing; worth a fresh look if it resurfaces as a real problem.

**Next**: Phase G, Session 25 - README tour

---

## Phase G - Capstone (Module 5) - sessions 25-26

**Essential.** Not more building—packaging and explaining the system you built.

The portfolio is now technically complete. Phase G is about narrative: making it clear what you built and why it matters.

### [x] Session 25: README Tour (The Guided Narrative) ✅

Your repo contains all the evidence. The README is the tour guide.

**Delivered:**
- Rewrote `README.md`: a positioning statement, then the pipeline in narrative order (legacy audit
  → improved pages → AI-assisted drafting → CI gates → skills measured and improved), each step
  linking its real artifact and stating what it proves
- Added a "How I built this" pointer to `ai-workflow/build-log.md`, per that file's own existing
  plan to be distilled here
- Setup instructions kept, moved after the narrative instead of leading with it
- Every link verified against a real file; build, markdownlint, and Vale all clean

**Next**: Session 26 - Defense (interview practice)

### [ ] Session 26: The Defense (Prove You Understand It)

Mock interview. Claude plays skeptical hiring manager. You defend your decisions.

**What you'll do:**
- Claude asks 5 hard questions about your system (sample questions below)
- You answer out loud, off the cuff, no notes (15–20 min)
- Then you write a 2-paragraph CV/LinkedIn blurb distilling the project

**Sample questions Claude might ask:**
- "Why freeze the skills before measuring them? Why not iterate first?"
- "Your gates are blocking 5% of PRs. Is that the right threshold?"
- "How would you scale this to a documentation set of 100 pages instead of 10?"
- "Why use skills instead of just calling the API with a long context window?"
- "What would you do if the product changed and your gate's facts became stale?"

**Deliverable:**
- Recorded or transcribed answers (shows you can explain the system)
- 2-paragraph CV/LinkedIn paragraph capturing the project

**Time**: ~1–1.5 hours

**Success criteria**: You can defend every major decision. You understand tradeoffs. You know what you'd do differently with more time.

**Branch**: session-26/capstone-complete

---

## Phase G complete ✓

Your portfolio is done and documented. You can explain it. You're ready to show it.

---

## Phase H - Stretch (Sessions 27+) - Optional

After Phase G, the portfolio is complete. Phase H is optional. Choose one path based on your goals.

### Path 1: Scale to Real Professional Work (Product Enablement Angle) — Recommended

If your goal is to move toward **product enablement roles**, apply the gates system to your real
professional documentation work. Keep this generic here - once it's real, that work and its
tooling belong in your employer's own private repo, not this public one.

**[ ] Session 27: Apply gates to your real professional documentation**

Build 2 gates against your real professional documentation work:
- Gate 1: Audit pages for style compliance, using your organization's own doc-writer skill
- Gate 2: Validate domain facts, using your organization's own subject-matter-expert skill

**What you'll do:**
1. Set up `.github/workflows/` in your organization's own repo (or create one) - not this repo
2. Adapt the gate architecture from Ridgeline (it's portable)
3. Build 2 gates specific to your organization's documentation
4. Document the gates in your organization's own private records - not `GATES.md` here

**Deliverable:**
- 2 working gates on real professional documentation, living in your employer's own private tooling
- Proof the system scales beyond Ridgeline
- Bridge from portfolio project to professional workflow

**Why this matters**: Product enablement teams build tooling. This shows you can design and operate gates in a real organization.

**Time**: ~2–3 hours

**Next**: You have a system in both a personal portfolio context (Ridgeline) and a real professional context.

---

### Path 2: Build Tooling (Advanced Coding) — Optional

Build interactive or analysis tools to showcase hands-on AI collaboration.

**[ ] Session 27: The audit script**

Crawl your live site and report on structure, broken links, readability.

- Write a plain-language spec
- (Claude) generates Python script from your spec
- You test, iterate on spec, run script
- Commit script + its output report

**Why**: Shows you can spec → iterate → integrate AI-generated code.

**[ ] Session 28: The MDX component**

Interactive decision tree: "Is the grant direct or inherited?" → recommended action.

- Spec the logic and UI
- (Claude) generates MDX (React in Markdown)
- You integrate into Docusaurus, debug build errors
- Live on your site

**Why**: Shows you can work with generated code in constrained environments.

**Time**: ~1.5 hours per session

---

### Path 3: Stop Here

Your portfolio is complete at Session 26. You don't need Phase H.

This is a valid endpoint: you've demonstrated system thinking, automation, and documentation skill. Everything else is polish.

---

### Addendum: unplanned work discovered on `main` (Aug 19-23), and its follow-up

Between Aug 19-23, PRs merged directly to `main` from Claude Code sessions outside this
conversation (branch pattern `claude/<slug>-<id>`), unrecorded here at the time. Reconciled after
the fact:

**What was real and correctly done**: the `parent-report`/`child-report`/`workflow-methodology`
gates - the exact fix this project's own "Fix the real docs-review gates" plan had queued - were
actually completed, and done well: all three real pages tagged with the right `template:` value,
the three scripts consolidated into a shared `.github/scripts/gate_common.py` (model
`claude-sonnet-5`, `ANTHROPIC_API_KEY`, structured output with a `suggestion` field, `--test-file`
local test mode), and the old fictional 4-genre `audit-report-pages` gate removed. No further work
needed there.

**What was incomplete**: three more genres - `api-reference`, `mcp-tool-reference`, `llm-docs` -
were added as Skills and documented in `CLAUDE.md` as if their CI gates existed ("Six CI gates
enforce template-specific requirements"). They don't. No script, no CI job, and no real page uses
any of the three - the templates' own example content is unfilled `[placeholder]` text, not
grounded in anything real, the same disconnection-from-reality mistake the original
`audit-report-pages` gate made. `CLAUDE.md` has been corrected to say so plainly in the meantime.

**[ ] Session 29: Ground and build the remaining 3 gates**

**In plain terms**: 3 Skills in this repo (`api-reference-validator`, `mcp-tool-reference-validator`,
`llm-docs-validator`) claim to automatically check pages of those 3 types. That check doesn't
actually run anywhere - no script, no CI job. This session builds the check for real, one genre at
a time, the same way Sessions 5-8 built the first working example of this pattern: a real page
first, then a checklist read off that page, then a script, then a CI job.

The actual procedure to follow is `.claude/gates-architecture.md`'s "Adding a new genre-specific
gate" section - it's already correct, including testing the script with `--test-file` before the
CI job gets added. What follows below is that same procedure worked through concretely for
`llm-docs`, so it's easier to picture - **if the two ever disagree, `gates-architecture.md` is the
one that's right**, not this worked example. Don't let this description drift from that file the
way `CLAUDE.md`'s gate count drifted from reality - if you change one, check the other.

**Worked example - do this once, for `llm-docs`** (the clearest of the 3, because its file already
exists and is already blank):

1. Write a first draft in `ai-workflow/drafts/llms-txt-draft.md` (not directly into `static/llms.txt` -
   per `CLAUDE.md`'s Draft Workflow rule: generated content is reviewed as a draft before it becomes
   the real thing). Content: a plain-text summary of this site, for an AI to read, not a human - one
   short paragraph per real page in `docs/`, e.g. "`unused-access-report.md`: what unused access is
   and how the report is ordered." No marketing language, just what each page contains.
2. **Review and edit that draft yourself before it goes anywhere near a gate.** This is the check-
   before-the-gate step - the draft exists so a wrong first attempt never becomes the thing the
   gate ends up measuring itself against.
3. Once you're satisfied, copy the reviewed content into `static/llms.txt` for real.
4. Open `audit-checklist.md` and add an `## llm-docs` section listing what makes that file good,
   read off what you just finalized in step 3 - e.g. "every real page in `docs/` is mentioned,"
   "no marketing language."
5. **`llm-docs` cannot reuse `gate_common.py` unmodified - check this before writing the script.**
   `gate_common.py`'s `run_ci()` only scans `docs/**/*.md` files and matches by a `template:`
   frontmatter tag. `static/llms.txt` is outside `docs/`, isn't Markdown, and has no frontmatter -
   it will never be found by that scan, no matter what it contains. `validate-llm-docs.py` needs to
   check `static/llms.txt` at its fixed path directly, not by tag-matching. Reuse `gate_common.py`'s
   `call_claude`/`response_schema`/prompt-building pieces if they fit, but the file-selection logic
   has to be different for this one genre - don't copy `validate-parent-report.py` and expect it to
   just work.
6. **Before touching CI, run it yourself with `--test-file`.** Write a small fixtures file with two
   cases: the real, finalized `static/llms.txt` from step 3 (expected: passes) and one small
   deliberately-broken version - e.g. missing a real page, or full of marketing language (expected:
   fails). Run `python validate-llm-docs.py --test-file <fixtures>.json` and confirm both come out
   right. Do not skip this - it's the exact step that was missing the first time (the original three
   scripts sat silently broken - wrong env var, a missing `.strip()` call - because nobody ran them
   before wiring them into CI).
7. Only once step 6 passes, add a `validate-llm-docs` job to `docs-ci.yml`
   (`continue-on-error: true` to start, same as the other three), so it runs on every PR.

**Then repeat the same shape for `mcp-tool-reference`** (draft in `ai-workflow/drafts/`, review it
yourself, promote to a real `docs/*.md` page tagged `template: mcp-tool-reference`, derive the
checklist from it, build the script, test with `--test-file`, then wire CI), using
`docs/pipeline-and-ai-terms.md`'s existing "MCP server"/"connector" section as your real source
material. Unlike `llm-docs`, this one **is** a normal `docs/*.md` page with frontmatter, so
`gate_common.py`'s existing tag-matching mechanism applies unmodified - `validate-mcp-tool-
reference.py` can be the same two-line wrapper shape as the original three.

**`api-reference` is different: skip it, for now.** Already checked during this reconciliation -
`grep -rli "endpoint\|rest api\|POST /\|GET /" docs/*.md` turns up nothing except the mystery
`documentation-validation-system.md` page itself, which isn't a real endpoint. There is no real
page to ground this genre in yet. Re-run that search in case something's changed, but go in
expecting "not yet" - and building only 2 of the 3 gates this session is a fine outcome, not a
shortfall.

**Once the script and CI job exist for a genre, update `CLAUDE.md`'s CI Gates section** to move it
out of "designed, not yet implemented" (added in PR #70) and into the real list.

**Deliverable:** real content in `static/llms.txt` (drafted, reviewed, promoted - not tagged, since
it has no frontmatter) and, if it makes sense, one new real `docs/*.md` page tagged `template:
mcp-tool-reference` - not `api-reference`, per above - each with its checklist section, its script
(`validate-llm-docs.py` using a fixed-path check, `validate-mcp-tool-reference.py` as a normal
`gate_common.py` wrapper), a `--test-file` fixtures file per script with a passing and a failing
case, a CI job added only after the fixtures pass locally, and `CLAUDE.md` corrected to match.

**Why this matters**: closes the gap between what `CLAUDE.md` claims and what the pipeline
actually runs - the same lesson Session 22/24's audit already taught this project once.

---

## Decision point: After Session 26

- **Highly recommended**: Do Path 1 (Scale to real professional work). It proves the system works professionally.
- **If you have time and interest**: Do Path 2 (audit script + MDX). It's showcase work, not essential.
- **Not optional in the same way as the above**: Session 29 (ground and build the remaining 3
  gates) - this isn't a stretch goal, it's closing a real gap left by unplanned work that landed on
  `main` on Aug 19-23. See the addendum above.
- **If you're satisfied**: Stop at Session 26. The portfolio is done.

---

## Project statistics

| Metric | Value |
|--------|-------|
| **Sessions (core)** | 26 (Phase A–G) |
| **Sessions (optional)** | 1–3 (Phase H, incl. Session 29) |
| **Total hours** | ~35–40 hours (core), 40–45 (with Phase H) |
| **Comfortable pace** | 2–3 sessions/week = 8–10 weeks |
| **Artifacts (final)** | 40+ files across docs/, ai-workflow/, .github/, .claude/ |
| **Live**: | Docusaurus site + GitHub Pages + GitHub Actions |

---

## Next immediate action

**You are here**: Sessions 21-25 done (Session 23's MCP exploration deferred as a nice-to-have, not
blocking). Phase F - Skills automation - is complete; Phase G - Capstone - is underway.

**Your move**: Start Session 26 (The Defense) whenever ready - see its full task breakdown above.

---

Created: [date]  
Last updated: Session 25 done (2026-08-20)  
Branch: session-25/readme-tour

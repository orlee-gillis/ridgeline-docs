# Ridgeline Docs-as-Code Roadmap: TRACKS.md

The syllabus says what each module teaches; this document says when things happen, in what order, and whose move it is. It's organized as numbered working sessions, not calendar weeks - a session is one sitting of 15-60 minutes, and the pace is yours. A comfortable cadence is 2-3 sessions per week, which lands the whole project in roughly 8-10 weeks.

Each session ends with a Next line: the exact thing that happens after it, and whether the move is yours or Claude's. When you come back after a break and don't remember where you were, find the first unchecked box and read its Next line.

**Legend**: [x] done · [~] in progress · [ ] not started · (You) your move · (Claude) say the word and it's generated

---

## Resume here

**Last worked**: Session 21 (design audit gate) — **IN PROGRESS** [~]

**Branch**: session-21/audit-gate-design

**Immediate next**: Complete Session 21 by creating and committing GATES-DESIGN.md, gates-test.json, and GATES-CHANGELOG.md (templates provided)

**Then**: Session 22 - Build gate infrastructure (GitHub Actions workflow + Node.js script + CLAUDE.md)

---

## Roadmap overview

This is a portfolio project demonstrating system-level thinking about AI-assisted documentation. Each phase builds infrastructure; later phases showcase it.

**Phases A-F** (Sessions 1-23): Build the system
- A: Foundations (writing in Docusaurus)
- B: Legacy content (editorial judgment, before/after)
- C: Docs-as-code (CI pipeline, PR loop)
- D: AI authoring (drafting with prompts)
- E: Quality gates (deterministic + advisory validation)
- F: Skills automation (measure, freeze, validate through CI)

**Phase G** (Sessions 24-25): Capstone - Package and explain the system
- **Essential**. Not more building—narrative and defense.
- Proves you can explain and defend the system you built.

**Phase H** (Sessions 26+): Stretch - Apply or extend
- **Optional**. After Phase G succeeds, choose one of these paths.
- Path 1: Scale to XM Cyber (apply gates system professionally)
- Path 2: Build tooling (audit script, interactive components)
- Path 3: Skip—capstone is complete at Session 25

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

## Phase F - Skills automation - sessions 19-23

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

### [~] Session 21: Design Audit Gate + Validate Baseline

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

**Status**: In progress—create the three files, fill them in, commit, then done.

**Next**: Session 22 - Build gate infrastructure + CLAUDE.md

### [ ] Session 22: Build Gate Infrastructure + Skill Selection

Build the GitHub Actions workflow, gate script, and automatic skill selection system.

**What you'll do:**
1. Create `.github/workflows/audit-report-pages.yml` (GitHub Actions workflow)
2. Create `audit-report.js` (Node.js gate script)
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
- Working audit gate in GitHub Actions
- CLAUDE.md with all skills + `load_when` triggers
- `.claude/` documentation suite
- GATES.md (first gate: audit-report-pages)
- GATES-CHANGELOG.md

**Time**: ~2–2.5 hours

**Next**: Session 23 - Validate gates + add validation gate + MCP + LLM docs

### [ ] Session 23: Validate Gates + MCP + LLM Documentation

Prove the audit gate works, add a validation gate, explore MCP, and document for LLM readers.

**Part A: Validate the audit gate** (~1 hour)
- Run audit gate against 8–10 past PRs from your repo
- Measure precision (of failures, how many are real?), recall (of problems it catches)
- Record metrics in GATES-METRICS.md
- Decision: is precision >80%, recall >70%? If not, adjust prompt and re-run.

**Part B: Design and build a validation gate** (~1 hour)
- Pick a second gate: **validation gate for Unused Access facts**
- Load the unused-access-expert skill as validation knowledge
- Design rubric: what counts as a valid claim about Unused Access?
- Build script + test locally on 3–4 test cases
- Document in GATES.md

**Part C: MCP exploration + LLM documentation** (~1 hour)
- **MCP**: Use Claude Code with Google Drive MCP to fetch and update a reference document
  - Example: Store "Unused Access glossary" in your Google Drive; fetch it via MCP
  - Show Claude Code using MCP to read the file and suggest updates to unused-access-expert.md
  - Document the pattern in `.claude/mcp-integration.md`
  - Why Google Drive: portable (you keep it after losing Atlassian access), personal account, same learning value
- **LLM docs**: Create the LLM-ready documentation layer
  - Create `ai-workflow/llm-ready-docs/` folder
  - Write `llm-ready-docs-checklist.md` (what makes a page LLM-friendly)
  - Mark up one finished page as an example (e.g., apply-a-remediation.md)
  - Create `ai-workflow/llm-ready-docs/llms.txt` (fragment: key concepts for LLMs)
  - Document in GATES-RUNBOOK.md how to maintain LLM-ready markup

**Deliverable:**
- GATES-METRICS.md with precision/recall for audit gate
- Second gate: validate-unused-access-facts.yml + validate-unused-access.js
- GATES-RUNBOOK.md (operations guide: debugging, tuning, adding gates)
- `.claude/mcp-integration.md` (MCP pattern for fetching + updating skills)
- `ai-workflow/llm-ready-docs/` folder with:
  - `llm-ready-docs-checklist.md`
  - `llms.txt`
  - One marked-up example page
- Updated GATES.md (now documents 2 gates)
- Updated GATES-CHANGELOG.md

**Time**: ~3 hours total

**Branch**: session-23/gates-validation-mcp-llm

**Success criteria**:
- Audit gate: precision >80%, recall >70%
- Validation gate: designed, tested, documented
- MCP: one working example of fetching + updating
- LLM docs: checklist + example + llms.txt

**Next**: Phase G, Session 24 - README tour

---

## Phase G - Capstone (Module 5) - sessions 24-25

**Essential.** Not more building—packaging and explaining the system you built.

The portfolio is now technically complete. Phase G is about narrative: making it clear what you built and why it matters.

### [ ] Session 24: README Tour (The Guided Narrative)

Your repo contains all the evidence. The README is the tour guide.

**What you'll do:**
- Rewrite the repo README as a guided tour
- Link every artifact in narrative order: legacy → audit → improved → notes → draft → final → gates → skills stage
- For each artifact, explain what it proves:
  - Before/after pages → editorial judgment
  - Drafting prompt + flagged draft + final edit → AI authoring skill
  - Vale rules, markdownlint, link check → deterministic validation
  - Advisory review workflow → AI as collaborator
  - Frozen skills, baselines, audit gate, validation gate → measurement + automation
  - CLAUDE.md, `.claude/` docs, MCP pattern → infrastructure thinking
  - LLM-ready markup → thinking beyond the immediate audience

- Make it readable in 5 minutes: someone visiting the repo should understand what you built without reading every file

**Deliverable:**
- Updated README.md that serves as a guided tour
- Every major artifact linked and contextualized
- Clear narrative: "Here's what I built and why"

**Time**: ~1.5–2 hours

**Next**: Session 25 - Defense (interview practice)

### [ ] Session 25: The Defense (Prove You Understand It)

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

**Branch**: session-25/capstone-complete

---

## Phase G complete ✓

Your portfolio is done and documented. You can explain it. You're ready to show it.

---

## Phase H - Stretch (Sessions 26+) - Optional

After Phase G, the portfolio is complete. Phase H is optional. Choose one path based on your goals.

### Path 1: Scale to XM Cyber (Product Enablement Angle) — Recommended

If your goal is to move toward **product enablement roles**, apply the gates system to your professional work.

**[ ] Session 26: Apply gates to XM Cyber docs**

Build 2 gates on your XM CEM Confluence work:
- Gate 1: Audit XCD pages for style compliance (using xcd-doc-writer skill)
- Gate 2: Validate CIEM facts (using ciem-expert skill)

**What you'll do:**
1. Set up `.github/workflows/` in the docs-as-code tracking repo (or create one)
2. Adapt the gate architecture from Ridgeline (it's portable)
3. Build 2 gates specific to XM CEM docs
4. Document in GATES.md for XM Cyber context

**Deliverable:**
- 2 working gates on professional documentation
- Proof the system scales beyond Ridgeline
- Bridge from portfolio project to professional workflow

**Why this matters**: Product enablement teams build tooling. This shows you can design and operate gates in a real organization.

**Time**: ~2–3 hours

**Next**: You have a system in both personal (Ridgeline) and professional (XM Cyber) contexts.

---

### Path 2: Build Tooling (Advanced Coding) — Optional

Build interactive or analysis tools to showcase hands-on AI collaboration.

**[ ] Session 26: The audit script**

Crawl your live site and report on structure, broken links, readability.

- Write a plain-language spec
- (Claude) generates Python script from your spec
- You test, iterate on spec, run script
- Commit script + its output report

**Why**: Shows you can spec → iterate → integrate AI-generated code.

**[ ] Session 27: The MDX component**

Interactive decision tree: "Is the grant direct or inherited?" → recommended action.

- Spec the logic and UI
- (Claude) generates MDX (React in Markdown)
- You integrate into Docusaurus, debug build errors
- Live on your site

**Why**: Shows you can work with generated code in constrained environments.

**Time**: ~1.5 hours per session

---

### Path 3: Stop Here

Your portfolio is complete at Session 25. You don't need Phase H.

This is a valid endpoint: you've demonstrated system thinking, automation, and documentation skill. Everything else is polish.

---

## Decision point: After Session 25

- **Highly recommended**: Do Path 1 (Scale to XM Cyber). It proves the system works professionally.
- **If you have time and interest**: Do Path 2 (audit script + MDX). It's showcase work, not essential.
- **If you're satisfied**: Stop at Session 25. The portfolio is done.

---

## Project statistics

| Metric | Value |
|--------|-------|
| **Sessions (core)** | 25 (Phase A–G) |
| **Sessions (optional)** | 1–2 (Phase H) |
| **Total hours** | ~35–40 hours (core), 40–45 (with Phase H) |
| **Comfortable pace** | 2–3 sessions/week = 8–10 weeks |
| **Artifacts (final)** | 40+ files across docs/, ai-workflow/, .github/, .claude/ |
| **Live**: | Docusaurus site + GitHub Pages + GitHub Actions |

---

## Next immediate action

**You are here**: Session 21 in progress. Complete by creating three files (templates provided).

**Session 21 task**: 
1. Fill in GATES-DESIGN.md (gate design, criteria, test cases)
2. Fill in gates-test.json (4 eval cases as test cases)
3. Fill in GATES-CHANGELOG.md (first entry: gate designed)
4. Commit all three

**Your move**: Fill templates, commit, then start Session 22. Use the mini learning plan (Sessions 22–23 of the CI gates course) as your step-by-step guide.

---

Created: [date]  
Last updated: Session 21 in progress  
Branch: session-21/audit-gate-design

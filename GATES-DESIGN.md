# Gate Design: Audit Report Pages

**Session**: 21  
**Gate Type**: Audit (quality validation)  
**Status**: Designed, ready for implementation in Session 22

---

## Overview

**Gate Name**: `audit-report-pages`

**Purpose**: Validate that new or updated report pages (child-report genre) match the required template structure and serve the reader's task.

**When it triggers**: Every PR that adds or modifies files matching `docs/**/*report*.md` or `docs/**/child-*.md`

**Does it block PRs?**: Yes, on high severity. Medium/low severity produces a report comment only.

---

## What it checks

### 1. Genre fit
- Does this page actually match the child-report template?
- Required sections present: Overview, Core concepts, How to investigate, Next steps
- Sections in the right order

### 2. Task fit
- Does the page serve the reader's actual task? (e.g., "how to investigate a report")
- Is it clear what the reader should do after reading?
- Does it link to prerequisites?

### 3. Unsourced claims
- Are facts about the feature stated without a source?
- Does the page credit related docs or skills?

### 4. Undefined terms
- Are there technical terms used without explanation?
- Are all jargon terms defined inline or linked to glossary?

### 5. Structure
- Are sections in a logical order for this genre?
- Is there adequate whitespace and examples?

---

## Severity framework

### High severity (blocks PR)
- Wrong genre (page is structured as reference/overview when it should be child-report)
- Missing critical section (e.g., no "How to investigate" in an investigation page)
- Unsourced claims in high-stakes domain (Unused Access, access grants)
- Page contradicts its own stated purpose

### Medium severity (report only)
- Style inconsistency (banned word, wrong capitalization)
- Confusing section order (suboptimal, not wrong)
- Undefined jargon (term used without explanation)
- Weak prerequisite linking (page should link to a foundational page)

### Low severity (informational only)
- Minor phrasing suggestions
- Readability improvements
- Optional structure refinements

---

## Test cases

**Test case 1**: [EVAL CASE 1 NAME FROM YOUR 4 EVAL CASES]
- Expected outcome: PASS
- Reason: Matches child-report template, clear task, properly sourced

**Test case 2**: [EVAL CASE 2 NAME]
- Expected outcome: PASS
- Reason: [reason]

**Test case 3**: [EVAL CASE 3 NAME]
- Expected outcome: FAIL (high severity)
- Reason: Missing "How to investigate" section

**Test case 4**: [EVAL CASE 4 NAME]
- Expected outcome: FAIL (medium severity)
- Reason: [reason]

---

## Cost & performance

**Cost per file**: ~2k tokens

**Latency**: ~2–3 seconds per page

**Determinism**: High (same file should produce same result on same prompt)

**False positive rate (estimated)**: ~5% acceptable (catches real structure problems, occasionally too strict on edge cases)

---

## Skills & context needed

**Skills to load**:
- `process-template` — child-report structure and genre definitions
- `ridgeline-doc-auditor` — audit rubric for task fit and unsourced claims

**External context**: None (everything is in skills)

**Prompt excerpt**:
```
You are auditing a Ridgeline child-report page.

Template structure:
- Overview: 1-2 sentence definition
- Core concepts: Define key terms
- How to investigate: Step-by-step walkthrough
- Next steps: Links to related pages

Audit for: (1) genre match, (2) task fit, (3) unsourced claims, (4) undefined terms, (5) structure

Severity: high = wrong genre/missing sections, medium = style/clarity, low = optional improvements
```

---

## Implementation notes

- Will be implemented in Session 22 as `.github/workflows/audit-report-pages.yml` + `audit-report.js`
- Skills are in `skills/` and loaded by the gate script
- Test cases will be stored in `gates-test.json` and run locally before CI deployment
- This gate is the first of the Phase F skills validation system

---

## Decisions & tradeoffs

**Why this gate first?** Report pages are the core of Phase D (AI authoring). Auditing them validates that the drafting system produces structurally sound output.

**Why these criteria?** They map directly to the child-report template and the Phase D drafting prompt.

**Why high severity on genre?** Wrong genre means the page structure is fundamentally broken. Fix before merge.

**Why medium severity on style?** Style issues don't break functionality. Can be fixed after merge if needed.

---

## Related documents

- `ai-workflow/skills/templates/child-report.md` — the template this gate validates
- `ai-workflow/skills/baseline/ridgeline-doc-writer.md` — the skill that produces these pages
- `eval-cases/phase-f-eval-cases.md` — the 4 test cases this gate uses

---

**Session 21 deliverable**: This document is complete and ready to commit.

**Next**: Session 22 will implement this design as a working GitHub Actions workflow.

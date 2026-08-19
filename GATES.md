# Gates inventory

Current state of every CI gate in this repo. For *why* a gate exists or changed, see
`GATES-CHANGELOG.md`. For *how* the gate system is organized, see `.claude/gates-architecture.md`.

---

## audit-report-pages

**Status**: Implemented, local tests passing (Session 22) - not yet enabled as a required check.

**Tier**: AI-blocking (see `.claude/gates-architecture.md`)

**Scope**: PRs touching `docs/**/*report*.md` or `docs/**/child-*.md`.

**Checks**: Report page genre compliance (inclusion/exclusion criteria, sort order and empty-value
handling, column table, "working a finding," data freshness, correct order), unsourced facts,
undefined terms, cross-page inconsistency, and stated purpose - using the same method as the
`ridgeline-doc-auditor` skill.

**Severity**: `high` blocks the PR. `medium` and `low` are report-only (posted as a PR comment, don't
fail the check).

**Model**: `claude-sonnet-5`.

**Files**:
- Design: `GATES-DESIGN.md`
- Script: `audit-report.js`
- Workflow: `.github/workflows/audit-report-pages.yml`
- Test fixtures: `gates-test.json`, `docs/eval-cases/*.md`

**Notes**: The original Session 21 design referenced an invented "child-report" page structure that
didn't match anything in the actual repo. Implementation was grounded in the real "Report page" genre
already defined in `ai-workflow/skills/ridgeline-doc-auditor/references/audit-checklist.md` instead -
see `GATES-CHANGELOG.md`'s Session 22 entry for the full reasoning.

---

## validate-child-report

**Status**: Live (pre-existing, predates the gates-inventory system).

**Tier**: AI-blocking

**Scope**: Files with `template: child-report` frontmatter under `docs/**/*.md`.

**Checks**: Required sections present and non-empty (mechanical), then AI validation that the
Introduction section states a value proposition and stays glossary-grounded.

**Model**: `claude-sonnet-4-6`.

**Files**: `.github/scripts/validate-child-report.py`

---

## validate-parent-report

**Status**: Live (pre-existing).

**Tier**: AI-blocking

**Files**: `.github/scripts/validate-parent-report.py`

---

## validate-workflow-methodology

**Status**: Live (pre-existing).

**Tier**: AI-blocking

**Files**: `.github/scripts/validate-workflow-methodology.py`

---

## review-docs (advisory)

**Status**: Live (pre-existing).

**Tier**: AI-advisory - never blocks (`continue-on-error: true`).

**Scope**: Any PR touching `docs/`.

**Checks**: Unsourced claims, purpose drift, term inconsistency, contradictions, unactionable
instructions. Explicitly does not repeat what the deterministic gates already cover.

**Model**: `claude-haiku-4-5`.

**Files**: `.github/scripts/review-docs.py`, the `review` job in `.github/workflows/docs-ci.yml`

---

## Deterministic gates

Not individually tracked here - see `.github/workflows/docs-ci.yml` for the `vale`, `markdown`,
`links`, and `build` jobs. No model call, no severity judgment, no design doc needed.

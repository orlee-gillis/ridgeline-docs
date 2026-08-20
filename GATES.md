# Gates inventory

Current state of every CI gate in this repo. For *why* a gate exists or changed, see
`GATES-CHANGELOG.md`. For *how* the gate system is organized, see `.claude/gates-architecture.md`.

---

## validate-parent-report

**Status**: Implemented, local tests passing (Session 22) - not yet a required check.

**Tier**: AI-blocking-capable (see `.claude/gates-architecture.md`), currently `continue-on-error: true`

**Scope**: Pages tagged `template: parent-report` in frontmatter.

**Checks**: The `parent-report` genre requirements in
`ai-workflow/skills/ridgeline-doc-auditor/references/audit-checklist.md` - what puts a row in the
report, what's excluded, how it's ordered and what an empty sort value means, a column table,
what to do with a finding, data freshness.

**Severity**: `blocker` / `should-fix` per finding, matching the checklist's own vocabulary.

**Model**: `claude-sonnet-5`.

**Real page checked**: `docs/unused-access-report.md` - the first real page this gate has ever
actually run against (see `GATES-CHANGELOG.md`, Session 22, for why it never ran before).

**Files**:
- Script: `.github/scripts/validate-parent-report.py` (thin wrapper) + `.github/scripts/gate_common.py` (shared implementation)
- Test fixtures: `parent-report-test.json`, `eval-cases/broken-parent-report.md`

---

## validate-child-report

**Status**: Implemented, local tests passing (Session 22) - not yet a required check.

**Tier**: AI-blocking-capable, currently `continue-on-error: true`

**Scope**: Pages tagged `template: child-report` in frontmatter.

**Checks**: The `child-report` genre requirements in `audit-checklist.md` - orientation, what
each part of the surface shows, how to read the primary view, the action it leads to, and any
guarantee attached to a recommendation (missing guarantee is a `blocker`).

**Severity**: `blocker` / `should-fix` per finding.

**Model**: `claude-sonnet-5`.

**Real page checked**: `docs/about-the-access-tab.md`.

**Files**:
- Script: `.github/scripts/validate-child-report.py` + `.github/scripts/gate_common.py`
- Test fixtures: `child-report-test.json`, `eval-cases/broken-child-report.md`

---

## validate-workflow-methodology

**Status**: Implemented, local tests passing (Session 22) - not yet a required check.

**Tier**: AI-blocking-capable, currently `continue-on-error: true`

**Scope**: Pages tagged `template: workflow-methodology` in frontmatter.

**Checks**: The `workflow-methodology` genre requirements in `audit-checklist.md` - prerequisites,
what you can do, the mechanics in the order they happen, any guarantee attached to a
hard-to-reverse step (missing guarantee is a `blocker`), limits and known gaps.

**Severity**: `blocker` / `should-fix` per finding.

**Model**: `claude-sonnet-5`.

**Real page checked**: `docs/apply-a-remediation.md`.

**Files**:
- Script: `.github/scripts/validate-workflow-methodology.py` + `.github/scripts/gate_common.py`
- Test fixtures: `workflow-methodology-test.json`, `eval-cases/broken-workflow-methodology.md`

---

## review-docs (advisory)

**Status**: Live (pre-existing, unchanged in purpose - Session 22 added an exclusion; Session 24
folded in AI-writing-tell checks, see below).

**Tier**: AI-advisory - never blocks (`continue-on-error: true`).

**Scope**: Any PR touching `docs/`, **except** pages tagged `template: parent-report` /
`child-report` / `workflow-methodology` - those get one of the three dedicated gates above
instead, so they don't get a second, overlapping AI comment on the same file.

**Checks**: Unsourced claims, purpose drift, term inconsistency, contradictions, unactionable
instructions, and AI writing tells (filler phrases, passive voice, vague declaratives, em dashes -
the core checks from `ai-workflow/skills/stop-slop/SKILL.md`, folded in here rather than run as a
second automated bot). Explicitly does not repeat what the deterministic gates already cover.
For a deeper pass than this summary check gives, ask for the `stop-slop` skill directly.

**Model**: `claude-haiku-4-5`.

**Files**: `.github/scripts/review-docs.py`, the `review` job in `.github/workflows/docs-ci.yml`

---

## Deterministic gates

Not individually tracked here - see `.github/workflows/docs-ci.yml` for the `vale`, `markdown`,
`links`, and `build` jobs. No model call, no severity judgment, no design doc needed.

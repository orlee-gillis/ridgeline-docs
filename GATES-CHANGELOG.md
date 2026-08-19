# GATES Changelog

**Date**: `[VERIFY: exact Session 21 date]`

This document tracks when gates are added, modified, deprecated, and the reasoning behind each change. It's the audit trail for the CI automation infrastructure.

---

## Session 21: Audit Gate Designed

**Gate**: `audit-report-pages`

**Date**: `[VERIFY: exact Session 21 date]`

**Action**: Designed (not yet implemented)

**Reason**: Phase F deliverable—validate that baseline skills produce structurally sound report pages. This gate will measure whether the frozen `ridgeline-doc-writer` skill and `unused-access-expert` skill are producing pages that match the child-report template and serve the reader's task.

**Scope**: Applies to all pages matching `docs/**/*report*.md` or `docs/**/child-*.md`

**Severity**: Blocks on high, reports on medium/low

**Status**: **SUPERSEDED in Session 22** - never implemented as designed. See the Session 22
entry below: the "Report page" / "child-report template" genre this design assumed doesn't
correspond to any real page. Left as-is above for the historical record.

**Related files**:
- `GATES-DESIGN.md` — full design documentation (now marked superseded)
- `gates-test.json` — 4 test cases (baseline validation)
- `ai-workflow/skills/templates/child-report.md` — the template being validated
- `ai-workflow/skills/baseline/ridgeline-doc-writer.md` — frozen skill this validates

**Notes**: This is the first gate in a Phase F automation system. It measures baseline skill quality through pass/fail criteria rather than manual human audit.

---

## Session 22: Activated the Real Page-Genre Gates

**Gates**: `validate-parent-report`, `validate-child-report`, `validate-workflow-methodology`

**Date**: 2026-08-19

**Action**: Fixed and activated (previously present but non-functional)

**Reason**: While reconciling the Session 21 `audit-report-pages` design against real content,
it became clear its "Report page" genre didn't match any real page - the page it was
implicitly grounded on, `docs/unused-access-report.md`, is actually a `parent-report` page,
one of three real, already-named genres with their own pre-existing scripts. Investigating why
led to finding those three scripts had never actually worked:

- No real page has ever carried a `template:` frontmatter tag, which all three scripts require
  to decide what to check. They've been silent no-ops since they were written.
- `validate-parent-report.py` had a live bug (`os.environ.get("CLAUDE_API_KEY").strip` -
  missing call parentheses, introduced by an earlier "fix/api-key-whitespace" commit that was
  trying to do the opposite) that would have thrown on every invocation.
- All three read a `CLAUDE_API_KEY` env var that isn't the secret actually configured in this
  repo (`ANTHROPIC_API_KEY`, used everywhere else).
- Their mechanical "required sections" checks (`Introduction`, `Requirements`, `Step 1/2/3`)
  don't match how the real pages are actually structured, confirmed by reading each real page's
  live structure.

Rather than build a new, disconnected `audit-report-pages` gate (Session 21's plan), fixed the
three existing scripts and pointed them at reality instead.

**Scope**: `validate-parent-report` runs on pages tagged `template: parent-report`;
`validate-child-report` on `template: child-report`; `validate-workflow-methodology` on
`template: workflow-methodology`. `docs/unused-access-report.md`, `docs/about-the-access-tab.md`,
and `docs/apply-a-remediation.md` are now tagged accordingly - the first real pages any of these
three gates has ever actually checked.

**Severity**: Each gate reports `blocker` / `should-fix` per finding (matching
`audit-checklist.md`'s existing severity vocabulary). All three jobs stay `continue-on-error:
true` in `docs-ci.yml` for now - they're running against real content for the first time ever,
so promoting them to a required, blocking check is a separate decision for after they've had a
chance to run clean on real PRs.

**Status**: Implemented, local tests passing (2 cases each: the real tagged page, plus a new
deliberately-broken fixture per genre) - not yet promoted to a required check.

**Related files**:
- `ai-workflow/skills/ridgeline-doc-auditor/references/audit-checklist.md` — genre sections
  renamed to match the real `template:` values and re-grounded in the real pages' actual
  structure (previous genres - Report page, Investigation surface page, Hub page, Reference
  page - removed; they didn't correspond to any real page)
- `.github/scripts/gate_common.py` — shared implementation (bug fixes, `ANTHROPIC_API_KEY`,
  structured JSON output via `output_config.format`, a required `suggestion` field per finding,
  `claude-sonnet-5`, `--test-file` local test mode) used by all three thin per-genre scripts
- `parent-report-test.json`, `child-report-test.json`, `workflow-methodology-test.json` +
  3 new fixtures under `eval-cases/`
- `.github/scripts/review-docs.py` — now skips pages tagged with one of the three genres
  (previously it had no such exclusion, since these gates had never actually run on anything)

**Notes**: `GATES-DESIGN.md` (the Session 21 `audit-report-pages` design) is marked superseded
rather than deleted, as a record of the wrong turn and why it was corrected.

---

## Future entries (template for next sessions)

### Session [X]: [Gate Name] [Action]

**Gate**: `[gate-name]`

**Date**: [DATE]

**Action**: [Designed / Implemented / Modified / Deprecated]

**Reason**: [Why this gate exists or changed]

**Scope**: [When it triggers]

**Severity**: [Blocking or reporting]

**Status**: [In progress / Ready / Live / Deprecated]

**Related files**: [Links to design, scripts, test cases]

**Notes**: [Any important context]

---

## Gate lifecycle

Each gate follows this sequence:

1. **Session N: Designed** — Purpose, scope, criteria, cost estimate documented in GATES-DESIGN.md
2. **Session N+1: Implemented** — GitHub Actions workflow + Node.js script created, tested locally
3. **Session N+2+: Live** — Running on PRs, metrics collected, false positive rate measured
4. **Optional**: Modified (prompt tuned, scope changed, severity adjusted)
5. **Optional**: Deprecated (replaced, no longer useful)

This changelog records each state transition and the reason for it.

---

## Gate inventory by status

### Designed (waiting for implementation)
- (none)

### Implemented (not yet live)
- validate-parent-report (Session 22)
- validate-child-report (Session 22)
- validate-workflow-methodology (Session 22)

### Live (running on PRs)
- (none yet)

### Deprecated
- (none yet)

---

## Principles

- **Every gate starts here**: Before writing workflow files, the gate is designed and documented.
- **Decisions are recorded**: "Why did we add this gate?" is answered here, not reconstructed from git history.
- **Cost is tracked**: Each gate entry notes tokens/latency so we can budget and decide when to run selective gates.
- **Severity is intentional**: Why does this gate block? Why does that one only report? Both decisions are explicit.

---

**Last updated**: Session 22 (validate-parent-report, validate-child-report, validate-workflow-methodology fixed and activated)

**Next update**: When one of the three gates is promoted to a required check, or the next gate is designed

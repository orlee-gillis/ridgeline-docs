# Prompt patterns for gates

Two patterns exist in this repo's gates. Reuse one of these rather than inventing a third.

## Pattern 1: Advisory diff review

Used by `.github/scripts/review-docs.py`. Reviews a diff (not a whole file), returns free-text
prose, posts it as a comment, never blocks.

Shape:
- Input: `git diff` output for the changed region only.
- Explicitly tells the model what NOT to check (things the deterministic gates already cover) -
  this is the most important line in the prompt. Without it, the model re-reports style issues
  Vale already caught, and the comment becomes noise.
- **Excludes files already covered by a genre-specific gate** (Pattern 2, below) before the diff
  ever reaches the model. `strip_covered_files()` parses the diff into per-file blocks, reads
  each file's *current* `template:` frontmatter from disk (not from the diff - an unrelated line
  change won't show unchanged frontmatter), and drops any block whose page is tagged
  `parent-report` / `child-report` / `workflow-methodology`. Without this, a report page gets two
  separately-worded AI comments about the same underlying issue.
- Output: free text, under a stated word limit, "say so in one sentence and stop" if nothing's
  wrong.
- Model: `claude-haiku-4-5` - cheap, because the output is advisory and a human filters it anyway.

Use this pattern for: PR-level advisory feedback that doesn't need to key on a specific finding
severity or block anything.

## Pattern 2: Structured genre audit with severity and suggestions

Used by `gate_common.py`, shared across `validate-parent-report.py`, `validate-child-report.py`,
`validate-workflow-methodology.py`. Reviews a whole page, returns a severity-ranked findings list
with sources and suggested fixes, and the calling script decides pass/fail from
`highest_severity`.

Shape:
- Input: the whole page (genre-level checks need the full structure, not one section).
- Context: the relevant `## <genre>` section of `audit-checklist.md`, read from disk at request
  time via `extract_checklist_section()` - not copy-pasted into the prompt as a static string.
  This keeps the gate in sync with the checklist; if the genre's requirements change, the gate's
  behavior changes with them, without a script edit.
- Output: `output_config.format` with an explicit JSON schema (`response_schema()` in
  `gate_common.py`), not a JSON-shaped instruction in prose. The API enforces the schema, so
  parsing never needs a bare `try/except` - the earlier version of these three scripts had
  exactly that pattern (`except: return False, ["Claude validation failed"]`), which silently
  swallowed real errors (including, at one point, an authentication bug - see
  `GATES-CHANGELOG.md`, Session 22) as a generic, unhelpful message.
- Every finding requires a `source` field (which checklist row it violates) and a `suggestion`
  field (a concrete fix, not a restatement of the problem) - "only report it if you can cite a
  source" mirrors the `ridgeline-doc-auditor` skill's own rule.
- Severity vocabulary matches the checklist's own (`blocker` / `should-fix`), not a separate
  scale invented per gate.
- Model: `claude-sonnet-5` - these gates are meant to eventually block PRs, so accuracy matters
  more than the cost delta over haiku.

Use this pattern for: any genre-specific gate that needs a severity judgment grounded in a
written checklist, not just a boolean.

## Choosing between them

| Question | Pattern |
| --- | --- |
| Does the page have a real `template:` genre with a written checklist section? | Yes -> Pattern 2. No -> Pattern 1 (general advisory). |
| Does this block a PR (even eventually)? | Yes -> Pattern 2. No, purely advisory -> Pattern 1. |
| Does the check need the whole page, or one diffed region? | Whole page -> Pattern 2. Diff region -> Pattern 1. |

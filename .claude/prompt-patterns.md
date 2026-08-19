# Prompt patterns for gates

Three patterns exist in this repo's gates. Reuse one of these rather than inventing a fourth - the
differences between them are deliberate, not accidental variation.

## Pattern 1: Advisory diff review

Used by `.github/scripts/review-docs.py`. Reviews a diff (not a whole file), returns free-text prose,
posts it as a comment, never blocks.

Shape:
- Input: `git diff` output for the changed region only.
- Explicitly tells the model what NOT to check (things the deterministic gates already cover) - this
  is the most important line in the prompt. Without it, the model re-reports style issues Vale
  already caught, and the comment becomes noise.
- Output: free text, under a stated word limit, "say so in one sentence and stop" if nothing's wrong.
- Model: `claude-haiku-4-5` - cheap, because the output is advisory and a human filters it anyway.

Use this pattern for: PR-level advisory feedback that doesn't need to key on a specific finding
severity or block anything.

## Pattern 2: Structured JSON validation

Used by `validate-child-report.py` and friends. Reviews one section of one file, returns a fixed JSON
shape, and the calling script decides pass/fail from a boolean.

Shape:
- Input: one section's content (not the whole page, not a diff).
- Output: `{"valid": true/false, "issues": [...]}` requested via a JSON instruction in the prompt text.
- Model: `claude-sonnet-4-6`.

**Known weakness, worth fixing if you touch this pattern again:** the response is parsed with a bare
`try: json.loads(...) except: return False, ["validation failed"]`. If the model wraps the JSON in
prose or the schema drifts, this fails silently as "invalid" rather than surfacing what actually went
wrong. `audit-report.js` (pattern 3) fixes this with `output_config.format` (structured outputs),
which guarantees parseable JSON instead of hoping for it.

Use this pattern for: single-question validation where the answer is genuinely boolean, and where a
false negative just means an extra look, not a wrongly-blocked PR.

## Pattern 3: Structured audit with severity

Used by `audit-report.js` (Session 22). Reviews a whole page, returns a severity-ranked findings list
with sources, and the calling script decides pass/fail/block from a `highest_severity` field.

Shape:
- Input: the whole page (genre-level checks need the full structure, not one section).
- Context: the relevant skill file(s) and checklist section, read from disk at request time - not
  copy-pasted into the prompt as a static string. This keeps the gate in sync with the skill; if
  `audit-checklist.md` changes, the gate's behavior changes with it, without a script edit.
- Output: `output_config.format` with an explicit JSON schema (`RESPONSE_SCHEMA` in
  `audit-report.js`), not a JSON-shaped instruction in prose. The API enforces the schema, so parsing
  never needs a bare try/except.
- Every finding requires a `source` field - this mirrors the audit skill's own rule ("if you cannot
  cite one, do not report the problem"). A prompt that skips this produces reasonable-sounding but
  unfalsifiable findings.
- Model: `claude-sonnet-5` - this gate blocks PRs, so accuracy matters more than the cost delta over
  haiku or sonnet-4-6.

Use this pattern for: any new blocking gate that needs a severity judgment, not just a boolean.

## Choosing between them

| Question | Pattern |
| --- | --- |
| Does this block a PR? | No -> pattern 1. Yes -> pattern 2 or 3. |
| Is the check genuinely binary (present/absent, valid/invalid)? | Yes -> pattern 2. No, it's a judgment with degrees -> pattern 3. |
| Does the check need the whole page, or one section? | Whole page -> pattern 3. One section -> pattern 2. |

# Case Study: Running the Documentation Orchestrator Against the Real UAX PRD

This is the case study `ai-workflow/decisions/multi-type-validation-architecture.md` names as
its own "Next Step 4" — never written until now. The other three next steps from that decision
(config file, real run, captured output) are all done here too, for real, not simulated.

**Config used:** `.claude/documentation-config.json` — `documentation_types: ["api-docs",
"mcp-tools", "llm-docs"]`, matching the PRD's own "Documentation Needs for MVP" section exactly
(it names those three, not `user-guide` — that's explicitly listed under "Future Phases (Not in
MVP)").

**Input:** `ai-workflow/inputs/uax-prd-with-customer-request.md`, read in full, no summarizing.

---

## Stage 0 — Generic PRD validation (`documentation-input-validator`)

**Result: PASS — Complete (Ready).**

Checked every required element against the checklist:

| Required element | Present? | Where |
|---|---|---|
| Feature name | ✓ | "Unauthorized Agent Access (UAX) Detection" |
| One-sentence purpose | ✓ | Feature Overview |
| Link to source | ✓ | Customer request #CUST-2026-0847, cited with a direct quote |
| Scope in/out | ✓ | Full "What's Included" / "What's Excluded" lists |
| Audience | ✓ | Primary + secondary users, with explicit goals |
| Core workflow | ✓ | Two full worked scenarios ("Happy Path" + "Example Scenario") |
| Key actors/entities | ✓ | Dedicated section, both actors and entities |
| Known constraints | ✓ | Performance, technical, and business constraints all listed |
| Error scenarios (should-have) | ✓ | Normal cases + edge cases |
| Access control (should-have) | ✓ | Named explicitly as a business constraint |
| Dependencies (should-have) | ✓ | "Relationship to Other Systems" section |
| Versioning notes (should-have) | — | Not present — one should-have gap, doesn't block |

No contradictions found (read-only framing is consistent everywhere it's mentioned — the
checklist's specific failure-mode example, a "read-only" vs. "can modify" conflict, does not
occur here).

This PRD is a genuinely strong Stage 0 pass — better than the checklist's own worked example, in
fact, since it includes a real customer quote the example doesn't.

---

## Stage 1 — Type-specific validation

**Result: all three types INCOMPLETE.** This is the actual, useful finding from running the
pipeline for real — not a formality, and not what I assumed going in.

### `mcp-tool-reference-validator` — INCOMPLETE

The PRD names exactly 2 example endpoints (`get_unauthorized_access`, `get_remediation_options`,
plus an "etc.") out of what other planning docs describe as a 5-tool surface. For any of them:

- ✗ No parameters listed for any tool (types, required/optional, defaults, constraints, "where
  to get it")
- ✗ No return structure (top-level keys, nested objects, nullable fields)
- ✗ No real example response for any tool
- ~ Error scenarios exist, but written at the REST-API level ("Agent not found → HTTP 404"), not
  tied to a specific tool call
- ✓ One genuine pass: null/empty behavior is actually well-documented ("No findings: Returns
  empty array []")
- ~ Tool-chaining relationships are described in prose (the workflow narrative) but not stated as
  explicit tool-to-tool dependencies

Far more than "3+ items unchecked" — the Tool Identity, Return Values, and Examples sections are
almost entirely empty. Per the checklist's own scoring, this is **Incomplete: request
clarification**, not a partial pass.

### `api-reference-validator` — INCOMPLETE

Same underlying gap. The PRD names 2 example endpoint paths but:
- ✗ No HTTP methods stated explicitly (GET is implied by the `GET /api/...` in one example, not
  confirmed for others)
- ✗ No request parameters documented for any endpoint
- ✗ No response body structure for any endpoint
- ~ Status codes are named (400, 404, 429) but generically, not tied to a specific endpoint, and
  without example response bodies
- ✗ No real request/response example anywhere in the PRD

### `llm-docs-validator` — INCOMPLETE

- ✗ Parameters/outputs not fully specified (same root gap as above)
- ✗ No decision logic for choosing between tools (e.g., when to use `get_unauthorized_access` vs.
  `get_actual_access` — the checklist's own example question, unanswered by this PRD)
- ✗ No concrete example with real values for any tool call
- ✓ Error scenarios are described, though at the REST level, not per-tool

---

## What this run actually found

**The real result, not the one I expected going in:** this PRD is an excellent *product* spec —
better than the validator's own worked example — but it is not a *technical* spec. It tells you
what the feature does, who it's for, and why, in real detail. It does not tell you what
`get_unauthorized_access`'s parameters are, what type `severity` is, or what a real response looks
like. Every validator failed for the same underlying reason: **tool/endpoint-level technical
detail doesn't exist yet, at any of the three levels asked for.**

This mirrors the same lesson from Documenting MCP's Project 1: you cannot draft real reference
documentation from a plausible-sounding gap — the checklists correctly refused to let drafting
proceed on assumed parameter names and made-up example values.

## Stage 2 — Draft generation

**Did not run.** Per each checklist's own scoring rule, "Incomplete" means *request
clarification*, not *draft with flagged assumptions* (that's reserved for "Partially complete,"
1–2 items missing — this run had far more than that in every category). Drafting anyway would
mean inventing parameter names, types, and example values with no source — exactly what this
project's standing rule is to avoid.

## What would need to happen before Stage 2 could run

A technical addendum to the PRD (or a separate spec) naming, for the actual tool surface:
- All 5 tools by name (the PRD names 2; the wider course plan implies `list_ai_identities`,
  `get_declared_scope`, `get_actual_access` also exist)
- Every parameter, typed, with required/optional and defaults
- Every return value's full structure
- At least one real example per tool (or explicitly marked as not-yet-verified, per this
  project's standing rule against inventing plausible examples)

## Conclusion

The pipeline works exactly as designed — it correctly caught a real gap instead of drafting past
it. That's a more useful result than a clean pass would have been: it proves the validators
actually validate, rather than rubber-stamping whatever's handed to them.

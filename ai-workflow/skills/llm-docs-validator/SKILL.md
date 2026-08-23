# LLM Documentation Validator

**Validates and drafts documentation designed for language model ingestion** — providing AI systems with feature knowledge, tool capabilities, and operational context without human intermediaries.

## When to use this skill

Invoke `/llm-docs-validator` when you have:

- A **PRD or feature spec** describing capabilities that AI systems should understand
- **Tool interfaces, APIs, or behavioral specifications** that LLMs need to reason about
- **An existing draft** that needs validation for LLM comprehension and usability

Use this Skill **before adding documentation to an llms.txt file or AI context window** to ensure LLMs can reliably understand and use the information.

## What it does

### Stage 1: LLM-Specific Input Validation

Checks the provided feature specification against an **LLM-focused checklist** (assumes Stage 0 already passed):

✓ All parameters/inputs fully specified — types, constraints, how to obtain values  
✓ All outputs/returns fully described — structure, types, edge cases, nullable fields  
✓ Decision logic documented — when to use this vs. alternatives  
✓ All error scenarios covered — HTTP codes, responses, recovery steps  
✓ No external dependencies — everything self-contained for LLM reasoning  
✓ Real, verified examples — success and error cases  

**Output:** A report of what's present, what's missing, and what could confuse an LLM.

### Stage 2: Draft Generation (if input is complete)

If the PRD passes Stage 1, generates a **draft LLM documentation page** with frontmatter automatically tagged `template: llm-docs`.

**Draft Location**: `ai-workflow/drafts/llm-docs-<feature-name>.md`

Each documentation block includes:
- **Feature description:** What this does and when LLMs should use it
- **Scope and constraints:** Clear boundaries on capability and applicability
- **Decision logic:** How to determine whether to use this feature
- **Complete reference:** Tools, parameters, return values, all self-contained
- **Examples and patterns:** Concrete scenarios showing correct usage
- **Known limitations:** Edge cases, error conditions, and failure modes
- **Relationship to other features:** How this fits into the larger system

The generated draft includes the template tag in frontmatter. When satisfied with the draft, move it to `docs/llm-docs-<feature-name>.md` and commit.

---

## How to invoke

From Claude Code, type:

```
/llm-docs-validator
```

Then provide:

1. **The input:** Paste your PRD, feature spec, or API documentation
2. **Your question:** "Validate this for LLM docs" or "Draft LLM documentation for this feature"
3. **Context:** How this documentation will be used (e.g., "for claude.ai/code context window", "for llms.txt", "for agent system prompt")

---

## What you'll get back

### If the PRD is **incomplete:**

A checklist showing:
- ✓ What's present
- ✗ What's missing (required)
- ? What's unclear (could confuse an LLM)

Example output:
```
VALIDATION REPORT: Unauthorized Agent Access — LLM Documentation

✓ Feature purpose: Detect tool access outside declared scope
✓ Completeness: All parameters, return values, and examples self-contained
✓ Formatting: Consistent use of lists, code blocks, clear section structure
✗ Decision logic: When should an LLM use this API vs. get_actual_access? Not clear.
✓ Constraints: Stated (read-only, no enforcement, lookback window 1-365 days)
✗ Examples: Only one example showing success path. Missing error scenarios.

BLOCKERS:
- Clarify decision logic: when is get_unauthorized_access the right choice?
- Add at least 2 error examples (identity not found, invalid date range)

RECOMMENDATIONS:
- Add a comparison table: get_unauthorized_access vs. get_actual_access (when to use each)
- Explain severity scoring in more detail (what makes something "high" vs. "critical")
```

### If the PRD is **complete:**

A draft LLM documentation page ready for:
1. Human review and editing
2. Integration into llms.txt or context documents
3. Testing with LLM-based tools

---

## Reference materials

- **LLM Docs Checklist:** `/ai-workflow/skills/llm-docs-validator/references/prd-checklist.md`
- **Draft Template:** `/ai-workflow/skills/llm-docs-validator/references/template.md`

---

## Scope & Limitations

**In scope:**
- Validating specs for LLM comprehension
- Drafting self-contained documentation for AI ingestion
- Checking completeness and clarity for automated reasoning
- Identifying ambiguities that would confuse LLMs

**Out of scope:**
- Human-facing documentation (use `/user-guide-validator` or `/mcp-tool-reference-validator` for that)
- LLM system prompt engineering (how to instruct an LLM to use the docs)
- Performance tuning for specific LLM architectures

---

## Notes

- This Skill's Stage 1 is **type-specific only** — it assumes Stage 0 (`/documentation-input-validator`) has already passed. The orchestrator runs Stage 0 once, then Stage 1 only for selected doc types.
- Stage 1 checks only LLM-specific requirements (self-contained specs, decision logic, error scenarios) — it does NOT re-check generic PRD completeness.
- Focuses on **clarity and completeness for automated reasoning**—LLMs need all context upfront; they can't ask clarifying questions.
- LLM-ingestible docs are often shorter and more highly structured than human-facing docs, not longer.

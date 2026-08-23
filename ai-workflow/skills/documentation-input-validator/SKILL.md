# Documentation Input Validator

**Validates PRD/feature specifications for documentation readiness** — generic across all documentation types (MCP tools, user guides, LLM-ingestible docs).

## When to use this skill

Invoke `/documentation-input-validator` when you have a **PRD, feature spec, or raw feature description** and need to know:

- Is the specification complete enough to write documentation from?
- What critical information is missing?
- Should we proceed to drafting, or request clarifications first?

Use this **before invoking type-specific validators** (`/mcp-tool-reference-validator`, `/user-guide-validator`, etc.).

## What it does

Validates that the input PRD contains all essential information needed for ANY documentation type:

✓ Feature/project name and purpose  
✓ Complete scope (what's included, what's not)  
✓ Audience and use case  
✓ Key actors, workflows, or decision points  
✓ Known constraints or limitations  
✓ Any special considerations (security, performance, error cases)  

**Output:** A completeness report showing what's present, what's missing, and what's unclear.

---

## How to invoke

From Claude Code, type:

```
/documentation-input-validator
```

Then provide:

1. **The input:** Paste your PRD, feature spec, Jira issue, or raw feature description
2. **Your question:** "Is this ready for documentation?" or "What's missing?"
3. **Context (optional):** Which doc types you plan to write (MCP, user guide, LLM docs, or "all")

---

## What you'll get back

### Example: Complete PRD

```
VALIDATION REPORT: Unauthorized Agent Access (UAX)

✓ Feature name: "Unauthorized Agent Access detection"
✓ Purpose: Detect when AI agents call tools outside their declared scope
✓ Scope clearly stated: detects violations, reports severity, suggests remediation (does NOT enforce)
✓ Audience: Platform engineers, security teams
✓ Core workflow documented: 1) declare scope 2) monitor calls 3) compare 4) report findings
✓ Constraints documented: read-only tools only; no enforcement capability
✓ Error cases covered: identity not found, invalid scopes, rate limits

RESULT: READY FOR DOCUMENTATION

Next steps:
→ Call /mcp-tool-reference-validator (for tool reference pages)
→ Call /user-guide-validator (for step-by-step guides)
→ Call /llm-docs-validator (for llms.txt)
```

### Example: Incomplete PRD

```
VALIDATION REPORT: Widget Sync Service

✓ Feature name: "Widget Sync Service"
✗ Purpose: Unclear — is this real-time? On-demand? Bidirectional?
✓ Audience: Application developers
✗ Scope: No mention of what "sync" covers. Does it include deletion? Conflicts? Partial updates?
✓ Constraints: Some mentioned (max 1000 widgets per call)
✗ Error cases: Not documented. What happens if source is unavailable? Quota exceeded?
✓ Workflows: One example provided (initial sync)

RESULT: INCOMPLETE — REQUEST CLARIFICATIONS

Blockers (must clarify before drafting):
  - Exactly what does "sync" mean? (initial load? ongoing? bidirectional?)
  - How are conflicts handled?
  - What error states exist and how are they reported?

Recommendations (should clarify for better docs):
  - Performance expectations (latency, throughput)
  - Security/access control (who can sync what?)
  - Versioning strategy (how to handle schema changes?)
```

---

## Reference materials

- **Completeness Checklist:** `/ai-workflow/skills/documentation-input-validator/references/prd-completeness-checklist.md`
- **Example PRDs:** See type-specific validators for domain-specific PRD examples

---

## Scope & Limitations

**In scope:**
- Validating PRD completeness for documentation purposes
- Identifying missing critical information
- Highlighting unclear or ambiguous statements
- Recommending what to clarify before drafting

**Out of scope:**
- Architectural critique (whether the feature should exist or be designed differently)
- Implementation validation (whether it's technically feasible)
- Drafting documentation (use type-specific validators for that)

---

## Notes

- This is **Stage 0** of the documentation validation pipeline. Run it first before type-specific validators.
- Same PRD validation applies to MCP tool docs, user guides, and LLM-ingestible docs.
- If you plan to write multiple documentation types, run this once, then branch to the appropriate type-specific validators.

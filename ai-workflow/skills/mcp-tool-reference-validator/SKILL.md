# MCP Tool Reference Validator

**Validates and drafts MCP tool documentation** against the reordered checklist from Session 8 of the Documenting MCP track.

## When to use this skill

Invoke `/mcp-tool-reference-validator` when you have:

- A **PRD or feature spec** describing one or more MCP tools
- **Raw tool details** (names, purposes, parameters, return values, error cases)
- **An existing draft** that needs validation and improvement

Use this Skill **before opening a PR** to catch gaps in the specification and get an initial draft.

## What it does

### Stage 1: PRD Input Validation

Checks the provided tool specification against a **required elements checklist**:

✓ Tool name and one-sentence purpose  
✓ All parameters listed (required/optional, types, constraints)  
✓ Return value structure described  
✓ At least one real use case or workflow  
✓ Known edge cases, error scenarios, or limitations documented  

**Output:** A report of what's present, what's missing, and what needs clarification before moving forward.

### Stage 2: Draft Generation (if input is complete)

If the PRD passes Stage 1, generates a **draft tool reference page** using the template from Documenting MCP (Track 4, Project 2).

Each tool gets:
- **Purpose:** Why you'd call this tool (not just what it does technically)
- **Parameters:** Every parameter with type, default, constraints, and "where to get it" guidance
- **Returns:** Structure organized by top-level keys, with nested object explanations
- **Example:** A real, verified example response
- **Notes:** Known gaps, untested cases, limits, or inconsistencies

---

## How to invoke

From Claude Code, type:

```
/mcp-tool-reference-validator
```

Then provide:

1. **The input:** Paste your PRD, feature spec, tool details, or existing draft
2. **Your question:** "Validate this PRD" or "Draft the tool reference for these 5 tools"
3. **Context:** Which feature this is for (e.g., "Unauthorized Agent Access", "Widget Sync Service")

---

## What you'll get back

### If the PRD is **incomplete:**

A checklist showing:
- ✓ What's present
- ✗ What's missing (required)
- ? What's unclear (clarification needed)

Example output:
```
VALIDATION REPORT: Unauthorized Agent Access (5 tools)

✓ Tool names: list_ai_identities, get_declared_scope, get_actual_access, get_unauthorized_access, get_remediation_options
✓ Purposes: All 5 stated
✓ Parameters: 4/5 tools fully specified; get_remediation_options is missing parameter details
✗ Return values: 2/5 return structures incomplete (get_declared_scope, get_remediation_options)
✓ Use cases: 2 workflows documented
✓ Error cases: 1/5 tools (get_unauthorized_access); others need coverage

BLOCKERS: 
- Return values for 2 tools must be specified before drafting

RECOMMENDATIONS:
- Add example error responses (currently missing for 4 tools)
- Document severity levels for get_unauthorized_access findings
```
```

### If the PRD is **complete:**

A draft tool reference page with all 5 tools documented, ready for:
1. Human review and editing
2. Commit to a feature branch
3. CI gate validation (Python validators + `validate-mcp-tool-reference`)

---

## Reference materials

- **PRD Checklist:** `/ai-workflow/skills/mcp-tool-reference-validator/references/prd-checklist.md`
- **Draft Template:** `/ai-workflow/skills/mcp-tool-reference-validator/references/template.md`
- **Quality Rubric:** The reordered checklist from `mcp-lab/documenting-mcp/session-8-testing-results.md`

---

## Scope & Limitations

**In scope:**
- Validating tool specs before drafting
- Drafting tool reference pages for MCP servers
- Checking completeness against the 8-item checklist
- Generating examples from specifications

**Out of scope:**
- Auditing completed documentation pages (use `/ridgeline-doc-auditor` for that)
- Architecting the tool surface (e.g., whether you should have 5 tools or 7)
- Writing conceptual overviews or feature narratives (use `/ridgeline-doc-writer` for that)

---

## Notes

- This Skill uses the **generic, reordered MCP tool documentation checklist** from Track 4 (Documenting MCP), so it applies to any feature in the portfolio, not just Ridgeline or UAX.
- Generated drafts follow the template from `documenting-mcp.md` Project 2, ensuring consistency across the portfolio.
- The Skill is **not frozen**; improvements feed back into the MCP documentation guidance as new features use it.

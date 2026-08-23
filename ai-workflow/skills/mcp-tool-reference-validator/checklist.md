# PRD Validation Checklist — MCP Tools (Stage 1)

**Assumes Stage 0 passed.** This checklist checks ONLY MCP-specific requirements.

(Stage 0 already verified: feature name, purpose, scope, audience, workflows, constraints)

## For each tool in the spec:

### Tool Identity & Specification
- [ ] **Tool name specified** (e.g., `list_ai_identities`, not "list AI identities")
- [ ] **Parameters fully specified:**
  - [ ] All parameters listed (none omitted)
  - [ ] Parameter types (string, integer, boolean, array, object, etc.)
  - [ ] Required vs. optional marked for each
  - [ ] Default values shown for optional parameters
  - [ ] Constraints documented (max length, allowed values, format, ranges)
  - [ ] "Where to get it" guidance for parameters from other tools or external sources

### Return Values — Complete Specification
- [ ] **Return structure described** — what shape? (object, array, scalar)
- [ ] **Top-level keys listed and explained** — what each key means
- [ ] **Nested objects documented** — all nested keys explained
- [ ] **Optional/null fields marked** — which can be null or missing?
- [ ] **Data types stated** — string, integer, array of objects, etc.

### Examples — Real & Verified
- [ ] **Real example provided** (not template or schema)
- [ ] **Example includes optional/null values in actual state** (not all fields filled)
- [ ] **Example is realistic** (actual API response, not sanitized)

### Error Scenarios — Complete Coverage
- [ ] **All error cases documented:**
  - [ ] Missing required parameter → HTTP code and response
  - [ ] Invalid parameter (out of bounds/wrong type/wrong format) → HTTP code and response
  - [ ] Resource not found (404) → HTTP code and response
  - [ ] Permission denied (403) → HTTP code and response
  - [ ] Rate limit hit (429) → HTTP code and response
- [ ] **Undocumented cases noted** — "Error behavior for X is not yet tested"
- [ ] **Null/empty behavior explained** — empty array vs. null vs. missing field?

### Workflow Context — Tool Relationships
- [ ] **Relationship to other tools mentioned** — chaining, dependencies, alternatives
- [ ] **Limitations or prerequisites stated** — any setup needed before calling?

---

## Scoring

**Complete (pass to Stage 2):** All items checked. PRD is ready for draft generation.

**Incomplete (request clarification):** 3+ items unchecked in any section. Skill returns a checklist of what's missing.

**Partially complete (conditional pass):** 1-2 items unchecked. Skill notes what's missing but proceeds with draft, flagging assumptions made.

---

## Example: Well-specified tool

```
Tool: get_unauthorized_access
Purpose: Return all instances where an AI identity called tools outside its declared scope, with severity scores.

Parameters:
- identity_id (string, required): The AI identity UUID. Obtain from list_ai_identities results.
- severity_threshold (string, optional, default "medium"): Filter findings by minimum severity. 
  Allowed values: "low", "medium", "high", "critical".
  Constraint: Case-insensitive.
- days_back (integer, optional, default 30): Look back this many days. Min 1, max 365.
  Constraint: Must be positive integer. Values > 365 are capped to 365.

Returns: Array of finding objects, each with:
- finding_id (string): Unique identifier for this unauthorized access instance
- tool_name (string): The tool the identity called (e.g., "upgrade_subscription")
- timestamp (string): ISO 8601 datetime when the call was made
- severity ("low" | "medium" | "high" | "critical"): Severity assigned by Ridgeline's risk model
- context (string): Brief description of why this tool use was flagged (e.g., "tool not in declared scope")
- remediation_options (array): List of remediation_option IDs that apply (see get_remediation_options)

Example response:
[
  {
    "finding_id": "f_abc123",
    "tool_name": "upgrade_subscription",
    "timestamp": "2026-08-23T14:30:00Z",
    "severity": "high",
    "context": "Tool not in declared scope for identity prod-infra-bot",
    "remediation_options": ["opt_1", "opt_2"]
  },
  {
    "finding_id": "f_xyz789",
    "tool_name": "check_storage_usage",
    "timestamp": "2026-08-22T09:15:00Z",
    "severity": "low",
    "context": "Tool in scope but called from unexpected context",
    "remediation_options": ["opt_3"]
  }
]

Known edge cases:
- Empty results: Returns empty array [], not null
- No findings for 30 days: Returns []
- identity_id not found: Returns HTTP 404 with error body {"error": "identity not found", "identity_id": "..."}
- Date parsing: days_back must be integer; fractional values are rejected with validation error

Workflow:
1. Call list_ai_identities to enumerate all identities
2. For each identity, call get_unauthorized_access with a severity threshold
3. For each finding, call get_remediation_options to determine next steps
4. A human reviews findings and chooses remediation
```

This tool passes the checklist and is ready for Stage 2 (draft generation).

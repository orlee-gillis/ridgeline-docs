# PRD Validation Checklist

What the Skill checks for in Stage 1 (input validation) before generating a draft.

## For each tool in the spec:

### Tool Identity
- [ ] **Tool name** (e.g., `list_ai_identities`, not "list AI identities")
- [ ] **One-sentence purpose** — what the tool does and when you'd use it (not just "returns X")

### Parameters
- [ ] **All parameters listed** — none omitted
- [ ] **Parameter types specified** — string, integer, boolean, array, object, etc.
- [ ] **Required vs. optional marked** for each
- [ ] **Default values shown** for optional parameters
- [ ] **Constraints documented** — max length, allowed values, format requirements, etc.
- [ ] **"Where to get it" guidance** for parameters that come from:
  - Another tool's output (e.g., "identity_id from `list_ai_identities`")
  - User knowledge (e.g., "from your dashboard")
  - Derived values (e.g., "ISO 8601 datetime")

### Return Values
- [ ] **Return structure described** — what shape does the response take?
- [ ] **Top-level keys listed and explained** — what does each key mean?
- [ ] **Nested objects documented** — if returns contain nested structures, explain their keys
- [ ] **Optional/null fields noted** — which fields can be null or missing?
- [ ] **Data types stated** — string, integer, array of objects, etc.

### Example Response
- [ ] **Real, verified example provided** — not a template or schema
- [ ] **Example includes optional/null values in their actual state** (not all fields filled in)
- [ ] **Example is realistic** — represents an actual API response, not a sanitized simplified version

### Edge Cases & Errors
- [ ] **Known error scenarios described** — what happens when:
  - Required parameter is missing
  - Parameter is out of bounds
  - Resource doesn't exist (404)
  - Permission denied (403)
  - Rate limit hit
- [ ] **Undocumented cases noted** — "Error behavior for X is not yet tested"
- [ ] **Null/empty behavior explained** — what does the tool return for empty results? Null vs. empty array?

### Workflow Context
- [ ] **Use case or workflow documented** — how does this tool fit into a larger operation?
  - Example: "Call `get_declared_scope` after `list_ai_identities` to find what tools an agent is allowed to use"
- [ ] **Relationship to other tools mentioned** — if this tool chains to another, say so
- [ ] **Limitations or prerequisites stated** — any setup needed before this tool works?

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

# LLM Documentation PRD Validation Checklist

What the Skill checks for in Stage 1 (input validation) before generating a draft.

## Required Elements

### Self-Contained Specification
- [ ] **Feature purpose is clear without external context** — LLMs can't follow links or infer unstated assumptions
- [ ] **All parameters/inputs fully specified** — types, constraints, allowed values, examples
- [ ] **All outputs/returns fully described** — structure, types, nested objects, nullable fields
- [ ] **All dependencies explicitly stated** — "requires X to be set up first" or "depends on Y being defined"

### Clarity for Automated Reasoning
- [ ] **Constraints and limitations explicitly stated** — what this tool does NOT do
- [ ] **Decision logic documented** — when should an LLM choose this feature over alternatives?
- [ ] **Error scenarios described** — what happens on missing input? invalid input? resource not found?
- [ ] **Edge cases and exceptions noted** — special behaviors, fallbacks, or unusual states

### Examples for Correctness
- [ ] **Success-path example provided** — realistic scenario showing correct usage
- [ ] **Error example(s) provided** — realistic scenarios showing what happens when things go wrong
- [ ] **Examples are concrete** — actual values, not placeholders like "[value]" or "..."

### Findability & Relationships
- [ ] **Purpose explains when to use this** — not just what it does, but why you'd call it
- [ ] **Related features/tools mentioned** — how does this fit with alternatives?
- [ ] **Scope boundaries clear** — what belongs to this feature vs. other features

---

## Strongly Recommended (Should-haves)

- [ ] **Heuristics or decision tree** — concrete guidance on "use this when X, use that when Y"
- [ ] **Performance characteristics mentioned** — latency, throughput, or scaling limits if relevant
- [ ] **Version or stability notes** — is this stable API or experimental?
- [ ] **Comparison with alternatives** — if this feature could be confused with another, show the difference
- [ ] **Common patterns or idioms** — examples of how sophisticated uses combine multiple calls

---

## Optional (Nice-to-haves, not blockers)

- [ ] **Pseudocode or algorithm description** — helpful for complex features
- [ ] **Trade-offs explained** — why design it this way vs. alternatives?
- [ ] **Typical time/cost implications** — "this operation usually takes ~100ms" or "costs 1 credit per call"
- [ ] **Accessibility or compatibility notes** — special behaviors on certain platforms or versions

---

## Scoring

**Complete (Ready):** All required elements ✓  
Proceed to Stage 2 draft generation.

**Mostly complete (Proceed with notes):** 1-2 should-haves missing  
Proceed with draft, but note missing heuristics or comparison in output.

**Incomplete (Request clarifications):** 3+ required elements missing or unclear  
Do not proceed; request clarifications before drafting.

---

## Failure Mode: Ambiguous Decision Logic

If the PRD doesn't make clear when to use this feature vs. similar ones:

```
CLARITY ISSUE: Both `get_actual_access` and `get_unauthorized_access` 
return tool calls made by an agent. The PRD doesn't explain WHEN to use which:
- get_actual_access: all calls an agent made?
- get_unauthorized_access: only calls outside declared scope?

Without this clarity, an LLM will guess and likely use the wrong tool. 
Clarify the decision logic: "Use get_actual_access when you need ..., 
use get_unauthorized_access when you need ...".
```

Do not proceed until ambiguity is resolved.

---

## Failure Mode: External Dependencies

If the PRD references unstated assumptions about other systems:

```
DEPENDENCY ISSUE: The spec says "must declare scope in agent management system first" 
but doesn't describe what that system is, how to declare scope, or what format it uses.

An LLM cannot infer this. Either:
1. Include a self-contained description of scope declarations (formats, semantics)
2. Or explicitly state "Scope declaration is managed by [system] (not documented here)"

Do not proceed until dependencies are clear.
```

---

## Example: Complete LLM Docs PRD

```
Feature: get_unauthorized_access

Purpose: Return all instances where an AI identity called tools 
outside its declared scope. Use this when investigating which agents 
or services have made unauthorized API calls.

Constraints (important for LLMs):
- Read-only: Returns data only, does not enforce or block future calls
- Lookback window: 1-365 days (not infinite history)
- Limit: Max 1000 findings per call
- Prerequisite: Identity must be registered with Ridgeline (not created by this API)

Parameters:
- identity_id (string, required): UUID of the agent. Obtain from list_ai_identities.
- severity_threshold (string, optional, default "medium"): 
  Filter to findings with this severity or higher.
  Allowed values: "low", "medium", "high", "critical" (case-insensitive)
- days_back (integer, optional, default 30): 
  Look back this many days. Min 1, max 365.
  Values > 365 are clamped to 365.

Returns: Array of findings, each with:
- finding_id (string): Unique ID for this instance
- tool_name (string): The tool the identity called (e.g., "upgrade_subscription")
- timestamp (ISO 8601): When the call was made
- severity ("low" | "medium" | "high" | "critical"): Risk level assigned by Ridgeline
- context (string): Why flagged (e.g., "Tool not in declared scope")
- remediation_options (array of strings): Option IDs to choose from (see get_remediation_options)

Decision logic (when to use this):
- Use get_unauthorized_access when: You need to know what unauthorized calls an agent made
- Use get_actual_access instead if: You want ALL calls (authorized + unauthorized)
- Use get_declared_scope instead if: You want to see what the agent IS ALLOWED to call (not what it actually called)

Error handling:
- identity_id not found: HTTP 404 {"error": "identity not found", "identity_id": "..."}
- Invalid severity_threshold: HTTP 400 {"error": "invalid severity", "allowed": ["low", "medium", "high", "critical"]}
- Invalid days_back (< 1 or non-integer): HTTP 400 {"error": "invalid days_back"}
- Rate limit exceeded: HTTP 429 {"error": "rate limit exceeded", "retry_after_seconds": 60}
- Empty results: Returns [] (not null)

Example success case:
- Call: get_unauthorized_access(identity_id="id_prod-bot", severity_threshold="high", days_back=30)
- Returns: Array with 2 findings for that identity in the last 30 days with severity >= high

Example error case:
- Call: get_unauthorized_access(identity_id="id_does_not_exist")
- Returns: HTTP 404 with "identity not found"

Patterns for LLM usage:
1. List all identities → get_unauthorized_access for each → aggregate findings
2. Find high-risk findings → get_remediation_options → recommend action
3. Monitor over time by calling daily and tracking new findings vs. old findings

Notes for LLMs:
- Empty array [] means no unauthorized access found (good sign)
- Null remediation_options array is not expected; always present
- Severity is assigned by Ridgeline's risk model (not the user); LLM cannot override
- Timestamp is when the call was made, not when the finding was created
- If the same tool is called multiple times, each call generates a separate finding
```

✓ This PRD is complete for LLM documentation.

---

## Example: Incomplete LLM Docs PRD

```
Feature: check_access

Purpose: Check tool access.

Parameters: identity, optional date range

Returns: findings or null

Error cases: Not documented
```

✗ Missing:
- Self-contained specification (what is "identity"? format? how to obtain?)
- Clear decision logic (when to use check_access vs. other tools?)
- Return value structure (what's in findings? types?)
- Error scenarios (what errors can occur? HTTP codes?)
- Examples (success + error cases)
- Constraints and limitations

Request clarifications before proceeding.

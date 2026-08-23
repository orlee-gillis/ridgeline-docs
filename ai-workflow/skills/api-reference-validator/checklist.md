# API Reference Validator Checklist — REST APIs (Stage 1)

**Assumes Stage 0 passed.** This checklist checks ONLY REST-API-specific requirements.

(Stage 0 already verified: feature name, purpose, scope, audience, workflows, constraints)

## Required Elements

### Endpoint Specification
- [ ] **All endpoints listed** with:
  - [ ] HTTP method (GET, POST, PUT, DELETE, PATCH, etc.)
  - [ ] Path/route (e.g., `/api/get_unauthorized_access`)
  - [ ] One-sentence description (what this endpoint does, when you'd call it)

### Request Parameters — Complete Specification
- [ ] **All parameters documented** for each endpoint:
  - [ ] Parameter name and location (query, path, body)
  - [ ] Data type (string, integer, boolean, array, object, etc.)
  - [ ] Required vs. optional marked
  - [ ] Default values (if applicable)
  - [ ] Constraints (max length, min/max value, allowed values, format)
  - [ ] "Where to get it" guidance (if value comes from another API call or user knowledge)

### Response Structure — Complete Specification
- [ ] **Response body structure documented:**
  - [ ] Top-level keys/fields listed
  - [ ] Data types for each field (string, integer, array of objects, etc.)
  - [ ] Optional/nullable fields marked
  - [ ] Nested object structures explained
  - [ ] Relationship to request parameters (e.g., "returns array of items matching filter")

### HTTP Status Codes — All Cases
- [ ] **Success response(s):**
  - [ ] 200 (OK) or 201 (Created) documented
  - [ ] Response schema for success case
- [ ] **Client error responses:**
  - [ ] 400 (Bad Request) — when? what causes it?
  - [ ] 401 (Unauthorized) — if authentication required
  - [ ] 403 (Forbidden) — if authorization required
  - [ ] 404 (Not Found) — when does endpoint return this?
- [ ] **Server error responses:**
  - [ ] 429 (Too Many Requests) — rate limit details
  - [ ] 500 (Internal Server Error) — what causes it?
  - [ ] Other error codes specific to this endpoint

### Error Response Format
- [ ] **Error responses documented:**
  - [ ] Error response body structure (e.g., `{"error": "...", "details": {...}}`)
  - [ ] What fields are included (error code, message, details)
  - [ ] How to interpret error responses

### Examples — Real & Verified
- [ ] **Success case example:**
  - [ ] Real, verified request (actual HTTP method, path, parameters)
  - [ ] Real, verified response body (actual JSON with real values)
- [ ] **Error case examples (at least 2):**
  - [ ] 400 Bad Request example (what request causes it, what error response looks like)
  - [ ] 404 Not Found example (what happens when resource doesn't exist)
  - [ ] 429 Rate Limited example (if applicable; what response looks like)
- [ ] **Examples include optional/null fields in actual state** (not all fields filled in)

### Authentication & Authorization
- [ ] **Authentication requirement documented:**
  - [ ] Is authentication required? (yes/no)
  - [ ] If yes: what auth method? (API key, Bearer token, OAuth, etc.)
  - [ ] How is auth passed? (header, query param, etc.)
- [ ] **Authorization requirement documented:**
  - [ ] Are there permission checks? (yes/no)
  - [ ] If yes: what permissions are required?
  - [ ] What happens if user lacks permission? (403 error with what message?)

### Rate Limiting & Constraints
- [ ] **Rate limits documented:**
  - [ ] Calls per minute/hour (if applicable)
  - [ ] What happens when rate limit exceeded (429 response format)
  - [ ] How to know when you're rate limited
- [ ] **Other constraints documented:**
  - [ ] Payload size limits
  - [ ] Query complexity limits
  - [ ] Timeout values
  - [ ] Pagination limits (if applicable)

---

## Strongly Recommended (Should-haves)

- [ ] **Response time/performance expectations** — typical latency for this endpoint
- [ ] **Pagination documentation** (if applicable) — how to fetch large result sets
- [ ] **Filtering/sorting parameters** — how to filter or sort results
- [ ] **Related endpoints mentioned** — how does this endpoint fit with others?
- [ ] **Deprecation notices** — is this endpoint stable or deprecated?
- [ ] **CORS information** — if used in browser, what origins are allowed?

---

## Optional (Nice-to-haves)

- [ ] **Request body examples** — not just responses, but what to send
- [ ] **cURL or Postman examples** — ready-to-run command examples
- [ ] **API versioning notes** — version info if applicable
- [ ] **Changelog** — recent changes to this endpoint
- [ ] **Common pitfalls or gotchas** — what do users often get wrong?

---

## Scoring

**Complete (Ready):** All required elements ✓  
Proceed to Stage 2 draft generation.

**Mostly complete (Proceed with notes):** 1-2 should-haves missing  
Proceed with draft, but note missing performance expectations or pagination in output.

**Incomplete (Request clarifications):** 3+ required elements missing or unclear  
Do not proceed; request clarifications before drafting.

---

## Failure Mode: Missing Error Examples

If the PRD documents error codes but provides NO examples of error responses:

```
CLARITY ISSUE: The spec says "Returns 400 Bad Request when severity_threshold is invalid"
but does not show what a 400 response looks like.

An API user cannot test their error handling without knowing the response format.
Either:
1. Provide a real example of a 400 response for invalid severity_threshold
2. Or document the response schema that applies to all error responses

Do not proceed until error examples are provided.
```

---

## Failure Mode: Ambiguous Parameter Constraints

If parameters are documented but constraints are vague:

```
CLARITY ISSUE: Parameter days_back is documented as "integer" but no constraints stated.
- Can it be negative?
- What's the maximum? Minimum?
- What happens if user passes 1000?

Without this clarity, API users will encounter unexpected behavior.
Document: "Integer, minimum 1, maximum 365. Values > 365 are clamped to 365."
```

---

## Example: Well-Specified Endpoint

```
Endpoint: GET /api/get_unauthorized_access

Description: Retrieve all instances where an AI identity called tools outside 
its declared scope, with severity scores and remediation options.

Request Parameters:
- identity_id (string, required, path): UUID of the AI identity
  Obtain from GET /api/list_ai_identities
- severity_threshold (string, optional, query, default "medium")
  Allowed values: "low", "medium", "high", "critical" (case-insensitive)
- days_back (integer, optional, query, default 30)
  Lookback window. Min 1, max 365. Values > 365 clamped to 365.

Response (200 OK):
- Array of finding objects, each with:
  - finding_id (string): Unique identifier
  - tool_name (string): Tool the identity called
  - timestamp (ISO 8601 string): When the call was made
  - severity ("low" | "medium" | "high" | "critical")
  - context (string): Why flagged
  - remediation_options (array of strings): Option IDs

Example Request:
GET /api/get_unauthorized_access?identity_id=id_prod-bot&severity_threshold=high&days_back=7

Example Success Response (200):
[
  {
    "finding_id": "f_abc123",
    "tool_name": "upgrade_subscription",
    "timestamp": "2026-08-23T14:30:00Z",
    "severity": "critical",
    "context": "Tool not in declared scope",
    "remediation_options": ["opt_revoke", "opt_update"]
  }
]

Example Error Response (404):
HTTP 404
{
  "error": "identity_not_found",
  "identity_id": "id_does_not_exist",
  "hint": "Use GET /api/list_ai_identities to find valid identities"
}

Example Error Response (400):
HTTP 400
{
  "error": "invalid_parameter",
  "parameter": "severity_threshold",
  "constraint": "must be 'low', 'medium', 'high', or 'critical'",
  "received": "extreme"
}

Example Error Response (429):
HTTP 429
{
  "error": "rate_limit_exceeded",
  "limit": "100 calls per minute",
  "retry_after_seconds": 60
}

Constraints:
- Rate limit: 100 calls/minute per identity
- Result limit: Max 1000 findings per call
- Latency: ~5 minute delay before findings appear

Authentication: Bearer token in Authorization header
```

✓ This endpoint specification is complete and ready for draft generation.

---

## Example: Incomplete Endpoint

```
Endpoint: GET /api/check_access

Description: Check tool access.

Request: identity_id (required), optional date range

Response: findings or null

Error cases: Not documented
```

✗ Missing:
- What is the exact path? (/api/check_access? /check_access?)
- What HTTP method? (GET? POST?)
- Response schema (what's in findings? types?)
- Success HTTP code (200? 201?)
- Error codes and responses (what happens on invalid input? 404? 400?)
- Examples (success and error cases)
- Error response format (how are errors structured?)

Request clarifications before proceeding.

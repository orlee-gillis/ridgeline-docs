# API Reference Validator

**Validates and drafts REST API reference documentation** — endpoint specifications, request/response structures, error handling, and example calls.

## When to use this skill

Invoke `/api-reference-validator` when you have:

- A **PRD or feature spec** describing a REST API (HTTP endpoints, methods, parameters, responses)
- **Raw API details** (endpoints, methods, parameters, response types, error codes)
- **An existing draft** that needs validation for completeness and clarity

Use this Skill **before opening a PR** to ensure API documentation is complete and accurate.

## What it does

### Stage 1: REST API Specification Validation

Checks the provided API specification against a **REST-API-specific checklist** (assumes Stage 0 already passed):

✓ All endpoints documented (paths, HTTP methods)  
✓ Request parameters fully specified (query, path, body, types, constraints)  
✓ Response structures described (status codes, body schema, nested objects)  
✓ Real, verified examples (success + error cases with actual HTTP)  
✓ Authentication and authorization requirements  
✓ Error scenarios and HTTP status codes  

**Output:** A report of what's present, what's missing, and what needs clarification.

### Stage 2: Draft Generation (if input is complete)

If the PRD passes Stage 1, generates a **draft API reference page** using a REST-focused template.

Each endpoint includes:
- **Method & Path:** HTTP verb and route (e.g., `GET /api/get_unauthorized_access`)
- **Description:** What this endpoint does and when you'd call it
- **Request:** Query/path/body parameters with types, defaults, constraints
- **Response:** Status codes, response schema, nested objects, nullable fields
- **Example:** Real, verified request and response (success + error)
- **Notes:** Error handling, rate limits, edge cases, gotchas

---

## How to invoke

From Claude Code, type:

```
/api-reference-validator
```

Then provide:

1. **The input:** Paste your PRD, feature spec, or API details
2. **Your question:** "Validate this API spec" or "Draft API reference for these endpoints"
3. **Context:** Which feature this is for (e.g., "Unauthorized Agent Access", "Data Export Service")

---

## What you'll get back

### If the PRD is **incomplete:**

A checklist showing:
- ✓ What's present
- ✗ What's missing (required)
- ? What's unclear (clarification needed)

Example output:
```
VALIDATION REPORT: Unauthorized Agent Access — API Reference

✓ Endpoints: get_unauthorized_access, get_remediation_options documented
✓ Methods: GET specified for both
✓ Request parameters: identity_id, severity_threshold, days_back specified
✗ Response schema: get_unauthorized_access returns described, but field types not stated (string? array of objects?)
✓ Error codes: 404, 400, 429 documented
✗ Examples: Only success case shown; missing 404 and 429 error examples

BLOCKERS:
- Response schema must specify field types and nested structure
- Error examples needed (404, 429)

RECOMMENDATIONS:
- Clarify nullable fields (is last_activity nullable?)
- Add rate limit documentation (when do 429s occur?)
```

### If the PRD is **complete:**

A draft API reference page ready for:
1. Human review and editing
2. Commit to a feature branch
3. Integration into published documentation

---

## Reference materials

- **API Checklist:** `/ai-workflow/skills/api-reference-validator/references/prd-checklist.md`
- **Draft Template:** `/ai-workflow/skills/api-reference-validator/references/template.md`

---

## Scope & Limitations

**In scope:**
- Validating REST API specifications
- Drafting API reference pages
- Checking completeness of endpoint, parameter, and response documentation
- Error scenario documentation
- Example requests and responses

**Out of scope:**
- OpenAPI/Swagger spec generation (use OpenAPI tools for that)
- GraphQL schema validation (use `/graphql-schema-validator` for that)
- gRPC service documentation (separate validator)
- Performance testing or load testing
- Security audit (beyond documenting auth/authz requirements)

---

## Notes

- This Skill's Stage 1 is **type-specific only** — it assumes Stage 0 (`/documentation-input-validator`) has already passed. The orchestrator runs Stage 0 once, then Stage 1 only for selected doc types.
- Stage 1 checks only REST-API-specific requirements (endpoints, parameters, responses, examples) — it does NOT re-check generic PRD completeness.
- Focuses on **HTTP REST APIs** (JSON over HTTP); GraphQL and gRPC are separate validators.
- Works best when paired with `/documentation-input-validator` (Stage 0) first.

# PRD: Unauthorized Agent Access Detection

**Feature Name:** Unauthorized Agent Access (UAX) Detection  
**Source:** Customer request #CUST-2026-0847 (AcmeCorp Security Team) + Internal Security Initiative  
**Phase:** MVP (Phase 1)  
**Status:** Ready for Documentation  
**Date:** August 2026

---

## Customer Request Citation

**From:** Sarah Chen, Security Lead at AcmeCorp  
**Date:** July 15, 2026  
**Request ID:** CUST-2026-0847  
**Subject:** "We need to audit when our AI agents call tools they shouldn't"

> "We've deployed several AI agents to automate infrastructure tasks. Each agent has a specific scope of tools it's allowed to call. But we have no visibility into whether agents are respecting those boundaries. Last month, one agent called `upgrade_subscription` when it should only be calling infrastructure tools. We didn't catch it for 3 days. We need a system that:
> 1. Tells us when an agent calls a tool outside its scope
> 2. Shows us when it happened and from where
> 3. Lets us decide whether to revoke access or update the scope declaration
> 4. Does this WITHOUT blocking the agent (read-only reporting, not enforcement)"

---

## Feature Overview

**Feature Name:** Unauthorized Agent Access (UAX) Detection

**One-Sentence Purpose:** Detect when AI agents call tools outside their declared scope, assign severity, and recommend remediation actions.

**Why Now:** As AI agents increasingly automate critical infrastructure tasks, visibility into policy violations is essential for security and compliance.

---

## Scope

### What's Included (Scope)

1. **Detection:** Identify when an agent calls a tool not in its declared scope
2. **Severity Scoring:** Assign risk levels (low/medium/high/critical) based on tool sensitivity and context
3. **Reporting:** Present findings in a structured format with context and remediation options
4. **Remediation Guidance:** Suggest actions (revoke access, update scope, investigate context) without enforcing them
5. **Historical Analysis:** Look back 1-365 days to find past violations
6. **Filtering:** Filter by severity threshold, date range, identity

### What's Excluded (Not Scope)

- **Enforcement:** This system does NOT block or prevent unauthorized calls (read-only reporting only)
- **Scope Management:** Does NOT manage or declare agent scope (done by admin console elsewhere)
- **Real-time Blocking:** Does NOT prevent calls in real-time (detection is ~5 minute latency)
- **Auto-remediation:** Does NOT automatically revoke access or update scope (human approval required)
- **Scope Inference:** Does NOT infer what an agent should be allowed to call (scope is explicit elsewhere)

---

## Audience

**Primary Users:**
- Security teams (finding violations, recommending action)
- Platform engineers (managing agent policies, investigating violations)

**Secondary Users:**
- Compliance officers (audit trails, historical reporting)
- AI engineers (understanding agent behavior and policy violations)

**User Goals:**
- "Can I find what tools this agent called that it shouldn't have?"
- "How severe is this violation?" 
- "What should I do about it?"
- "Is this a pattern or a one-time mistake?"

---

## Core Workflow

### Happy Path: Detect and Review a Violation

1. **Admin declares scope** (elsewhere)
   - Agent `prod-infra-bot` is allowed to call: `check_resource_utilization`, `get_scaling_policy`, `update_scaling_settings`

2. **Agent makes a call** (over time)
   - At 2026-08-23 14:30 UTC, `prod-infra-bot` calls `upgrade_subscription`
   - This tool is not in the declared scope → violation detected

3. **Ridgeline detects and scores** (automated, ~5 min latency)
   - Finding created: `upgrade_subscription` called outside scope
   - Severity: `high` (subscription management is sensitive)
   - Context: Call made from IP 10.0.1.5 (CI/CD runner)

4. **Security team reviews**
   - Sees the finding in the dashboard
   - Reads the context: timestamp, source IP, exact parameters
   - Recognizes the IP: "That's our deployment pipeline"

5. **Security team decides**
   - Option A: "This was a mistake in our deploy script. Revoke access for now."
   - Option B: "Actually, the agent should be allowed to do this. Update the scope declaration."
   - Option C: "This is suspicious. Investigate further."
   - → Takes action (no enforcement by system, human approval required)

6. **Finding status updates**
   - Status: "Remediated" (action taken) or "Reviewed" (false positive, no action)
   - Audit trail preserved for compliance

---

## Key Actors and Entities

### Actors
- **AI Agent:** A service account, model deployment, or autonomous system that makes tool calls
- **Tool:** An API endpoint, microservice, or capability the agent can invoke
- **Security Team:** Humans who review findings and decide on remediation
- **Admin:** System that manages agent scope declarations (outside this system)

### Entities
- **AI Identity:** Unique identifier for an agent (UUID, name)
- **Tool Name:** The specific tool/API endpoint called (e.g., `upgrade_subscription`)
- **Declared Scope:** List of tools the agent is allowed to call (managed elsewhere)
- **Actual Access:** Log of tools the agent actually called (detected by Ridgeline)
- **Finding:** A violation instance (agent called tool outside scope)
- **Severity:** Risk level (low/medium/high/critical) assigned by risk model
- **Remediation Option:** An actionable step (revoke access, update scope, etc.)

---

## Known Constraints and Limitations

### Performance Constraints
- **Latency:** ~5 minute delay before findings are generated (not real-time)
- **Lookback Window:** 1-365 days maximum (older findings archived)
- **Result Limit:** Max 1000 findings per API call (pagination not yet supported)
- **Rate Limit:** 100 calls/minute per identity

### Technical Constraints
- **Read-Only:** System detects and reports only; cannot enforce or prevent calls
- **Scope Definition:** Scope is managed by separate system; this system reads it but cannot modify it
- **Call Attributes:** Only detects tool name and timestamp; cannot capture method or parameters for now

### Business Constraints
- **Approval Requirement:** All remediation requires human approval (no auto-actions)
- **Audit Trail:** All findings and actions logged for compliance
- **Access Control:** Only security teams and platform engineers can access findings

---

## Error Scenarios and Failure Modes

### Normal Error Cases
- **Agent not found:** Agent was deleted or never registered → HTTP 404
- **Invalid date range:** `days_back` out of bounds → HTTP 400
- **Rate limit exceeded:** Too many calls in short period → HTTP 429
- **No findings:** Agent made no unauthorized calls in period → Returns empty array []

### Edge Cases
- **Scope updated after call:** Finding shows violation for tool now in scope → Human must review timestamp
- **False positive:** Tool is called for legitimate reason outside normal policy → Mark "reviewed" to dismiss
- **Mass violations:** Single agent calls many unauthorized tools → Suggests checking scope or agent credentials

---

## Success Criteria

Users will succeed when they can:

1. **Identify violations:** "Which tools did my agent call that it shouldn't have?"
2. **Understand context:** "When did this happen? From where? Why is it a violation?"
3. **Prioritize response:** "Which violations are critical vs. low-risk?"
4. **Take action:** "What are my options? Revoke? Update scope? Investigate further?"
5. **Audit compliance:** "Can I prove we found and handled this violation?"

---

## Example Scenario (Concrete)

**Scenario:** You're a security engineer at AcmeCorp. You deploy an AI agent called `prod-infra-bot` to automate scaling decisions.

**Setup:**
- Agent can call: `check_resource_utilization`, `get_scaling_policy`, `update_scaling_settings`
- Agent is managed by cloud admin console (separate from Ridgeline)

**What happens:**
1. On Tuesday at 14:30, an engineer deploys a new version of the automation script
2. Due to a bug, the script calls `upgrade_subscription` (should have been filtered out)
3. Ridgeline detects this 5 minutes later
4. A finding is created: severity "high", reason "tool not in declared scope"
5. Wednesday morning, you review findings and see this one
6. You click "View context" and see the call came from your deployment IP
7. You recognize the bug immediately
8. You click "Mark as reviewed" and add note: "False positive - bug in deployment v2.4.3, fixed in v2.4.4"
9. The finding status updates to "Reviewed"
10. You push the fixed version
11. No more findings from this agent on this tool

**Success:** You caught the violation, investigated, understood the context, and took action. Audit trail is complete.

---

## Relationship to Other Systems

- **Agent Management:** Scope is declared in admin console (not Ridgeline)
- **Logging System:** Tool calls are logged by observability system; Ridgeline queries this data
- **Alerting:** Findings can be routed to security team via email/Slack (future integration)
- **Remediation Tools:** Scope updates are handled by admin console (future integration)

---

## Future Phases (Not in MVP)

- **Phase 2:** User guides for security teams on how to review and remediate findings
- **Phase 3:** LLM integration so AI agents understand their own scope and flag violations
- **Real-time Blocking:** Enforcement option (block calls outside scope before they execute)
- **Auto-remediation:** Automatic revocation of access to overly-permissive agents

---

## Documentation Needs for MVP

Based on this PRD, what documentation should we create?

**This phase needs:**
1. **API Reference Documentation** — Developers need to understand the REST API
   - What endpoints exist (`GET /api/get_unauthorized_access`, `GET /api/get_remediation_options`, etc.)
   - What parameters they accept (query, path, headers)
   - What responses they return (status codes, schemas, examples)
   - Error handling and HTTP status codes

2. **MCP Tool Reference Documentation** — Claude and AI agents need to understand the tool definitions
   - Tool names and purposes
   - Parameters and constraints
   - Return value structures
   - Error scenarios and recovery
   - Real usage examples

3. **LLM Documentation** — AI agents need to understand this capability autonomously
   - What this capability does (detect unauthorized tool access)
   - When AI agents should use it (security auditing workflows)
   - How it integrates with other security tools
   - Decision logic and examples


# PRD Completeness Checklist

What Stage 0 validates — generic across all documentation types.

---

## Required Elements

**Feature Identity**
- [ ] Feature name (official name, not "the new thing")
- [ ] One-sentence purpose (what problem does it solve?)
- [ ] Link to source (Jira ticket, GitHub issue, design doc, or explicit "fictional for portfolio")

**Scope**
- [ ] What's included (core functionality)
- [ ] What's NOT included (explicit boundaries)
- [ ] Example: "Detects unauthorized calls (does NOT prevent or enforce them)"

**Audience**
- [ ] Who uses this? (end users, developers, admins, all of the above?)
- [ ] What's their goal? (what do they want to accomplish with this feature?)

**Core Workflow or Use Case**
- [ ] At least one complete workflow or example scenario
- [ ] Should show the happy path end-to-end
- [ ] Example: "1) Admin declares tool scope 2) agent calls tool 3) system compares 4) report is generated"

**Key Actors, Objects, or Entities**
- [ ] What things are being acted on? (sites, agents, identities, widgets, etc.)
- [ ] Who/what performs actions? (users, systems, bots)

**Known Constraints or Limitations**
- [ ] Performance limits (throughput, latency, max items, etc.)
- [ ] Technical constraints (read-only, no async, etc.)
- [ ] Business constraints (requires subscription tier, etc.)

---

## Strongly Recommended (Should-haves)

- [ ] Error scenarios or failure modes documented
- [ ] Security or access control mentioned (who can do what?)
- [ ] Any assumptions or dependencies (requires X to be set up first)
- [ ] Versioning or backward-compatibility notes (if relevant)

---

## Optional (Nice-to-haves, not blockers)

- [ ] Performance expectations or benchmarks
- [ ] Design rationale (why design it this way vs. alternatives?)
- [ ] Future extensibility (what might come next?)
- [ ] Visual diagram or mockup
- [ ] Links to related features

---

## Scoring

**Complete (Ready):** All required elements ✓  
- Proceed to type-specific validators

**Mostly complete (Proceed with notes):** 1-2 should-haves missing  
- Proceed, but document assumptions in drafts

**Incomplete (Request clarifications):** 3+ required elements missing or unclear  
- Do not proceed; request clarifications before drafting

---

## Failure Mode: Ambiguous or Contradictory

If the PRD contains **contradictory statements** (e.g., "read-only tools" AND "can modify permissions"), flag this explicitly:

```
CONFLICT: The spec states tools are "read-only" but also mentions "grant tool access." 
These contradict. Clarify: can this feature modify tool permissions or only report violations?
```

Do not proceed until contradiction is resolved.

---

## Example: Complete PRD

```
Feature: Unauthorized Agent Access Detection

Purpose: Detect when AI agents call tools outside their declared scope, 
with severity scoring and remediation options.

Scope:
- INCLUDES: Detect calls outside scope, score severity, suggest remediation
- INCLUDES: Report findings in structured format
- EXCLUDES: Enforce or prevent unauthorized calls (read-only reporting only)
- EXCLUDES: Manage agent scope directly (done by humans on agent's own system)

Audience: Platform engineers, security teams managing AI agents

Core Workflow:
1. Admin declares which tools an agent is allowed to call (managed elsewhere)
2. Ridgeline watches the agent's actual tool calls over time
3. Ridgeline compares declared scope vs. actual calls
4. For any mismatch, assigns severity (low/medium/high/critical)
5. Reports finding with remediation options (revoke access, or update declaration)
6. Human approves remediation (Ridgeline does not execute it)

Key Entities:
- AI identity (agent, service account, model deployment)
- Tool name (what the agent tried to call)
- Declared scope (what it's allowed to call)
- Actual access (what it really called)
- Finding (a violation, with severity and remediation options)

Constraints:
- Read-only tools only (no enforcement, no modification)
- Lookback window: 1-365 days (default 30)
- Max findings per call: 1000
- Rate limit: 100 calls/minute per identity

Error Scenarios:
- Identity not found → HTTP 404
- Invalid lookback window → HTTP 400
- Rate limit exceeded → HTTP 429
```

✓ This PRD is complete and ready for documentation.
```

---

## Example: Incomplete PRD

```
Feature: Widget Sync Service

Purpose: Sync widgets.

Scope: (not stated)

Audience: Developers

Workflow: Widgets get synced.
```

✗ Missing:
- What does "sync" mean exactly?
- Scope boundaries (bidirectional? deletion? conflicts?)
- Error handling
- Constraints
- Example scenario

Request clarifications before proceeding.

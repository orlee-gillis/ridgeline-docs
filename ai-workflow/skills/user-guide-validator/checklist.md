# User Guide PRD Validation Checklist — User-Facing Tasks (Stage 1)

**Assumes Stage 0 passed.** This checklist checks ONLY user-guide-specific requirements.

(Stage 0 already verified: feature name, purpose, scope, audience, at least one workflow, constraints)

## Required Elements

### Task Workflow — User-Oriented Details
- [ ] **Complete task workflow documented** — end-to-end steps from start to success
- [ ] **Decision points noted** — what choices does the user make? Which path applies to them?
- [ ] **Normal (happy) path clearly separated** from error handling
- [ ] **Step-by-step instructions** — each step is atomic and actionable
- [ ] **Prerequisite setup/permissions** — what needs to be true before user starts? (beyond general setup from Stage 0)

### Success Criteria & Interpretation
- [ ] **Success criteria defined** — how does user know the task succeeded?
- [ ] **How to interpret results** — what does the output/screen/status mean?
- [ ] **User skill level noted** — beginner/intermediate/advanced? (refines how to explain steps)

### Failure Handling — Troubleshooting
- [ ] **Common failure modes described** — what could go wrong during this task?
- [ ] **Troubleshooting guidance** — for each failure, how does user recover?
- [ ] **Error messages explained** — what do error states mean to the user?
- [ ] **When to escalate** — what should user do if troubleshooting doesn't help?

### Real-World Example
- [ ] **Concrete scenario with realistic context** (not bare-bones template)
- [ ] **Related tasks or next steps** — how does this task fit into larger workflows?

---

## Strongly Recommended (Should-haves)

- [ ] **Audience skill level noted** — is this for beginners, intermediate, or advanced users?
- [ ] **Time estimate** — how long should this task take?
- [ ] **Permissions or access requirements** — does the user need specific permissions?
- [ ] **Decision tree or flowchart** — when you have multiple paths, showing which path for which scenario
- [ ] **Interpret results section** — once the task is done, how does the user interpret what they see?

---

## Optional (Nice-to-haves, not blockers)

- [ ] **Video or screenshot references** — visual aids
- [ ] **API calls or configuration shown** — helpful for developers, optional for end users
- [ ] **Performance expectations** — "this takes ~30 seconds" or "results update in real-time"
- [ ] **Glossary or term definitions** — for domain-specific language
- [ ] **FAQ section** — frequently asked questions not covered in troubleshooting

---

## Scoring

**Complete (Ready):** All required elements ✓  
Proceed to Stage 2 draft generation.

**Mostly complete (Proceed with notes):** 1-2 should-haves missing  
Proceed with draft, but note assumptions in output.

**Incomplete (Request clarifications):** 3+ required elements missing or unclear  
Do not proceed; request clarifications before drafting.

---

## Failure Mode: Unclear Audience or Goal

If the PRD targets multiple audiences without clarity on who the guide is FOR:

```
CONFLICT: The spec mentions both security teams (who review findings) 
and developers (who set up tool scope declarations). 
This is TWO DIFFERENT GUIDES. Clarify: Is this guide for security teams 
reviewing findings, OR for developers setting up scope, OR a two-part guide?
```

Do not proceed until this is resolved.

---

## Example: Complete User Guide PRD

```
Feature: Reviewing Unauthorized Access Findings

User Goal: A security team member reviews a list of tool access violations 
and decides whether to escalate or revoke access.

Audience: Security teams, platform engineers (non-developers)
Skill level: Intermediate (understands "tool scope", "agent", "permission")
Time to complete: 5 minutes per finding

Prerequisites:
- User has access to the Ridgeline dashboard
- User understands that "tool scope" = which tools an agent is allowed to call
- User knows their organization's naming conventions for agents

Main Workflow:
1. Log into Ridgeline dashboard
2. Navigate to "Findings" section
3. Filter by severity (optional) and date range
4. For each finding:
   a. Read the finding summary: which agent, which tool, why flagged
   b. Click "View context" to see when/how the call was made
   c. Decide: is this a violation (unauthorized call) or a false positive?
   d. If violation: choose remediation (revoke access, or update scope declaration)
   e. If false positive: mark as reviewed
5. Complete action (revoke/update/mark reviewed)
6. Check status: finding now shows "in review" or "remediated"

Success Criteria:
- User can identify which agent made the unauthorized call
- User can see WHEN and HOW the call was made
- User can initiate remediation without contacting support

Common Issues:
- Q: I see a lot of "low severity" findings. Should I fix them all?
  A: No. Focus on "high" and "critical" first. "Low" severity are often false positives from monitoring changes.
  
- Q: A finding says my agent called "check_storage_usage" but we declared that in scope. Why is it flagged?
  A: This can happen if scope was updated AFTER the call was made. Check the timestamp on the finding; if it predates your scope change, it's a false positive. Mark it "reviewed" and it won't reappear.

- Q: How do I know what the agent is "supposed" to call?
  A: You don't see that in Findings. Go to Settings → Agents and click the agent's name to see its declared scope.

Related Tasks:
- How to update an agent's tool scope (in Settings)
- How to interpret severity levels (reference page)
- How to set up an alert for critical findings (setup guide)
```

✓ This PRD is complete and ready for draft generation.

---

## Example: Incomplete User Guide PRD

```
Feature: Tool Access Reporting

Goal: Users run a report on tool access.

Audience: Platform engineers
```

✗ Missing:
- What specific task are users trying to accomplish? (report on what?)
- Workflow steps (how do they create the report? what options do they choose?)
- Prerequisites (what setup is required?)
- Success criteria (what does a successful report look like?)
- Troubleshooting (what if the report is empty? takes too long? shows wrong data?)
- Realistic example scenario

Request clarifications before proceeding.

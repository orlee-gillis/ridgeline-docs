# User Guide Validator

**Validates and drafts user-facing task documentation** — step-by-step guides, how-tos, and workflow documentation for end users.

## When to use this skill

Invoke `/user-guide-validator` when you have:

- A **PRD or feature spec** describing a user-facing feature or workflow
- **Task scenarios** explaining what users need to accomplish
- **An existing draft** that needs validation for user comprehensibility

Use this Skill **before opening a PR** to ensure user guides are complete and task-focused (not just API documentation reworded).

## What it does

### Stage 1: User-Guide-Specific Input Validation

Checks the provided feature specification against a **user-guide-specific checklist** (assumes Stage 0 already passed):

✓ Complete task workflow — end-to-end steps, decision points, happy path  
✓ Prerequisites specific to the task (beyond general feature setup)  
✓ Success criteria and how to interpret results  
✓ Common failure modes and troubleshooting for each  
✓ Realistic example scenario showing concrete context  
✓ Related tasks and next steps, user skill level clarification  

**Output:** A report of what's present, what's missing, and what needs clarification.

### Stage 2: Template Selection & Draft Generation (if input is complete)

If the PRD passes Stage 1, asks a clarifying question about guide structure, then generates a **draft user guide**.

**Template Selection Question:**
```
What type of user guide is this?

1. High-level overview (parent-report)
   → For feature-level guides, "Getting started", architectural overview
   → Audience: All users, new to feature

2. Specific task or feature (child-report)
   → For task walkthroughs, how-to guides, individual workflows
   → Audience: Users performing specific actions

3. Step-by-step process (workflow-methodology)
   → For detailed procedures, methodologies, complex workflows
   → Audience: Users needing comprehensive step-by-step guidance
```

**Draft includes:**
- **Frontmatter:** Automatically populated with selected template (parent-report, child-report, or workflow-methodology)
- **Overview:** Why this feature matters and what you can do with it
- **Before you start:** Prerequisite knowledge, setup, or permissions needed
- **Main task (step-by-step):** Clear, numbered steps with decision points
- **Example scenario:** A realistic walkthrough with context
- **Success criteria:** How to verify you completed the task
- **Troubleshooting:** Common issues and solutions
- **Next steps:** Related tasks or advanced workflows

---

## How to invoke

From Claude Code, type:

```
/user-guide-validator
```

Then provide:

1. **The input:** Paste your PRD, feature spec, or task description
2. **Your question:** "Validate this for a user guide" or "Draft a user guide for this feature"
3. **Context:** Which feature this is for and who the users are (e.g., "Unauthorized Agent Access for security teams", "Widget sync for application developers")

---

## What you'll get back

### If the PRD is **incomplete:**

A checklist showing:
- ✓ What's present
- ✗ What's missing (required)
- ? What's unclear (clarification needed)

Example output:
```
VALIDATION REPORT: Unauthorized Agent Access — User Guide

✓ Feature purpose: Detect and report unauthorized tool access
✓ Audience: Security teams, platform engineers
✓ Task scenarios: One workflow documented (finding unauthorized access)
✗ Prerequisite knowledge: What's a "tool scope" and how is it declared? (not explained)
✓ Success criteria: User can identify which tools an agent called outside scope
✗ Troubleshooting: Empty — what if findings seem incorrect? What if lookback window is too long?
? Audience clarity: Should this guide also cover developers setting up agents, or just security teams reviewing findings?

BLOCKERS:
- Clarify prerequisite knowledge (what is tool scope? where do declarations live?)
- Add troubleshooting section with 3+ common issues

RECOMMENDATIONS:
- Include a decision tree: "Am I looking for what THIS agent accessed" vs. "I want to know what this agent IS ALLOWED to access"
- Add a section on interpreting severity levels (low/medium/high/critical)
```

### If the PRD is **complete:**

1. **Template selection:** You'll be asked which template type fits the guide
2. **Draft generation:** A user guide with:
   - Frontmatter including selected template (parent-report, child-report, or workflow-methodology)
   - Task-oriented content structured for that template type
   
Ready for:
1. Human review and editing
2. Commit to a feature branch (template tag already populated)
3. User feedback testing

---

## Reference materials

- **User Guide Checklist:** `/ai-workflow/skills/user-guide-validator/references/prd-checklist.md`
- **Draft Template:** `/ai-workflow/skills/user-guide-validator/references/template.md`

---

## Scope & Limitations

**In scope:**
- Validating feature specs for user-guide readiness
- Drafting task-oriented user guides
- Checking completeness against user-focused criteria
- Identifying missing prerequisite knowledge or troubleshooting

**Out of scope:**
- Tool reference documentation (use `/mcp-tool-reference-validator` for that)
- Conceptual overviews or feature narratives (use `/ridgeline-doc-writer` for that)
- Auditing completed guides (use `/ridgeline-doc-auditor` for that)

---

## Notes

- This Skill's Stage 1 is **type-specific only** — it assumes Stage 0 (`/documentation-input-validator`) has already passed. The orchestrator runs Stage 0 once, then Stage 1 only for selected doc types.
- Stage 1 checks only user-guide-specific requirements (task workflows, prerequisites, success criteria, troubleshooting) — it does NOT re-check generic PRD completeness.
- Focuses on **task-oriented documentation for end users**, not technical API reference.
- Differs from `/mcp-tool-reference-validator` by prioritizing user workflows over technical specifications.

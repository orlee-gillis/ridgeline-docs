# User Guide Validator

**Validates and drafts user-facing task documentation** — step-by-step guides, how-tos, and workflow documentation for end users.

## When to use this skill

Invoke `/user-guide-validator` when you have:

- A **PRD or feature spec** describing a user-facing feature or workflow
- **Task scenarios** explaining what users need to accomplish
- **An existing draft** that needs validation for user comprehensibility

Use this Skill **before opening a PR** to ensure user guides are complete and task-focused (not just API documentation reworded).

## What it does

### Stage 1: PRD Input Validation

Checks the provided feature specification against a **user-guide-specific checklist**:

✓ Feature purpose and user goals (what problem does this solve for users?)  
✓ Task scenarios — at least one complete end-to-end workflow  
✓ Prerequisite knowledge or setup (what does the user need to know first?)  
✓ Success criteria (how does the user know they succeeded?)  
✓ Common failure modes or troubleshooting (what could go wrong and how to fix it?)  
✓ Audience clarity (who is this guide for? developers? admins? end users?)

**Output:** A report of what's present, what's missing, and what needs clarification.

### Stage 2: Draft Generation (if input is complete)

If the PRD passes Stage 1, generates a **draft user guide** using a task-oriented template.

Each guide includes:
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

A draft user guide ready for:
1. Human review and editing
2. Commit to a feature branch
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

- This Skill focuses on **task-oriented documentation for end users**, not technical API reference.
- Differs from `/mcp-tool-reference-validator` by prioritizing user workflows over technical specifications.
- Works best when paired with `/documentation-input-validator` (Stage 0) first to ensure baseline completeness.

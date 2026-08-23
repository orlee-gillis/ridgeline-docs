---
title: Documentation Validation System
description: A composable multi-type validation pipeline demonstrating docs-as-code architecture with variable documentation needs
---

# Documentation Validation System

This page describes Ridgeline's documentation validation and drafting system—a composable architecture that validates and generates documentation when **not all documentation types are needed for every feature**.

## The Problem

Cloud security features have diverse documentation needs depending on their phase and audience:

| Phase | Type | Purpose |
|-------|------|---------|
| **Phase 1** | MCP Tool Reference | Developers: "How do I call this API?" |
| **Phase 2** | User Guide | Security teams: "How do I use this feature?" |
| **Phase 3** | LLM Documentation | AI agents: "What can you do with this?" |

But not every feature goes through all phases simultaneously. Some features might need:
- Only API reference (backend service, no UI)
- Only user guides (UI-first, no programmatic API)
- API + LLM docs but no user guide (developer tool)
- All three (full-stack feature)

**The challenge:** How to validate documentation when documentation types are variable, not fixed?

## Solution: Composable Validators + Intelligent Orchestration

The system consists of **5 independent Skills** that compose into a powerful validation pipeline:

### Architecture Overview

```
PRD Input
    ↓
┌─────────────────────────────────────┐
│  Stage 0: Generic Validation        │
│  documentation-input-validator      │
│  Checks: name, purpose, scope,      │
│          audience, workflows,       │
│          constraints (universal)    │
└─────────────────────────────────────┘
    ↓ (if passes)
    ├─→ Stage 1: Type-Specific Validation (selected types only)
    │   ├─ mcp-tool-reference-validator
    │   │   (tool names, parameters, returns, examples, errors)
    │   ├─ user-guide-validator
    │   │   (task workflows, prerequisites, troubleshooting)
    │   └─ llm-docs-validator
    │       (decision logic, completeness, error scenarios)
    │
    └─→ Stage 2: Optional Draft Generation
        ├─ MCP tool reference draft
        ├─ User guide draft
        └─ LLM documentation draft
```

### Key Design Principles

#### 1. No Stage Overlap
- **Stage 0** checks items universal to all features (runs once)
- **Stage 1** checks ONLY type-specific items (no re-checking Stage 0)
- Result: Efficient, no redundant validation

#### 2. Composable, Not Monolithic
Each validator is independent:
- Can run standalone (users get deep feedback on one type)
- Can be used together (orchestrator coordinates multiple types)
- New doc types add new validators (don't modify existing ones)

#### 3. Flexible Type Selection
Two modes for determining which doc types are needed:

**Configuration-Driven** (for established features):
```json
{
  "feature_name": "Unauthorized Agent Access Detection",
  "documentation_types": ["mcp-tools", "user-guide", "llm-docs"]
}
```
Repeatable, automation-friendly, works in CI.

**Interactive Discovery** (for new features):
```
Q1: Does this expose a programmatic interface?
    → Yes = need MCP tools validator

Q2: Do end users interact with this directly?
    → Yes = need user guide validator

Q3: Should AI systems understand this?
    → Yes = need LLM docs validator
```
Low barrier to entry, helps users discover what they need.

**Per-Run Override:**
```
/documentation-orchestrator --types mcp-tools,llm-docs
# Skips user guide validator
```

## Workflow Example: Unauthorized Agent Access

Here's how the system works for a real feature:

### Step 1: Configuration
Create `.claude/documentation-config.json`:
```json
{
  "feature_name": "Unauthorized Agent Access Detection",
  "documentation_types": ["mcp-tools", "user-guide", "llm-docs"]
}
```

### Step 2: Run Orchestrator
```
/documentation-orchestrator
```

The orchestrator reads the config and determines:
- **Yes** to MCP tool reference (has API)
- **Yes** to user guide (security teams use it)
- **Yes** to LLM docs (AI agents should understand it)

### Step 3: Stage 0 Validation
Generic PRD completeness check runs once:
```
✓ Feature name: "Unauthorized Agent Access Detection"
✓ Purpose: Detect tool calls outside declared scope
✓ Scope: What's in/out clearly stated
✓ Audience: Security teams, platform engineers
✓ Workflows: Complete detection workflow documented
✓ Constraints: Read-only, lookback window limits
```

If Stage 0 passes → proceed to Stage 1

### Step 4: Stage 1 Validation
Only the three selected validators run (no wasted effort):

**MCP Tool Validator:**
```
✓ Tool names: get_unauthorized_access, get_remediation_options
✓ Parameters: identity_id (string), severity_threshold (enum), days_back (int)
✓ Return values: Finding objects with all fields documented
✓ Error scenarios: 404 not found, 400 invalid parameter, 429 rate limit
✓ Examples: Real success and error responses
```

**User Guide Validator:**
```
✓ Task workflows: Complete finding review workflow documented
✓ Prerequisites: What users need to know first
✓ Success criteria: How to know the task succeeded
✓ Troubleshooting: Common issues and solutions
✓ Examples: Realistic scenario with context
```

**LLM Docs Validator:**
```
✓ Decision logic: When to use this vs. get_actual_access
✓ Completeness: All params, returns, errors documented
✓ Examples: Success and error cases provided
✓ Self-contained: No external references needed
```

If all Stage 1 validators pass → offer to generate drafts

### Step 5: Stage 2 Drafts
```
✓ mcp-tools: Generate tool reference page
✓ user-guide: Generate step-by-step user guide
✓ llm-docs: Generate LLM-ingestible documentation
```

Each draft is ready for human review and editing.

## The Skills

### `documentation-input-validator` (Stage 0)
Generic PRD completeness for all doc types.

**Checks:**
- Feature identity (name, purpose, source)
- Scope (included, excluded, boundaries)
- Audience and use cases
- At least one complete workflow
- Key actors/entities
- Known constraints/limitations
- Error handling and edge cases

**Output:** Completeness report (ready/incomplete/needs clarification)

### `mcp-tool-reference-validator` (Stage 1+2)
MCP tool specification validation and drafting.

**Stage 1 checks:**
- Tool names (e.g., `list_ai_identities`)
- Parameters (types, constraints, where to get them)
- Return values (structure, types, nullable fields)
- Real, verified examples
- All error scenarios (HTTP codes, responses, recovery)
- Relationships to other tools

**Stage 2 output:** Tool reference page with Purpose → Parameters → Returns → Examples → Notes

### `user-guide-validator` (Stage 1+2)
Task-oriented user documentation validation and drafting.

**Stage 1 checks:**
- Complete task workflows (start to finish)
- Prerequisites and setup
- Success criteria and result interpretation
- Troubleshooting for common failure modes
- Real-world example scenarios
- Related tasks and next steps

**Stage 2 output:** User guide with Before You Start → Steps → Example → Success Criteria → Troubleshooting → Next Steps

### `llm-docs-validator` (Stage 1+2)
LLM-ingestible documentation validation and drafting.

**Stage 1 checks:**
- Self-contained specification (no external references)
- All parameters/outputs fully documented
- Decision logic (when to use this vs. alternatives)
- Error scenarios with recovery steps
- Real examples (success and error cases)

**Stage 2 output:** Compact, highly-structured documentation for AI reasoning

### `documentation-orchestrator` (Coordinator)
Determines which doc types are needed, runs Stage 0 once, then Stage 1 for selected types, optionally generates Stage 2 drafts.

**Modes:**
- **Config-driven:** Reads `.claude/documentation-config.json`
- **Interactive:** Asks 3 questions about the feature
- **Override:** `--types mcp-tools` forces specific types

## Design Thinking

### Why Composable Over Monolithic?

A monolithic validator would:
- ❌ Force all types to run every time
- ❌ Be hard to extend (adding new type requires rewriting core)
- ❌ Prevent users from getting deep feedback on one type

Composable validators:
- ✅ Only run selected types
- ✅ New types add new validators (no modification to existing)
- ✅ Users can run individual validators for focused feedback

### Why Config + Interactive, Not Just One?

**Config-only approach:**
- ✅ Repeatable for established features
- ❌ Friction for new features (need setup first)
- ❌ Doesn't scale well for automation discovery

**Interactive-only approach:**
- ✅ Good for discovery and new features
- ❌ Slow for repeated runs
- ❌ Doesn't work well in CI

**Config + Interactive with fallback:**
- ✅ Repeatable for established features
- ✅ Discovery-friendly for new features
- ✅ Works in CI and interactive contexts
- ✅ Per-run overrides for flexibility

### Why No Stage 0 Duplication?

Stage 0 checks generic items once. Stage 1 checks ONLY type-specific items.

**Why?**
- Efficient (no redundant checking)
- Clear separation of concerns
- Each validator handles only its domain

**Trade-off:**
- Requires careful checklist curation
- But eliminates confusion about which validator checks what

## Extensibility

The architecture scales to new documentation types:

```
Want to add REST API documentation?
→ Create api-reference-validator (Stage 1+2)
→ Add "api-docs" to config schema
→ Add question 4 to interactive flow
→ No changes to Stage 0 or orchestrator
```

## Portfolio Value

This system demonstrates:

1. **Architectural Thinking**
   - Composable design (vs. monolithic)
   - Stage separation (vs. overlap)
   - Configuration-driven (vs. hardcoded)

2. **Solving Real Constraints**
   - "Not all features need all doc types"
   - Supporting both established and new features
   - Balancing flexibility and repeatability

3. **Design Trade-Offs**
   - Simple vs. flexible (chose flexible)
   - Monolithic vs. composable (chose composable)
   - Config vs. discovery (chose both with fallback)

4. **Documentation as Code**
   - Validation rules are code
   - Checklists are processable documents
   - Orchestration is deterministic

## What's Next

Future extensions planned:

- **REST API Reference Validator** (for REST APIs like UAX's API)
- **GraphQL Documentation Validator** (for GraphQL schemas)
- **OpenAPI Integration** (for existing Swagger/OpenAPI specs)
- **Performance Benchmarking** (which validators are fastest)
- **CI/CD Integration** (automated validation in GitHub Actions)

---

## Learn More

**Reference Documentation:**
- [documentation-input-validator](/ai-workflow/skills/documentation-input-validator/SKILL.md) — Stage 0 validation
- [mcp-tool-reference-validator](/ai-workflow/skills/mcp-tool-reference-validator/SKILL.md) — MCP tools
- [user-guide-validator](/ai-workflow/skills/user-guide-validator/SKILL.md) — User guides
- [llm-docs-validator](/ai-workflow/skills/llm-docs-validator/SKILL.md) — LLM documentation
- [documentation-orchestrator](/ai-workflow/skills/documentation-orchestrator/SKILL.md) — Coordination

**Process Documentation:**
- [Design Decision Document](/ai-workflow/decisions/multi-type-validation-architecture.md) — Architecture and trade-offs
- [Problem Brief](/ai-workflow/inputs/documentation-validation-system-brief.md) — Requirements and constraints

**Case Studies:**
- Unauthorized Agent Access Feature (coming soon) — Real example of the system in action

---
title: Documentation Validation System
description: A composable multi-type validation pipeline demonstrating docs-as-code architecture with variable documentation needs
---

This page describes Ridgeline's documentation validation and drafting system—a composable architecture that validates and generates documentation when **not all documentation types are needed for every feature**.

## The Problem

Cloud security features have diverse documentation needs depending on their phase and audience:

| Phase | Type | Purpose |
|-------|------|---------|
| **Phase 1** | API Reference | Developers: "What are the endpoints and how do I call them?" |
| **Phase 1** | MCP Tool Reference | Developers: "What are the tool definitions and parameters?" |
| **Phase 2** | User Guide | Security teams: "How do I use this feature?" |
| **Phase 3** | LLM Documentation | AI agents: "What can you do with this?" |

But not every feature goes through all phases simultaneously. Some features might need:

- Only REST API reference (backend service, no UI)
- Only MCP tool reference (callable functions, no HTTP API)
- REST API + MCP tools (both programmatic interfaces)
- API + user guide (developer tool + end-user UI)
- API + LLM docs but no user guide (developer tool)
- All four (full-stack feature)

**The challenge:** How to validate documentation when documentation types are variable, not fixed?

## Solution: Composable Validators + Intelligent Orchestration

The system consists of **6 independent Skills** that compose into a powerful validation pipeline:

### Architecture Overview

```text
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
    │   ├─ api-reference-validator
    │   │   (endpoints, methods, parameters, responses, error codes, examples)
    │   ├─ mcp-tool-reference-validator
    │   │   (tool names, parameters, returns, examples, errors)
    │   ├─ user-guide-validator
    │   │   (task workflows, prerequisites, troubleshooting)
    │   └─ llm-docs-validator
    │       (decision logic, completeness, error scenarios)
    │
    └─→ Stage 2: Optional Draft Generation
        ├─ API reference draft
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

```text
Q1: Does this expose a REST API?
    → Yes = need API reference validator

Q2: Does this expose MCP tools or other programmatic interfaces?
    → Yes = need MCP tools validator

Q3: Do end users interact with this directly?
    → Yes = need user guide validator

Q4: Should AI systems understand this?
    → Yes = need LLM docs validator
```

Low barrier to entry, helps users discover what they need.

**Per-Run Override:**

```bash
/documentation-orchestrator --types api-docs,llm-docs
# Skips MCP tools and user guide validators
```

## Workflow Example: Unauthorized Agent Access

Here's how the system works for a real feature:

### Step 1: Configuration

Create `.claude/documentation-config.json`:

```json
{
  "feature_name": "Unauthorized Agent Access Detection",
  "documentation_types": ["api-docs", "mcp-tools", "llm-docs"]
}
```

### Step 2: Run Orchestrator

```bash
/documentation-orchestrator
```

The orchestrator reads the config and determines:

- **Yes** to API reference (has REST endpoints)
- **Yes** to MCP tool reference (has tool definitions)
- **No** to user guide (no UI for end users)
- **Yes** to LLM docs (AI agents should understand it)

### Step 3: Stage 0 Validation

Generic PRD completeness check runs once:

```text
✓ Feature name: "Unauthorized Agent Access Detection"
✓ Purpose: Detect tool calls outside declared scope
✓ Scope: What's in/out clearly stated
✓ Audience: Security teams, platform engineers
✓ Workflows: Complete detection workflow documented
✓ Constraints: Read-only, lookback window limits
```

If Stage 0 passes → proceed to Stage 1

### Step 4: Stage 1 Validation

Only the selected validators run (no wasted effort):

**API Reference Validator:**

```text
✓ Endpoints: GET /api/get_unauthorized_access, GET /api/get_remediation_options
✓ HTTP methods: GET documented for each endpoint
✓ Parameters: identity_id (path), severity_threshold (query), days_back (query) fully specified
✓ Response schema: Finding objects with all fields, types, nullable indicators
✓ HTTP status codes: 200, 400, 404, 429, 500 documented with error responses
✓ Examples: Real success and error response examples
```

**MCP Tool Validator:**

```text
✓ Tool names: get_unauthorized_access, get_remediation_options
✓ Parameters: identity_id (string), severity_threshold (enum), days_back (int)
✓ Return values: Finding objects with all fields documented
✓ Error scenarios: 404 not found, 400 invalid parameter, 429 rate limit
✓ Examples: Real success and error responses
```

**LLM Docs Validator:**

```text
✓ Decision logic: When to use this vs. get_actual_access
✓ Completeness: All params, returns, errors documented
✓ Examples: Success and error cases provided
✓ Self-contained: No external references needed
```

If all Stage 1 validators pass → offer to generate drafts

### Step 5: Stage 2 Drafts

```text
✓ api-docs: Generate API reference page (endpoints, parameters, responses, examples)
✓ mcp-tools: Generate tool reference page
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

### `api-reference-validator` (Stage 1+2)

REST API specification validation and drafting.

**Stage 1 checks:**

- Endpoints (paths, HTTP methods)
- Request parameters (query, path, body; types, constraints, defaults, where to get them)
- Response structures (status codes, body schemas, nested objects, nullable fields)
- Real, verified examples (success + error cases)
- All HTTP status codes and error scenarios
- Authentication and authorization requirements
- Rate limits and other constraints

**Stage 2 output:** API reference page with Endpoint → Request → Response → Examples → Constraints → Notes

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
- **Interactive:** Asks 4 questions about the feature (REST API, MCP tools, user guides, AI/LLM docs)
- **Override:** `--types api-docs,llm-docs` forces specific types

## Templates and Publishing

### Two-Flow Architecture

The system separates **authoring** (validators) from **publishing** (CI gates):

**Flow 1: Authoring (Validators)**

1. Run a validator (`/api-reference-validator`, `/mcp-tool-reference-validator`, etc.)
2. Validator generates a draft with **auto-tagged frontmatter** (template field pre-populated)
3. **Human review:** Edit the draft as needed
4. **Commit:** Push the draft to your feature branch (template tag already in frontmatter)

**Flow 2: Publishing (CI Gates)**

1. **Pull request:** Open a PR to merge your feature branch
2. **CI validation:** Gates check the page's template tag and validate accordingly
3. **Merge:** Once CI passes, merge to main (gates in `.github/workflows/` enforce template-specific requirements)

### Doc Type → Template Mapping

Each documentation type maps to one or more templates:

| Doc Type | Template | Generated By | Notes |
|----------|----------|--------------|-------|
| **API Reference** | `api-reference` | `api-reference-validator` | Auto-tagged. Single template. |
| **MCP Tool Reference** | `mcp-tool-reference` | `mcp-tool-reference-validator` | Auto-tagged. Single template. |
| **User Guide** | `parent-report`, `child-report`, or `workflow-methodology` | `user-guide-validator` | **Interactive selection.** Validator asks which template fits your guide (high-level overview, specific task, or step-by-step process). |
| **LLM Documentation** | `llm-docs` | `llm-docs-validator` | Auto-tagged. Single template. |

### Auto-Tagging vs. Interactive Selection

**Auto-tagged validators** add the template field automatically:

- `api-reference-validator` generates: `template: api-reference`
- `mcp-tool-reference-validator` generates: `template: mcp-tool-reference`
- `llm-docs-validator` generates: `template: llm-docs`

**Interactive validators** ask a clarifying question:

- `user-guide-validator` asks: "What type of guide is this?" and generates the selected template (`parent-report`, `child-report`, or `workflow-methodology`)

### Why This Design?

- **Validators are pre-publication tools** — they help you draft and catch gaps before committing
- **Templates are publication metadata** — they tell CI gates which requirements to enforce
- **Two flows separate concerns** — authoring flexibility + gated publication consistency
- **Auto-tagging where possible** — reduces friction for deterministic cases (API docs, tool reference, LLM docs)
- **Interactive where needed** — user guides need human judgment about structure/audience fit

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

The architecture scales to new documentation types. For example, REST API documentation was added as the 4th type:

```text
Added REST API documentation:
✓ Created api-reference-validator (Stage 1+2)
✓ Added "api-docs" to config schema
✓ Added Q1 (REST API) to interactive flow
✓ No changes needed to Stage 0 or orchestrator core logic
```

To add another type (e.g., GraphQL schema validation):

1. Create `graphql-schema-validator` (Stage 1+2)
2. Add `"graphql-docs"` to config schema enum
3. Add question about GraphQL to interactive flow
4. Orchestrator automatically discovers and uses it

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

- **GraphQL Documentation Validator** (for GraphQL schemas)
- **OpenAPI Integration** (for existing Swagger/OpenAPI specs)
- **Performance Benchmarking** (which validators are fastest)
- **CI/CD Integration** (automated validation in GitHub Actions)
- **Auto-remediation** (suggest fixes for common missing documentation)

---

## Learn More

**Reference Documentation (in repository):**

- [documentation-input-validator](https://github.com/orlee-gillis/ridgeline-docs/blob/main/ai-workflow/skills/documentation-input-validator/SKILL.md) — Stage 0 validation
- [api-reference-validator](https://github.com/orlee-gillis/ridgeline-docs/blob/main/ai-workflow/skills/api-reference-validator/SKILL.md) — REST APIs
- [mcp-tool-reference-validator](https://github.com/orlee-gillis/ridgeline-docs/blob/main/ai-workflow/skills/mcp-tool-reference-validator/SKILL.md) — MCP tools
- [user-guide-validator](https://github.com/orlee-gillis/ridgeline-docs/blob/main/ai-workflow/skills/user-guide-validator/SKILL.md) — User guides
- [llm-docs-validator](https://github.com/orlee-gillis/ridgeline-docs/blob/main/ai-workflow/skills/llm-docs-validator/SKILL.md) — LLM documentation
- [documentation-orchestrator](https://github.com/orlee-gillis/ridgeline-docs/blob/main/ai-workflow/skills/documentation-orchestrator/SKILL.md) — Coordination

**Process Documentation (in repository):**

- [Design Decision Document](https://github.com/orlee-gillis/ridgeline-docs/blob/main/ai-workflow/decisions/multi-type-validation-architecture.md) — Architecture and trade-offs
- [Problem Brief](https://github.com/orlee-gillis/ridgeline-docs/blob/main/ai-workflow/inputs/documentation-validation-system-brief.md) — Requirements and constraints

**Case Studies:**

- [Orchestrator Showcase (Unauthorized Agent Access)](https://github.com/orlee-gillis/ridgeline-docs/blob/main/ai-workflow/inputs/orchestrator-showcase-uax.md) — Real example of the system in action

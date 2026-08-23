# Decision: Multi-Type Documentation Validation Architecture

**Date:** August 23, 2026  
**Status:** Implemented  
**Outcome:** 6 composable Skills (5 validators + 1 orchestrator)

---

## Problem Statement

How do you validate and draft documentation when not all doc types are always needed?

**The Challenge:** A feature might need:
- **Phase 1:** REST API reference (HTTP endpoints and parameters)
- **Phase 1:** MCP tool reference (tool definitions and parameters)
- **Phase 2:** User guide (end-user task documentation)
- **Phase 3:** LLM documentation (for AI reasoning)

But another feature might need only REST APIs, or only MCP tools, or REST APIs + user guides, or any other combination. **There won't always be a need for all 4 types simultaneously.**

A naive approach would run all validators every time, wasting effort. A monolithic validator would be hard to extend. The question: how to make documentation types flexible and composable?

---

## Design Options Considered

### Option A: Single Monolithic Validator
Run all checks at once for all doc types.

**Pros:** Simple
**Cons:** 
- Can't skip unnecessary validators
- Hard to extend (adding new doc types requires modifying one large file)
- Forces users to think about all types every time
- Wastes computation on irrelevant checks

**Decision:** Rejected

---

### Option B: User Specifies Types Each Run
`/validator --types mcp-tools,user-guide` forces the user to decide every time.

**Pros:** Flexible
**Cons:**
- Requires decision every run (friction)
- Doesn't work for automation/CI
- Inconsistent across runs of same feature

**Decision:** Viable as override, but not primary workflow

---

### Option C: Configuration-Driven + Interactive Fallback (Chosen)
- If config exists (`.claude/documentation-config.json`): Use it (repeatable, automation-friendly)
- If no config: Ask interactive questions (discovery for new features)
- Per-run overrides available (flexibility)

**Pros:**
- Scales from one-off features (interactive) to established features (config)
- Repeatable for same feature
- Works in CI/automation
- Interactive discovery helps users learn what they need
- Allows evolution (config changes as feature evolves)

**Cons:**
- Slightly more complexity (config schema + question flow)

**Decision:** Adopted

---

## Architecture Decisions

### 1. Stage Separation: No Overlap

**Decision:** Stage 0 (generic) + Stage 1 (type-specific only) + Stage 2 (drafting)

**Why:**
- Stage 0 checks items universal to all features (name, purpose, scope, audience, workflows, constraints)
- Stage 1 checks ONLY type-specific items (no re-checking Stage 0 content)
- Eliminates redundancy
- Allows Stage 1 to run independently if Stage 0 already passed

**Trade-off:** Requires careful checklist curation to avoid overlap
**Benefit:** Efficient; no wasted validation checks

---

### 2. Composition Over Monolith

**Decision:** 6 independent Skills, not 1 mega-validator

Skills:
- `documentation-input-validator` (Stage 0, runs first)
- `api-reference-validator` (Stage 1+2, REST APIs)
- `mcp-tool-reference-validator` (Stage 1+2, MCP tools)
- `user-guide-validator` (Stage 1+2, user guides)
- `llm-docs-validator` (Stage 1+2, LLM docs)
- `documentation-orchestrator` (coordinator)

**Why:**
- Each validator is self-contained and testable
- New doc types add new validators (not modify existing ones)
- Users can run individual validators for deep feedback
- Orchestrator composes them cleanly

**Trade-off:** Requires coordination logic (the orchestrator)
**Benefit:** Scalable; extensible

---

### 3. Configuration Schema

**Decision:** `.claude/documentation-config.json` declares which doc types a feature needs

```json
{
  "feature_name": "Unauthorized Agent Access Detection",
  "documentation_types": ["api-docs", "mcp-tools", "llm-docs"],
  "run_stage_0_first": true,
  "draft_on_stage_1_pass": true
}
```

**Why:**
- Declarative: teams decide once, don't re-decide
- Idempotent: same config → same validators run
- Automation-friendly: CI/CD can read and follow it
- Evolvable: config changes as feature phases progress

**Trade-off:** Requires setup for new features
**Benefit:** Repeatable, automatable

---

### 4. Interactive Questions for New Features

**Decision:** If no config exists, ask 4 questions to discover doc types needed

**Questions:**
1. Does this expose a REST API? → API docs?
2. Does this expose MCP tools or other programmatic interfaces? → MCP tools?
3. Do end users interact with this directly? → User guide?
4. Should AI systems understand this? → LLM docs?

**Why:**
- Low barrier to entry (no config file upfront)
- Helps users discover what they need
- Captures domain knowledge in answers
- Can be saved to config for future runs

**Trade-off:** Slightly slower (interactive prompts)
**Benefit:** Great for discovery; educational

---

### 5. Three Independent Validators (MCP, User Guide, LLM)

**Decision:** Each doc type gets its own Stage 1+2 validator

**Why:**
- Different criteria for each type
- Different templates for each type
- Can be used independently (users don't need all 3)
- Clear separation of concerns

**Checklist Differences:**

| Validator | Stage 1 Checks | Stage 2 Output |
|---|---|---|
| **MCP tools** | Tool names, parameters, returns, examples, error scenarios | Tool reference page (parameters → returns → examples) |
| **User guides** | Task workflows, prerequisites, success criteria, troubleshooting | Step-by-step guide (before you start → steps → example → success) |
| **LLM docs** | Decision logic, completeness, error scenarios, examples | Self-contained spec (all context upfront for LLM reasoning) |

**Trade-off:** Three separate checklists to maintain
**Benefit:** Tailored validation; type-specific templates

---

## Key Design Principles

### Principle 1: Composable, Not Monolithic
Each validator is independent. The orchestrator coordinates them without forcing users to understand the whole system.

### Principle 2: Flexible, Not Rigid
Config for established features; interactive discovery for new ones. Per-run overrides available.

### Principle 3: No Duplication
Stage 0 checks generic items once. Stage 1 validators check ONLY their type-specific items.

### Principle 4: Scalable
New doc types → new Stage 1 validators. No need to modify existing code.

### Principle 5: Declarative Configuration
Documentation types are declared in a config file, not inferred or hardcoded.

---

## Decisions Made in Service of the Challenge

**Challenge:** "There won't always be a need for all 3"

**Response:**
1. **Orchestrator determines types** (config or interactive)
2. **Only selected validators run** (no wasted effort on unnecessary types)
3. **Configuration evolves with the feature** (Phase 1: API only; Phase 2: add user guide; etc.)
4. **Per-run overrides** (flexibility when needed)

This makes documentation types **variable, not fixed**.

---

## What This Enables

1. **Portfolio Demonstration:**
   - Shows multi-stage validation pipeline
   - Demonstrates composable architecture
   - Illustrates design trade-offs and decisions

2. **Real-World Usage:**
   - Different features declare different doc types
   - Configuration scales from simple to complex
   - Interactive discovery helps new teams get started

3. **Future Extension:**
   - New doc types add new validators (no modify existing)
   - New checks add to checklists (not to orchestrator)
   - Config schema stays stable

---

## Alternative Outcomes Not Chosen

### Why Not: Single Config File with All Checks
**Rejected because:** Would create one massive validator; hard to extend; users can't run just one type for deep feedback.

### Why Not: Always Ask Interactive Questions
**Rejected because:** Slow for repeated runs of same feature; doesn't work well in CI; inconsistent.

### Why Not: Force Users to Choose Types Manually
**Rejected because:** Friction; doesn't scale; automation unfriendly.

### Why Not: Auto-Detect Doc Types from PRD Content
**Rejected because:** Inference is fragile; wrong guesses frustrating; explicit is better than implicit.

---

## Lessons Learned

1. **Composition > Monolith:** Smaller, focused validators are easier to maintain and extend than one big one.

2. **Declarative Config:** Making types explicit (in a config file) is clearer than inferring them.

3. **Fallback to Interactive:** For new features, interactive questions are better than forcing config upfront.

4. **No Overlap:** Carefully separating concerns (Stage 0 generic, Stage 1 type-specific) prevents redundant checks and enables efficient validation.

5. **Flexibility Matters:** Supporting config + interactive + per-run overrides covers the range from automation to discovery.

---

## Success Criteria Met

✅ Supports variable documentation needs (not all 3 always needed)  
✅ Composable (each validator independent)  
✅ Scalable (new doc types add new validators)  
✅ Flexible (config + interactive + overrides)  
✅ Idempotent (same inputs → same results)  
✅ No duplication (Stage 0 once, Stage 1 type-specific)  
✅ Portfolios well (demonstrates design thinking and architecture)

---

## Next Steps

1. Create `.claude/documentation-config.json` for UAX feature
2. Test orchestrator with real PRDs (does it select correct doc types?)
3. Generate initial drafts using the orchestrator
4. Document case study (PRD → orchestrator → drafts)

# Input: Multi-Type Documentation Validation System

**Problem Statement:** August 23, 2026

---

## Challenge

Build a documentation validation and drafting system that can handle multiple documentation types **without requiring all types for every feature**.

### The Specific Problem

When documenting a cloud security feature like "Unauthorized Agent Access Detection," you might need:

| Phase | Documentation Type | Purpose |
|-------|------------------|---------|
| Phase 1 | MCP tool reference | Developers understand how to call the detection API |
| Phase 2 | User guide | Security teams understand how to review findings and take action |
| Phase 3 | LLM documentation | AI agents understand the feature's capabilities and constraints |

But not every feature goes through all three phases at once. Some features might:
- Only need an API reference (backend service, no UI)
- Only need a user guide (UI-first, no programmatic interface)
- Need API docs + LLM docs but no user guide (developer tool, AI-aware)
- Need all three (full-stack feature with AI integration)

**The constraint:** "There won't always be a need for all 3."

### Why This Matters for Docs-as-Code

A naive validation system would:
- Run all validators every time (wasted effort)
- Be hard to extend (adding new doc type requires rewriting core logic)
- Force users to declare unused doc types

This doesn't scale well for a portfolio of diverse features with varying documentation needs.

---

## Requirements

### Functional Requirements

1. **Support variable documentation needs**
   - Some features need only 1 doc type; others need 2 or 3
   - System shouldn't force unnecessary validation

2. **Validate before drafting**
   - Stage 0: Generic PRD completeness (applies to all)
   - Stage 1: Type-specific validation (only for selected types)
   - Stage 2: Draft generation (optional)

3. **Determine doc types intelligently**
   - For established features: Read declaration from config file
   - For new features: Ask interactive questions
   - Always allow manual override

4. **No redundant checking**
   - Each validator checks only its concerns
   - Stage 0 checks generic items once
   - Stage 1 checks type-specific items only (no re-checking Stage 0)

### Non-Functional Requirements

1. **Composable**
   - Each validator is independent
   - Orchestrator coordinates without being a monolith
   - New doc types add new validators (don't modify existing ones)

2. **Scalable**
   - Works for single one-off features (interactive discovery)
   - Works for established features (config-driven)
   - Works in CI/automation

3. **Portfolio-worthy**
   - Demonstrates design thinking and trade-offs
   - Shows composable architecture principles
   - Illustrates solving real constraints

---

## Success Criteria

- ✅ Can validate documentation when not all 3 types are needed
- ✅ Configuration-driven and interactive modes both work
- ✅ No overlap between Stage 0 and Stage 1 checklists
- ✅ Each validator is independent and composable
- ✅ New doc types can be added without modifying existing validators
- ✅ Works with real features (e.g., Unauthorized Agent Access)
- ✅ Portfolio demonstrates design process and decisions

---

## Scope Boundaries

### In Scope

- Generic PRD completeness validation (all doc types)
- MCP tool reference validation and drafting
- User guide validation and drafting
- LLM documentation validation and drafting
- Orchestrator that determines doc types and coordinates validation
- Configuration schema for declaring doc types
- Interactive questions for discovery

### Out of Scope (Future Extensions)

- REST API reference validation (separate validator, planned)
- GraphQL API reference validation
- gRPC service documentation
- OpenAPI/Swagger integration
- Performance benchmarking of validators
- CI/CD integration implementation

---

## Key Decisions to Make

1. **How to separate Stage 0 from Stage 1?**
   - Ensure no duplicate checking

2. **How to structure the orchestrator?**
   - Config-first? Interactive-first? Both with fallback?

3. **How many initial validators?**
   - Start with 3 (MCP, user guide, LLM) and add REST API later?

4. **How to make it extensible?**
   - New doc types = new validators (composition)
   - Not new doc types = modifications to existing validator (monolith)

---

## Constraints

- **Design must be composable** — each validator independent
- **No Stage 0 duplication** — stage 0 checks once, stage 1 checks only type-specific
- **Flexible doc type selection** — can't force all 3 types always
- **Portfolio-demonstrable** — design process and decisions should be documented
- **Real-world usage** — must work for actual features like UAX

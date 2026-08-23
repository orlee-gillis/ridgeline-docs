# Documentation Orchestrator

**Orchestrates multi-type documentation validation** — determines which doc types a feature needs, then runs the appropriate validators in the correct order.

## When to use this skill

Invoke `/documentation-orchestrator` when you have:

- A **PRD or feature spec** and want to generate multiple doc types
- **Uncertainty about which doc types are needed** — the orchestrator can help you decide
- **A feature with existing configuration** — the orchestrator reads `.claude/documentation-config.json` and validates accordingly

Use this Skill **after** you have a PRD ready (or use `/documentation-input-validator` first if you're unsure about PRD completeness).

## What it does

### Stage 0: Determine Documentation Types

**Option 1: Configuration-driven (if `.claude/documentation-config.json` exists)**
- Reads declared doc types from config
- Runs Stage 1 for those types only
- Fast, repeatable, works in CI

**Option 2: Interactive (if no config found)**
- Asks clarifying questions to determine which doc types are needed
- Recommends doc types based on answers
- Offers to save config for future runs

### Stage 1: Unified PRD Validation

Runs the validation pipeline in order:

1. **Stage 0 (generic):** `documentation-input-validator` runs once
   - Checks: feature name, purpose, scope, audience, workflows, constraints
   - Applies to ALL features regardless of doc type

2. **Stage 1 (type-specific):** For each selected doc type, runs its validator:
   - **MCP tools:** `mcp-tool-reference-validator` (parameters, returns, examples, errors)
   - **User guides:** `user-guide-validator` (task workflows, prerequisites, troubleshooting)
   - **LLM docs:** `llm-docs-validator` (decision logic, completeness, error scenarios)

### Stage 2: Draft Generation (Optional)

If all Stage 1 validators pass, offers to generate drafts:
- User can choose: generate all drafts, or pick which types
- Drafts are placed in appropriate directories
- Ready for human review and editing

---

## How to invoke

From Claude Code, type:

```
/documentation-orchestrator
```

Then provide:

1. **The input:** Paste your PRD or feature spec
2. **Your question:** "Validate this feature" or "Generate docs for this"
3. **Optional override:** `--types mcp-tools,user-guide` (skips LLM docs)

Or with a configuration file already in place:

```
/documentation-orchestrator --config  # Reads from .claude/documentation-config.json
```

---

## What you'll get back

### Scenario 1: Auto-detection (no config found)

The orchestrator asks interactive questions:

```
Does this feature expose tools, APIs, or other programmatic interfaces?
→ Determines if MCP tool documentation is needed

Do end users (non-developers) interact with this feature directly?
→ Determines if user guides are needed

Might AI systems (Claude, agents, etc.) need to understand this feature?
→ Determines if LLM documentation is needed

Based on your answers, I recommend: mcp-tools, user-guide
Run with these types? [y/n] → Save to config? [y/n]
```

### Scenario 2: Config-driven (if `.claude/documentation-config.json` exists)

```
Found configuration: documentation_types = ["mcp-tools", "user-guide"]
Running validators for: MCP tool reference, User guide
(Skipping LLM docs)
```

### Scenario 3: Validation passes

**If Stage 0 passes:**
```
✓ Stage 0 (generic): PRD is complete
  Feature name, purpose, scope, audience, workflows, constraints: all present

Ready to run type-specific validators.
```

**If all Stage 1 validators pass:**
```
✓ Stage 1 (MCP tools): Tool names, parameters, returns, examples, errors: all present
✓ Stage 1 (User guide): Task workflows, prerequisites, success criteria, troubleshooting: all present
(Skipping LLM docs per your selection)

All validators passed! Ready to generate drafts.
Generate drafts for: mcp-tools, user-guide? [y/n]
```

### Scenario 4: Validation fails

**If Stage 0 fails:**
```
✗ Stage 0 (generic) failed

Missing: Audience clarity (who uses this feature?)
         Constraints (performance limits? technical boundaries?)

Blockers: Cannot proceed to Stage 1 until Stage 0 passes.

Recommended clarifications:
- Add audience description (end users, developers, admins?)
- Document constraints: performance limits, API rate limits, operational boundaries
```

**If Stage 1 fails (MCP tools):**
```
✓ Stage 0 passed
✗ Stage 1 (MCP tools) failed

Missing: Parameter constraints (max length? allowed values?)
         Return value structure (what fields are nullable?)
         Error scenario documentation (what happens on 404?)

Cannot proceed to Stage 2 until Stage 1 passes.

Run `/mcp-tool-reference-validator` separately for detailed feedback on tool specification.
```

### Scenario 5: Drafts generated

```
✓ Stage 0 passed
✓ Stage 1 (MCP tools) passed
✓ Stage 1 (User guide) passed

Drafts generated:
✓ docs/tools/unauthorized-access-detection.md (MCP tool reference)
✓ docs/how-to/review-unauthorized-access.md (User guide)

Next steps:
1. Review drafts (check for accuracy, completeness, tone)
2. Edit as needed (merge with existing docs, adjust examples)
3. Commit to branch: git add docs/ && git commit -m "..."
4. Open PR for review

Preview: /home/user/ridgeline-docs/docs/tools/unauthorized-access-detection.md
```

---

## Configuration File (`.claude/documentation-config.json`)

**Optional, but recommended for established features.** Tells the orchestrator which doc types to validate without asking each time.

```json
{
  "feature_name": "Unauthorized Agent Access Detection",
  "description": "Detects when AI agents call tools outside their declared scope",
  "documentation_types": ["mcp-tools", "user-guide", "llm-docs"],
  "run_stage_0_first": true,
  "draft_on_stage_1_pass": true
}
```

**Fields:**
- `feature_name` (string, optional): Human-readable name for logging
- `documentation_types` (array, required): Which validators to run
  - Options: `"mcp-tools"` | `"user-guide"` | `"llm-docs"`
  - Example: `["mcp-tools"]` runs only MCP validation; `["mcp-tools", "llm-docs"]` skips user guides
- `run_stage_0_first` (boolean, default true): Always run generic validation first
- `draft_on_stage_1_pass` (boolean, default true): Auto-offer drafts if Stage 1 passes

**How to create one:**
1. Run orchestrator interactively (without config)
2. When asked "Save config?", answer yes
3. Config is saved to `.claude/documentation-config.json`

**How to override per-run:**
```bash
/documentation-orchestrator --types mcp-tools  # Ignores config, runs only MCP tools
/documentation-orchestrator --skip-config      # Interactive mode even if config exists
```

---

## Interactive Questions

**Question 1: Does this feature expose an API, tool interface, or other programmatic interface?**
- **If yes:** Add `mcp-tools` validator
- **Context:** If the feature is callable (users call it, services call it, code calls it), it needs reference documentation
- **Examples of yes:** Database API, microservice endpoint, tool definition, SDK function
- **Examples of no:** Internal algorithm, background service, invisible infrastructure

**Question 2: Do end users (non-developers) interact with this feature directly?**
- **If yes:** Add `user-guide` validator
- **Context:** If users perform tasks using this feature, they need step-by-step guidance
- **Examples of yes:** Web dashboard, command-line tool, mobile app, admin console
- **Examples of no:** Backend service, API only, developer-only feature

**Question 3: Might AI systems (Claude, agents, etc.) need to understand this feature?**
- **If yes:** Add `llm-docs` validator
- **Context:** If you want LLMs to autonomously reason about or use this feature, they need self-contained documentation
- **Examples of yes:** Feature that agents should be aware of, capability for AI tools to invoke, domain knowledge for AI reasoning
- **Examples of no:** Internal implementation detail, not relevant to autonomous systems

---

## Reference materials

- **Documentation Input Validator (Stage 0):** `/documentation-input-validator`
- **MCP Tool Reference Validator (Stage 1):** `/mcp-tool-reference-validator`
- **User Guide Validator (Stage 1):** `/user-guide-validator`
- **LLM Docs Validator (Stage 1):** `/llm-docs-validator`
- **Config Schema:** `/ai-workflow/skills/documentation-orchestrator/references/config-schema.json`

---

## Scope & Limitations

**In scope:**
- Determining which doc types a feature needs
- Running Stage 0 once and Stage 1 for selected types
- Generating drafts from validated specs
- Managing configuration for repeated runs
- Interactive guidance for new features

**Out of scope:**
- Writing or editing documentation content (type-specific validators do that)
- Architectural decisions (whether a feature should exist)
- Performance or feasibility assessment
- Publishing or deployment

---

## Notes

- The orchestrator is **not a replacement for individual validators** — if you need deep feedback on one validator, run `/mcp-tool-reference-validator` directly instead
- **Stage 0 always runs first** — the generic PRD completeness check applies to all features
- **Stage 1 is type-specific only** — each validator checks only its domain, no overlap or double-checking
- **Idempotent** — running the orchestrator multiple times with the same config produces the same results
- **Composable** — works with existing CI/CD; config file enables automation

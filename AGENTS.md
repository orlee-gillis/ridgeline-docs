# Agent Behavior Constraints

## Claude Code

Claude Code may:
- Create and edit files in `ai-workflow/skills/`
- Create and edit files in `meta/`
- Run Vale and build tools
- Create feature branches and open PRs

Claude Code must not:
- Edit or delete anything in `ai-workflow/legacy/` (archived content)
- Commit directly to `main`
- Edit `.vale.ini`, `CLAUDE.md`, or `AGENTS.md` without creating a PR

## Enforcement

These constraints are self-enforced — Claude Code reads this file and refuses 
requests that violate them. If a request conflicts with these rules, Claude Code 
states the rule and declines.

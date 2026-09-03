# ridgeline-docs

Customer documentation for **Ridgeline**, a fictional security product - built as a public docs-as-code portfolio artifact.

The pipeline: Markdown source in `docs/`, pull-request review, CI quality gates, automatic deployment to GitHub Pages. The `ai-workflow/` folder preserves the AI-assisted authoring artifacts (inputs, prompts, flagged drafts, finals) so the editorial story is visible in the repo history.

## Repo layout

| Path | Purpose |
|---|---|
| `docs/` | Published pages (Docusaurus source of truth) |
| `ai-workflow/` | AI-assisted authoring artifacts and skill baselines - see its README |
| `styles/Ridgeline/` | Custom Vale rules (the style guide as code) |
| `.github/workflows/` | `docs-ci.yml` (blocking gates), `deploy.yml` (Pages deploy) |
| `.github/scripts/` | Template compliance validators (parent-report, child-report, workflow-methodology) |
| `.claude/` | Project config, skills, and settings for Claude Code |
| `CLAUDE.md` | Project rules and conventions (see below) |

## Project conventions

This is a live portfolio project with editorial rules and quality gates:
- **No direct commits to `main`** — all changes go through pull requests.
- **Template compliance** — pages marked with `template: parent-report` or similar are validated against schema via `.github/scripts/validate-*.py`.
- **Skill freeze** — `ridgeline-doc-writer` and `unused-access-expert` are frozen until Phase F baseline evaluation (Session 21) completes.
- **AI-assisted authoring** — the `ai-workflow/` folder preserves authoring artifacts (inputs, prompts, audits, decisions) so editorial decisions are traceable.

See **`CLAUDE.md`** for the complete set of hard rules, folder roles, and conventions for contributors.

## Local development

Clone the repo and run locally, or use a Codespace (see below).

## Working in a Codespace

**Code -> Codespaces -> Create codespace on main.** The devcontainer installs dependencies and Claude Code automatically. Then:

```bash
npm start     # live preview on port 3000
claude        # Claude Code; authenticate on first run
```

## Quality gates

Every PR to `main` must pass the `docs-ci` build gate, which checks:
- Markdown linting (markdownlint via `.markdownlint-cli2.jsonc`)
- Link validation (no 404s or malformed URLs)
- Template compliance (for pages marked with `template:` in frontmatter, validates required sections and AI-graded content alignment)

The template validators live in `.github/scripts/validate-*.py` and require `CLAUDE_API_KEY` to run.

## Publishing model

Commits are saves; merging to `main` is publishing (it triggers the GitHub Pages deploy). Every docs PR must pass the `docs-ci` build gate before merge.

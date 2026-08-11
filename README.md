# ridgeline-docs

Customer documentation for **Ridgeline**, a fictional security product - built as a public docs-as-code portfolio artifact.

The pipeline: Markdown source in `docs/`, pull-request review, CI quality gates, automatic deployment to GitHub Pages. The `ai-workflow/` folder preserves the AI-assisted authoring artifacts (inputs, prompts, flagged drafts, finals) so the editorial story is visible in the repo history.

## Repo layout

| Path | Purpose |
|---|---|
| `docs/` | Published pages (Docusaurus source of truth) |
| `ai-workflow/` | AI-assisted authoring artifacts - see its README |
| `styles/Ridgeline/` | Custom Vale rules (the style guide as code) |
| `.github/workflows/` | `docs-ci.yml` (blocking gates), `deploy.yml` (Pages deploy) |

## CI Gates

This site enforces five quality gates before merge:
- **Docusaurus build** — validates the site builds without errors
- **Vale linting** — enforces prose style and consistency
- **Lychee link validation** — ensures all internal links are live
- **Markdownlint** — validates Markdown syntax and formatting
- **AI-assisted content audit** — checks for clarity, consistency, and style using Claude

The AI-assisted gate is part of an intentional workflow exploring modern documentation practices.

## Setup (browser-only)

1. **Upload these files** to the repo root via **Add file -> Upload files**. If the uploader drops the hidden `.github` or `.devcontainer` folders, create their files via **Add file -> Create new file** - typing the full path (for example `.github/workflows/deploy.yml`) creates the folders.
2. **Personalize** `docusaurus.config.js`: replace `YOUR-GITHUB-USERNAME` in the 3 marked spots. Also update the one link in `docs/index.md`.
3. **Enable Pages:** Settings -> Pages -> Build and deployment -> Source: **GitHub Actions**.
4. **First deploy:** Actions tab -> **deploy** -> Run workflow. The site goes live at `https://<username>.github.io/ridgeline-docs/`.

## Working in a Codespace

**Code -> Codespaces -> Create codespace on main.** The devcontainer installs dependencies and Claude Code automatically. Then:

```bash
npm start     # live preview on port 3000
claude        # Claude Code; authenticate on first run
```

## Publishing model

Commits are saves; merging to `main` is publishing (it triggers the Pages deploy). Every docs PR must pass the `docs-ci` build gate before merge.

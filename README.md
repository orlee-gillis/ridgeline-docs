# ridgeline-docs

A public portfolio artifact: customer documentation for **Ridgeline**, a fictional cloud security
product, built end to end as a docs-as-code pipeline - legacy audit, AI-assisted drafting, CI
quality gates, and a measured, evidence-based improvement of the AI skills that produce the docs.
Nothing described in the docs is a real product; the pipeline and the evidence around it are real.

This README is a guided tour. Each section below links the real artifact and says what it proves -
read top to bottom for the whole story, or jump to any one piece.

## The pipeline

1. **Legacy audit** - [`ai-workflow/legacy/`](ai-workflow/legacy/) holds the "before" pages:
   fictionalized from real documentation, deliberately unedited. [`ai-workflow/audits/`](ai-workflow/audits/)
   is what got flagged before anything was rewritten. **Proves:** editorial judgment - assessing
   existing content against a standard before touching it.
2. **Improved pages** - [`docs/what-changed.md`](docs/what-changed.md) is the before/after diff
   with its provenance stated plainly. **Proves:** the improvement is demonstrable, not asserted.
3. **AI-assisted drafting** - [`ai-workflow/inputs/`](ai-workflow/inputs/) (the raw feature note),
   [`ai-workflow/prompts/`](ai-workflow/prompts/) (the drafting prompt, versioned), and
   [`ai-workflow/drafts/`](ai-workflow/drafts/) (the AI's first draft, every unverified claim
   flagged `[VERIFY: ...]`) feed into the shipped page,
   [`docs/apply-a-remediation.md`](docs/apply-a-remediation.md). The human edit is its own commit
   in [PR #5](https://github.com/orlee-gillis/ridgeline-docs/pull/5), so the editorial pass is
   visible as a diff, not just described. **Proves:** a disciplined AI-drafting workflow where the
   model flags what it doesn't know instead of inventing it, and the human edit is auditable.
4. **CI quality gates** - three tiers, documented in [`GATES.md`](GATES.md) and
   [`docs/meta/ci-gates.md`](docs/meta/ci-gates.md): deterministic checks (Vale, markdownlint, link
   check, build), three genre-specific AI gates grounded in real pages
   (`validate-parent-report`/`child-report`/`workflow-methodology`), and an advisory AI reviewer
   that never blocks. [`GATES-CHANGELOG.md`](GATES-CHANGELOG.md) is the honest record of a real
   correction: the first version of this gate system was built on an unverified premise and stayed
   broken, silently, for a full session before anyone checked it against real content.
   **Proves:** the judgment call of what should block a merge versus what should only advise, and
   the discipline to catch and document your own mistake rather than bury it.
5. **Skills, measured and improved** - [`ai-workflow/skills/`](ai-workflow/skills/) holds four
   Claude Skills: `ridgeline-doc-writer` and `unused-access-expert` (drafting and fact-checking,
   designed to pair rather than compete), `ridgeline-doc-auditor` (review, never drafting), and
   `stop-slop` (a vendored, MIT-licensed skill for catching AI writing tells). The two baseline
   skills were audited against a seven-dimension rubric
   ([`rubric.md`](ai-workflow/skills/rubric.md)), scored independently, then compared
   ([`session-24-verdicts.md`](ai-workflow/skills/session-24-verdicts.md)) - disagreements written
   up as ADRs ([`session-24-rubric-disagreements.md`](ai-workflow/decisions/session-24-rubric-disagreements.md))
   rather than averaged away. The audit caught a real bug: the drafting skill's routing genres had
   drifted out of sync with the actual CI gates, so its drafts would never have been checked at
   all. **Proves:** measuring AI tooling quality with a repeatable method, not a vibe - and using
   that measurement to find and fix a real defect.

## How I built this

[`ai-workflow/build-log.md`](ai-workflow/build-log.md) logs every time AI generated code or config
in this repo: the prompt, what the model got wrong, and how I verified work I didn't write myself.

## Repo layout

| Path | Purpose |
|---|---|
| `docs/` | Published pages (Docusaurus source of truth) |
| `ai-workflow/` | AI-assisted authoring artifacts - see [its own README](ai-workflow/README.md) |
| `styles/Ridgeline/` | Custom Vale rules (the style guide as code) |
| `.github/workflows/` | `docs-ci.yml` (gates), `deploy.yml` (Pages deploy) |
| `.github/scripts/` | The gate scripts and the advisory reviewer |

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

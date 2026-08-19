# Gates architecture

This repo's CI runs three tiers of check on every pull request. They exist for different reasons and
are held to different standards - conflating them is the most common way a gate goes wrong.

## The three tiers

### 1. Deterministic

Vale (prose linting), markdownlint (structure), lychee (link checking), and the Docusaurus production
build. No model call, no judgment, no ambiguity. These run in `.github/workflows/docs-ci.yml` as the
`vale`, `markdown`, `links`, and `build` jobs.

**Rule:** if a check can be deterministic, it should be. A gate that asks a model to catch a banned
word or a broken link is wasting a model call on something `grep` already does reliably.

### 2. AI-advisory

`review-docs.py`, run as the `review` job in `docs-ci.yml`. Posts a PR comment. Never fails the build
(`continue-on-error: true`). Uses `claude-haiku-4-5` because the cost of being wrong is low - a human
reads the comment and can ignore it.

Advisory gates are for judgment calls that are useful to surface but not worth blocking a merge over:
tone, whether a claim looks unsourced, whether a page still serves its stated purpose.

### 3. AI-blocking

`validate-child-report.py`, `validate-parent-report.py`, `validate-workflow-methodology.py`, and
`audit-report.js` (Session 22). These can fail the PR check. Because a false positive here blocks
someone's merge, blocking gates need:

- A narrow, well-defined scope (a specific page type, not "all documentation")
- A severity split, so only the most confident/highest-stakes findings actually block - see
  `audit-report.js`'s `high` (blocks) vs. `medium`/`low` (report only)
- A stronger model where accuracy matters more than cost - `audit-report.js` uses
  `claude-sonnet-5`, not haiku
- Local test fixtures, run before the gate ever touches a real PR - see `testing-patterns.md`

**Rule:** before adding a new blocking gate, ask whether it could be advisory instead. Blocking is for
things you're confident enough about to interrupt someone's work over.

## Where gates live

| What | Where |
| --- | --- |
| Design (before writing any code) | `GATES-DESIGN.md` |
| Status and inventory | `GATES.md` |
| History - when a gate was added/changed and why | `GATES-CHANGELOG.md` |
| Workflow trigger | `.github/workflows/<gate-name>.yml` (one file per blocking gate; advisory checks can share `docs-ci.yml`) |
| Script | `.github/scripts/*.py` for Python gates, repo root for Node gates (e.g. `audit-report.js`) |
| Local test fixtures | `<gate-name>-test.json` at repo root, referencing fixture pages under `docs/eval-cases/` |

## Cost model

Each gate entry in `GATES-CHANGELOG.md` should note its approximate per-file token cost and latency -
see `GATES-DESIGN.md`'s "Cost & performance" section for the pattern. This matters once there are
several blocking gates running on every relevant PR; without it, nobody notices the CI bill creeping
up until it's a problem.

## Adding a gate: the sequence

1. Design it in `GATES-DESIGN.md` - purpose, scope, severity framework, cost estimate, test cases.
2. Write the fixtures first (`docs/eval-cases/*.md` + `<gate-name>-test.json`), before the script.
   A gate you can't test locally is a gate you're debugging in CI.
3. Implement the script and workflow.
4. Run the local test mode until fixtures pass with the expected severities.
5. Record it in `GATES.md` and add an entry to `GATES-CHANGELOG.md`.
6. Only then does it go live on real PRs.

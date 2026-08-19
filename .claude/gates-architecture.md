# Gates architecture

This repo's CI runs a few tiers of check on every pull request. They exist for different reasons
and are held to different standards - conflating them is the most common way a gate goes wrong,
and is exactly what went wrong in Session 21/22 (see `GATES-CHANGELOG.md`).

## The tiers

### 1. Deterministic

Vale (prose linting), markdownlint (structure), lychee (link checking), and the Docusaurus
production build. No model call, no judgment, no ambiguity. These run in
`.github/workflows/docs-ci.yml` as the `vale`, `markdown`, `links`, and `build` jobs.

**Rule:** if a check can be deterministic, it should be. A gate that asks a model to catch a
banned word or a broken link is wasting a model call on something `grep` already does reliably.

### 2. AI-advisory

`review-docs.py`, run as the `review` job in `docs-ci.yml`. Posts a PR comment. Never fails the
build (`continue-on-error: true`). Uses `claude-haiku-4-5` because the cost of being wrong is low
- a human reads the comment and can ignore it.

Runs on any doc page **except** ones already covered by a genre-specific gate below (see
`prompt-patterns.md` for how that exclusion works) - a page with its own dedicated check
shouldn't also get a second, overlapping advisory pass.

### 3. AI-blocking-capable, genre-specific

`validate-parent-report.py`, `validate-child-report.py`, `validate-workflow-methodology.py`.
Each checks pages tagged with a specific `template:` frontmatter value against that genre's
requirements in `ai-workflow/skills/ridgeline-doc-auditor/references/audit-checklist.md`. Uses
`claude-sonnet-5` - accuracy matters more here than in the advisory tier, since a finding could
eventually gate a merge. All three currently run as `continue-on-error: true` while they're new;
promoting one to a required check is a separate, later decision.

**These three share one implementation** (`.github/scripts/gate_common.py`) parameterized by
genre name - each per-genre script is a two-line wrapper. Don't copy-paste a fourth gate's logic
into a new file; add a `## <genre>` section to `audit-checklist.md`, tag a real page with that
`template:` value, and write a two-line wrapper calling `gate_common.run("<genre>")`.

**Rule:** a genre only gets a check here once a *real page* exists to ground it. Session 21 built
a gate for a genre ("Report page") that didn't correspond to any real page - the checklist
described something that didn't exist, and there was nothing to test it against except more
invented content. Check `ai-workflow/TODO.md` and the live site before adding a new genre here.

## Where gates live

| What | Where |
| --- | --- |
| Genre requirements (what each `template:` value must contain) | `ai-workflow/skills/ridgeline-doc-auditor/references/audit-checklist.md` |
| Status and inventory | `GATES.md` |
| History - when a gate changed and why | `GATES-CHANGELOG.md` |
| Shared gate implementation | `.github/scripts/gate_common.py` |
| Per-genre thin wrapper | `.github/scripts/validate-<genre>.py` |
| Local test fixtures | `<genre>-test.json` at repo root, referencing fixture pages under `eval-cases/` (never under `docs/` - see `testing-patterns.md`) |

## Adding a new genre-specific gate

1. Confirm a **real page** exists using this genre - don't invent one. Check the live site and
   `ai-workflow/TODO.md` for known gaps first.
2. Add a `## <genre>` section to `audit-checklist.md`, grounded in that real page's actual
   structure (read the page, don't guess from a template file - templates and real pages can
   drift apart).
3. Tag the real page(s) with `template: <genre>` in frontmatter.
4. Write `.github/scripts/validate-<genre>.py` as a two-line wrapper around `gate_common.run()`.
5. Write `<genre>-test.json` with at least two cases: the real tagged page (should pass) and one
   small deliberately-broken fixture under `eval-cases/` (should fail). Run
   `python .github/scripts/validate-<genre>.py --test-file <genre>-test.json` until both pass
   with the expected severity.
6. Add the job to `docs-ci.yml` (`continue-on-error: true` to start), record it in `GATES.md`,
   and add an entry to `GATES-CHANGELOG.md`.
7. Only promote to a required check after it's run clean on real PRs for a while.

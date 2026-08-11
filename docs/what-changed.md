# What Changed: AI-Assisted Audit & Rewrite

Two pages from the Ridgeline portfolio were audited with structured Claude Skills, then rewritten based on findings. This case study shows what changed and why.

## How This Workflow Works

![Audit to ship workflow](/workflow-diagram.svg)

**Stage 1: Audit** — Run structured skills to identify problems that human review might miss or catch differently.

1. **Audit** with structured skills (`ridgeline-doc-auditor`, `unused-access-expert`) — surface editorial and factual problems
2. **Compare** findings to writer-only audit — identify which problem classes the skills catch
3. **Rewrite** based on merged findings — implement fixes while maintaining voice
4. **Gate** with CI — catch regressions automatically via `.github/workflows/docs-ci.yml`
5. **Ship** — confident the pages are auditable and future changes won't break what we fixed

---

## The Biggest Changes

**Stage 2: Rewrite** — Show which problems the audit identified and how the rewrite addressed them.

**A safety guarantee that was missing from both pages** (caught by both writer + skills). Access rights the activity logs cannot audit are classified **Undetermined**, and the product treats them as *used* — remediation never removes them. Both pages named the classification and neither explained that. For a security feature, a reader who reads **Undetermined** as "probably unused" draws the opposite conclusion from the truth. It now appears on both pages, as an admonition, in the same words.

**One page stopped depending on another** (writer caught this). The Access tab page linked out for four concepts — category, scope, JIT grants, inheritance. Rather than repointing links to pages now out of scope, I explained each concept in place. The page got longer and became self-sufficient. Deferring an explanation is only free when the target actually exists.

**Section order was confusing readers** (writer + skills both flagged). Both pages presented mechanism details before answering "what can I actually do?" The rewrite surfaces the "why" and "what" before the "how," so readers can decide whether the page is for them before diving into process.

**Terminology that changed a claim** (skills caught this). One page said rows sort by "unused access rights" when they sort by unused *grants*. A grant is a container holding many rights, so the two produce different orderings. This is exactly the distinction the glossary exists to hold. The skills audit found this terminology slip; the writer-only audit did not.

**Reference links that pointed nowhere** (skills-only flag). Five cross-page anchors resolved to headings that did not exist. All five are gone, replaced with live links or inline definitions. The skills audit caught these via automated link validation; the writer-only audit found only three of the five.

## What the Two Passes Caught Differently

**Stage 1: Compare** — Show which problem classes the writer and skills each caught, and where they diverged.

| Page                 | Writer found | Skills found | Overlap |
| -------------------- | ------------ | ------------ | ------- |
| Unused Access report | 10           | 14           | 7       |
| About the Access tab | 12           | 22           | 1       |

The overlap collapsed on the second page. Its problems were mostly invisible when reading: broken anchors, a column named two different things across two pages, a factual error introduced in translation, inconsistent terminology. No amount of careful reading surfaces those. The first page's problems were editorial — dense paragraphs, confusing headings, missing structure — and there the two passes largely agreed.

---

## CI Quality Gates

**Stage 4: Gate** — Automate detection of countable problems so mechanical errors don't make it to production.

Every pull request runs through five blocking gates in `.github/workflows/docs-ci.yml`. Each gate catches a different class of problem:

**Docusaurus build** (npm script)
- Command: `npm run build`
- Parses all Markdown files in `docs/`
- Validates frontmatter (required fields: `title`, slug consistency)
- Builds static HTML and catches broken internal links via route validation
- Fails if any link references a page that doesn't exist or a heading anchor with no match
- Output: build logs in Actions; blocks merge if build fails

**Vale prose linting** (GitHub Action)
- Runs custom Vale rules in [`styles/Ridgeline/`](https://github.com/orlee-gillis/ridgeline-docs/blob/main/styles/Ridgeline/) (currently: `AccessGrant.yml` for terminology substitutions)
- Scans for banned terms (e.g., "entitlements" → "access grant"; "workspace platform" → "cloud platform")
- Reports violations as inline GitHub PR comments with line numbers
- Fails if any error-level violations are found; warnings are reported but don't block
- Output: PR check status + inline comments; blocks merge if errors exist

**Link validation** (GitHub Action)
- Tool: Lychee link checker
- Offline validation: checks links in `docs/` and `README.md` against local filesystem (`static/` directory)
- Does not validate external URLs (runs offline)
- Catches broken relative links, malformed paths, case-sensitivity issues
- Output: detailed report in Actions; blocks merge if broken links found
- Complements Docusaurus (which catches route/anchor issues); catches filesystem-level problems

**Markdown structure** (GitHub Action)
- Tool: markdownlint
- Validates markdown syntax and structure:
  - No skipped heading levels (h2 → h4 without h3 fails)
  - No malformed tables, lists, code blocks
  - Consistent bullet point style and indentation
  - Proper use of blank lines between block elements
- Output: error report with file and line number; blocks merge on violations
- Enforces readability at the syntax level

**AI-assisted content audit** (Python script + Claude API)
- Script: `.github/scripts/review-docs.py`
- Runs on PRs with changes to `docs/` directory
- Uses Claude to review doc diffs: checks for unverified claims, missing context, inconsistencies with existing pages
- Produces a review comment on the PR with findings
- Does **not** block merge (`continue-on-error: true`) — advisory only
- Requires `ANTHROPIC_API_KEY` secret in GitHub Actions

The countable problems—links, terminology, syntax—are caught automatically. Editorial problems surface as review comments for human judgment.

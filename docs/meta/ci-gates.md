# CI gates

How this repo checks documentation quality automatically, and why the checks are split the way
they are.

## Three tiers

Every pull request that touches `docs/` runs through three kinds of check, each held to a
different standard.

**Deterministic.** Vale (prose linting), markdownlint (structure), lychee (link checking), and
the Docusaurus production build. No model call, no judgment - if a check can be deterministic, it
is. Running a model to catch a banned word or a broken link would waste a call on something
`grep` already does reliably.

**AI-advisory.** One script, `review-docs.py`, posts a single comment covering claims that look
unsourced, terms used inconsistently, or a page that's drifted from its stated purpose. It never
fails the build - a human reads the comment and can disagree with it. Runs on `claude-haiku-4-5`,
since the cost of an occasional wrong call is low.

**AI-blocking-capable, genre-specific.** Three gates, one per documentation genre, each checking
a page against a written checklist for that genre. These are the ones covered below.

## The genre gates

A page opts into a genre-specific check by declaring it in frontmatter:

```yaml
---
title: Unused Access report
template: parent-report
---
```

Three genres exist, each with its own gate and its own real example page:

| Genre | Gate | Real page |
| --- | --- | --- |
| `parent-report` | `validate-parent-report.py` | `unused-access-report.md` |
| `child-report` | `validate-child-report.py` | `about-the-access-tab.md` |
| `workflow-methodology` | `validate-workflow-methodology.py` | `apply-a-remediation.md` |

Each gate reads the matching `##` section from
[`audit-checklist.md`](https://github.com/orlee-gillis/ridgeline-docs/blob/main/ai-workflow/skills/ridgeline-doc-auditor/references/audit-checklist.md) -
the required elements for that genre and why each one matters - and hands it to Claude alongside
the full page. The checklist is read from disk on every run, not copied into the script, so
editing one `##` section changes every future run of that gate without touching code.

The model returns a fixed shape: a one-line summary of the page's purpose, a list of findings
(each with a severity, which checklist row it violates, and a suggested fix), and the highest
severity found. Severity is `blocker`, `should-fix`, or `none` - the same vocabulary the checklist
itself uses. A `blocker` is reserved for a missing safety or guarantee statement (a step a reader
could act on without knowing what it can't undo); everything else that's missing is `should-fix`.

### Why structured output instead of asking for JSON in the prompt

An earlier version of these scripts asked the model to "respond with JSON" as plain prompt text,
then parsed the reply with a bare `try / except: return False, ["validation failed"]`. That
pattern makes every failure - a malformed key, a wrapped code fence, an actual API error - look
identical: one generic message with no way to tell them apart.

The current version passes a JSON Schema as `output_config.format` on the API request. The
response is guaranteed to match the schema before the script ever sees it, so there's nothing to
catch and no ambiguity between "the model found nothing wrong" and "the response didn't parse."

### One shared implementation, three thin wrappers

`gate_common.py` holds everything genre-agnostic: reading frontmatter, pulling the right checklist
section, building the prompt, calling the API, running the checks, and the local test runner.
Each per-genre script is two lines:

```python
from gate_common import run

if __name__ == "__main__":
    sys.exit(run("parent-report"))
```

Adding a fourth genre means adding a checklist section, tagging a real page, and writing one file
like the one above - not a fourth copy of the whole implementation.

## Testing before a gate ever sees a real PR

Each gate has a paired fixtures file (`parent-report-test.json` and so on) with two kinds of
case: the real tagged page, and a small synthetic page built to fail in one specific way. Fixtures
live in a top-level `eval-cases/` folder, not under `docs/` - a fixture placed under `docs/` would
get published as if it were real content, and since the gates scan every file under `docs/` by
frontmatter tag rather than by diff, a tagged fixture left there would be treated as real on every
future run, not just the one that added it.

```bash
python .github/scripts/validate-parent-report.py --test-file parent-report-test.json
```

`verify.sh` at the repo root runs all three gates' test modes plus the build, markdownlint, and
Vale in one pass - the single command to run before opening a PR that touches a gate or a tagged
page.

## What the first real run found

These three gates existed in the repo before they were wired up to any real page - no page had
ever carried the `template:` tag they looked for, so they'd never actually run. Fixing that
surfaced two real problems on the very first pass, not synthetic ones:

- `unused-access-report.md` stated its data-freshness interval two different ways in two
  different places - "recalculates once a day" in the actual "Data freshness" section, and a
  stray, unheaded sentence near the bottom claiming a 15-minute cycle. The gate flagged the
  contradiction; the stray sentence was deleted.
- `apply-a-remediation.md` has an open `[VERIFY: which role can select Apply]` placeholder in its
  prerequisites table, tracked separately in a decision record. The gate correctly reported this
  as `should-fix`, not a false pass and not a hard block - the page is honestly flagging an
  unresolved question, which is exactly what this project's own convention asks authors to do.

Neither of those would have surfaced without a gate reading the whole page against a written
standard - the deterministic checks (spelling, links, structure) have no way to catch a
self-contradiction or an unresolved dependency.

## Where to look next

- `GATES.md` - current status of every gate.
- `GATES-CHANGELOG.md` - when each gate changed and why, including the design that was scrapped
  before this one (a genre that turned out not to match any real page).
- `.claude/gates-architecture.md` - the full add-a-gate sequence.
- `.claude/prompt-patterns.md` - the two prompt shapes (advisory vs. structured genre audit) and
  when to use each.

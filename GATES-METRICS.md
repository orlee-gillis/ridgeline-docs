# Gate Validation Metrics

Session 23, Part A: measure whether the three real genre gates (`validate-parent-report`,
`validate-child-report`, `validate-workflow-methodology`) actually work, rather than assuming it
from Session 22's design work alone.

**Date**: 2026-08-20
**Method**: each gate's `--test-file` mode against its own fixture pair - the real tagged page
(expects a clean or near-clean result) and a synthetic fixture deliberately missing required
elements (expects a `should-fix` or `blocker` result). Run via `./verify.sh`.

## Results

| Gate | Real page | Result | Broken fixture | Result | Match? |
| --- | --- | --- | --- | --- | --- |
| `validate-parent-report` | `unused-access-report.md` | `none` (expected `none`) | `broken-parent-report.md` | `should-fix` (expected `should-fix`) | Yes, 2/2 |
| `validate-child-report` | `about-the-access-tab.md` | `none` (expected `none`) | `broken-child-report.md` | `blocker` (expected `blocker`) | Yes, 2/2 |
| `validate-workflow-methodology` | `apply-a-remediation.md` | `none` (expected `none` or `should-fix`) | `broken-workflow-methodology.md` | `blocker` (expected `blocker`) | Yes, 2/2 |

All three gates: 2/2 test cases passed. 6/6 total.

## Precision and recall

- **Precision** (of the cases flagged as a problem, how many were real problems): 3/3 = 100%.
  Every fixture the gates flagged (`should-fix` or `blocker`) was the deliberately-broken one, not
  the real page.
- **Recall** (of the real problems in the test set, how many got caught): 3/3 = 100%. No broken
  fixture was missed - none scored `none`.

**Sample-size caveat.** This is the whole eval set (2 cases per gate, 6 total), not a sampled
subset of a larger corpus - Session 23's original plan called for running against "8-10 past PRs,"
but this repo doesn't yet have that volume of history through the three real gates to draw a
larger sample from. 100% on n=2 per gate is a clean result, not a statistically powerful one.
Growing the eval set (more real drafts, more deliberately-broken variants) is future work, not a
blocker - see the follow-up note below.

## Real-world corroboration (beyond the synthetic test set)

The gates already produced two real findings in production, before this metrics run existed,
recorded in `docs/meta/ci-gates.md` and `GATES-CHANGELOG.md`'s Session 22 entry:

- `validate-parent-report` caught a real self-contradiction in `unused-access-report.md`: the page
  stated its data-freshness interval two different ways in two different places ("recalculates
  once a day" in the actual Data Freshness section, versus a stray, unheaded sentence near the
  bottom claiming a 15-minute cycle). Flagged and the stray sentence was deleted.
- `validate-workflow-methodology` correctly reported `apply-a-remediation.md`'s open
  `[VERIFY: which role can select Apply]` placeholder as `should-fix`, not a false pass and not a
  hard block - matching this project's own convention that an honestly-flagged open question isn't
  a bug.

Neither of those would have surfaced from the deterministic checks (Vale, markdownlint, link
check) - they require a gate that reads the whole page against a written standard.

## Decision (against Session 23's >80% precision / >70% recall bar)

Both metrics clear the bar on the available evidence. Given the small sample size, this is a
provisional pass, not a final verdict - re-run this file's numbers once more real pages carry a
`template:` tag and more history exists to test against.

## Follow-up

- Expand the eval set as new pages get tagged with `template:` values, rather than leaving it
  frozen at one real page + one synthetic fixture per gate.
- Once `apply-a-remediation.md`'s `[VERIFY]` items are resolved (Session 24), narrow its expected
  severity in `workflow-methodology-test.json` from `["none", "should-fix"]` back to a single
  value - the tolerance was only needed while the placeholder was genuinely ambiguous.

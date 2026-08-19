# Testing gates locally

A gate should be provably correct against known fixtures before it ever runs on a real PR. This
is what `<genre>-test.json` + each script's `--test-file` mode exist for - and the reason the
three genre gates went untested (and, it turned out, broken) for so long: they had no fixtures
and no way to run locally at all before Session 22.

## The pattern

1. Fixture pages live under a top-level `eval-cases/` folder, **not** under `docs/`. This isn't
   just organization - two real failures follow from putting them under `docs/`:
   - They get published to the live site as if they were real content.
   - Worse: `gate_common.py`'s CI mode globs **every** file under `docs/**/*.md` and checks its
     `template:` tag - it isn't diff-scoped. A deliberately-broken fixture left under `docs/`
     with a `template:` tag would be treated as a real page on *every future run*, not just the
     PR that adds it.
   Each fixture is small and clearly fake (see the header comment in each one), so a test failure
   is never confused with a real documentation bug.
2. `<genre>-test.json` lists each case's `filepath` and its expected `expectedSeverity`
   (`"none"`, `"should-fix"`, or `"blocker"`, matching `audit-checklist.md`'s own vocabulary).
   Include the **real tagged page** as one case (should be `"none"` once the checklist section
   correctly describes it) alongside at least one synthetic broken fixture - testing only against
   invented content risks the same drift Session 21's design suffered from.
3. Run:

   ```bash
   python .github/scripts/validate-parent-report.py --test-file parent-report-test.json
   ```

   (same shape for the other two genres). Each script audits every case exactly as it would a
   real PR file, compares actual vs. expected severity, and prints PASS/FAIL. Non-zero exit if
   any case doesn't match.

Requires `ANTHROPIC_API_KEY` in the environment - the same variable the live workflow reads from
the `ANTHROPIC_API_KEY` repo secret (not `CLAUDE_API_KEY` - see `GATES-CHANGELOG.md`, Session 22,
for why that distinction mattered). Set it in your shell before running; never paste it anywhere
it could be logged or committed.

`verify.sh` at the repo root runs the build, markdownlint, Vale, and all three gates' test modes
in one pass - use that instead of running each check separately.

## Choosing fixtures

Cover at least: the real page (clean pass), and one synthetic fixture missing something the
checklist marks as a `blocker` (a missing safety/guarantee statement) if the genre has one. A
fixture that's merely missing an optional element won't exercise the blocking path at all.

## Before promoting a gate to a required check

Don't skip local testing to save time. A blocking gate that's wrong in CI blocks someone's actual
work, and by then the fix costs a debugging session instead of a fixture edit. Get the fixtures
passing first - and confirm the *real* tagged page passes too, not just the synthetic ones. A
gate that only ever ran against invented fixtures is exactly how Session 21's gate ended up
checking a genre with no real page behind it.

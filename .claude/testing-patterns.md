# Testing gates locally

A gate should be provably correct against known fixtures before it ever runs on a real PR. This is
what `<gate-name>-test.json` + a `--test-file` mode exist for.

## The pattern (`audit-report.js`)

1. Fixture pages live under `docs/eval-cases/`, one file per scenario. Each is a small, clearly-fake
   page (see the header comment in each fixture) - never real product content, so a test failure is
   never confused with a real documentation bug.
2. `gates-test.json` lists each fixture's path and its **expected** outcome - `expectedSeverity` for
   `audit-report.js`. This is the file the gate's test mode reads.
3. Run:

   ```bash
   node audit-report.js --test-file gates-test.json
   ```

4. The script audits each fixture exactly as it would a real PR file, compares the actual severity to
   the expected one, and prints PASS/FAIL per case. Exit code is non-zero if any case doesn't match -
   safe to wire into a pre-commit hook or a CI step that runs before the real gate does.

Requires `ANTHROPIC_API_KEY` in the environment - the same variable the live workflow reads from the
`ANTHROPIC_API_KEY` repo secret. Set it in your shell before running the command; never paste it
anywhere it could be logged or committed.

## Choosing fixtures

Cover at least: one clean pass, one that should fail at your gate's highest severity, one that should
fail at a lower severity. `audit-report.js`'s 4 fixtures follow this shape - see `gates-test.json` for
why each one is expected to score the way it does. Two passing fixtures with different topics/shapes
(not just one) catches a gate that's accidentally keying off wording or layout instead of the actual
criteria.

## Known gap

The Python validators (`validate-child-report.py`, `validate-parent-report.py`,
`validate-workflow-methodology.py`) don't have an equivalent local test mode or fixture file yet -
they run directly against `docs/**/*.md` and print pass/fail per matching file, with no baseline to
compare against. This is a real gap, not an oversight to route around: if you're touching one of
those scripts, consider adding a `<name>-test.json` + test mode following this same pattern rather
than tightening the prompt without a way to verify the change.

## Before enabling a gate on real PRs

Don't skip local testing to save time. A blocking gate that's wrong in CI blocks someone's actual
work, and by then the fix costs a debugging session instead of a fixture edit. Get the fixtures
passing first.

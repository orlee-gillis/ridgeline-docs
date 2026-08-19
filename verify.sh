#!/usr/bin/env bash
set -uo pipefail
cd "$(dirname "$0")"

# Runs every local check in one pass: build, markdownlint, Vale, and the three genre gate
# tests (parent-report, child-report, workflow-methodology). Run this before pushing,
# instead of running each check separately.
#
# Requires ANTHROPIC_API_KEY in the environment for the gate test steps.

FAILED=0

echo "=== 1/6 Docusaurus build ==="
if npm run build > /tmp/verify-build.log 2>&1; then
  echo "PASS"
else
  echo "FAIL - see /tmp/verify-build.log"
  tail -30 /tmp/verify-build.log
  FAILED=1
fi
echo

echo "=== 2/6 markdownlint ==="
if npx --yes markdownlint-cli2 "eval-cases/**/*.md" "docs/**/*.md" > /tmp/verify-markdownlint.log 2>&1; then
  echo "PASS"
else
  echo "FAIL - see /tmp/verify-markdownlint.log"
  tail -30 /tmp/verify-markdownlint.log
  FAILED=1
fi
echo

echo "=== 3/6 Vale ==="
if command -v vale > /dev/null; then
  if vale eval-cases/ docs/ > /tmp/verify-vale.log 2>&1; then
    echo "PASS"
  else
    echo "FAIL - see /tmp/verify-vale.log"
    tail -30 /tmp/verify-vale.log
    FAILED=1
  fi
else
  echo "SKIPPED - vale not installed (brew install vale)"
fi
echo

run_gate_test () {
  local label="$1" script="$2" fixtures="$3"
  echo "=== $label ==="
  if [ -z "${ANTHROPIC_API_KEY:-}" ]; then
    echo "SKIPPED - ANTHROPIC_API_KEY not set in this shell"
  else
    if python3 "$script" --test-file "$fixtures"; then
      echo "PASS"
    else
      echo "FAIL"
      FAILED=1
    fi
  fi
  echo
}

run_gate_test "4/6 validate-parent-report gate test" \
  .github/scripts/validate-parent-report.py parent-report-test.json

run_gate_test "5/6 validate-child-report gate test" \
  .github/scripts/validate-child-report.py child-report-test.json

run_gate_test "6/6 validate-workflow-methodology gate test" \
  .github/scripts/validate-workflow-methodology.py workflow-methodology-test.json

if [ "$FAILED" -eq 0 ]; then
  echo "All checks passed."
else
  echo "One or more checks failed. See logs above."
fi
exit $FAILED

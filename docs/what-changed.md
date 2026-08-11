# What Changed: AI-Assisted Audit & Rewrite

Two pages from the Ridgeline portfolio were audited with structured Claude Skills, then rewritten based on findings. This case study shows what changed and why.

## How This Workflow Works

**Stage 1: Audit** — Run structured skills to identify problems that human review might miss or catch differently.

1. **Audit** with structured skills (`ridgeline-doc-auditor`, `unused-access-expert`) — surface editorial and factual problems
2. **Compare** findings to writer-only audit — identify which problem classes the skills catch
3. **Rewrite** based on merged findings — implement fixes while maintaining voice
4. **Gate** with CI — catch regressions automatically via `.github/workflows/docs-ci.yml`
5. **Ship** — confident the pages are auditable and future changes won't break what we fixed

---

## The Biggest Changes

**Stage 2: Rewrite** — Show which problems the audit identified and how the rewrite addressed them.

**A safety guarantee that was missing from both pages** (caught by both writer + skills). Access rights the activity logs cannot audit are classified **Undetermined**, and the product treats them as *used* — remediation never removes them. Both pages named the classification and neither explained that. For a security feature, a reader who reads **Undetermined** as "probably unused"

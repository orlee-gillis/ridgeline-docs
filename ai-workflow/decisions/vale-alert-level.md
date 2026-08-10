# Vale Alert Level: Errors Only

**Decision:** Set `MinAlertLevel = error` in `.vale.ini` so the CI gate blocks only on rule violations, not soft suggestions.

**Why:** The style guide distinguishes between three levels of feedback:
- **Errors** are violations — inconsistencies, clarity issues, or accessibility problems that contradict the guide
- **Warnings and suggestions** are preferences — useful for authoring, but have legitimate exceptions

Blocking PRs on preferences exhausts reviewers and contributors. Industry norm is errors-only gates; local runs can report all levels for author feedback.

**Implication:** Contributors see Vale suggestions locally (helpful while writing), but CI only fails on actual violations. The style guide is now living infrastructure, not a checklist of preferences.

**Change:** One line in `.vale.ini`.
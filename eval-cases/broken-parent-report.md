---
title: About the Idle Session report
description: Gate test fixture, not real product documentation.
template: parent-report
---

<!-- Gate test fixture for validate-parent-report.py. Deliberately broken: no ordering
explanation, no "what to do with a finding," no data freshness. None of parent-report's
checklist rows are marked blocker, so expected result: should-fix (missing required
sections), not blocker. -->

The Idle Session report finds user sessions that have been open for more than 30 days without
activity.

## What the report includes

Each row is one idle session, identified by session ID and the user it belongs to.

## Columns

Session ID, user, and idle duration are shown for each row.

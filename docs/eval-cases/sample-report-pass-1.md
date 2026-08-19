---
title: About the Idle Credential report
description: What the Idle Credential report includes, how it is ordered, and what to do with a finding.
sidebar_position: 900
---

<!-- Gate test fixture for audit-report-pages (Session 22). Not real product
documentation - "Idle Credential" is a fictional report used only to exercise
the gate's pass path. Expected result: pass, no findings. -->

The Idle Credential report finds service credentials that have not authenticated in over 90 days,
and recommends rotating or revoking them. Use it to decide which credentials to act on first.

Open the report from **Access Center** > **Exposures** > **Idle Credentials**.

Idle Credential requires no additional platform permissions. It reuses the permissions granted when
each integration was connected, and reads authentication logs already available under them.

## What the report includes

Each row is one service credential that has not authenticated in the last 90 days. Credentials
include API keys, service account tokens, and OAuth client secrets. A team never appears as a row of
its own - teams show up only as the way a credential is owned.

The report covers **authentication idleness**. It does not cover credential strength or rotation
policy compliance, which are findings from a different part of the product, even though both appear
on the credential card.

## How the report is ordered

Rows sort by **Idle days**, highest first, then by credential scope (broadest first). The intent is
that the first screen holds the credentials that have been silent longest and could do the most
damage if compromised.

An empty **Idle days** value means the credential has never successfully authenticated. It is not a
defect - it usually means the credential was issued but never wired into its consumer.

## Columns

| Column | What it shows |
| --- | --- |
| Credential name | The label assigned when the credential was created |
| Idle days | Days since the credential's last successful authentication |
| Scope | The permissions the credential holds |
| Owner | The integration or service account the credential belongs to |

Idle days is relative to the report's last refresh, not to the moment you view the page - see Data
freshness below.

## Filters and views

Filter by scope (narrow / broad) or by owner. Column configuration and export use the same generic
controls available on every report in Access Center.

## Working a finding

1. Open the credential's detail card from the row.
2. Confirm the credential is genuinely unused, not just used infrequently (check the 12-month
   authentication history on the card, not just the 90-day window).
3. Rotate or revoke the credential from the card's **Remediate** action.

:::important
Revoking a credential takes effect immediately. Confirm nothing depends on it before revoking - the
report's 90-day window does not guarantee zero recent use, only zero use in that window.
:::

## Data freshness

The report recalculates every 6 hours. A credential that authenticates now will not drop off the
report until the next recalculation.

## Related

- [About the Unused Access report](../unused-access-report.md)

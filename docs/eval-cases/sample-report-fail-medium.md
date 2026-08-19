---
title: About the Lateral Path report
description: What the Lateral Path report includes, how it is ordered, and what to do with a finding.
sidebar_position: 903
---

<!-- Gate test fixture for audit-report-pages (Session 22). Not real product
documentation - structurally complete but uses an undefined term ("blast
radius index") and never links to a prerequisite concept page. Expected
result: fail, medium severity. -->

The Lateral Path report finds identities whose combined permissions let them reach a sensitive
resource through more than one intermediate role. Use it to decide which path to break first.

Open the report from **Access Center** > **Exposures** > **Lateral Path**.

## What the report includes

Each row is one lateral path: a chain of role assumptions from a starting identity to a sensitive
resource. An identity with only direct access to a resource never appears here, since there is no
chain to report.

The report covers paths of two or more hops. Direct grants are covered by the Access Grants report
instead.

## How the report is ordered

Rows sort by blast radius index, highest first.

An empty blast radius index means the path could not be scored. It is not a defect.

## Columns

| Column | What it shows |
| --- | --- |
| Path | The identity, intermediate roles, and destination resource |
| Hops | Number of role assumptions in the path |
| Blast radius index | See How the report is ordered |

## Filters and views

Filter by hop count. Column configuration and export use the same generic controls available on
every report in Access Center.

## Working a finding

1. Open the path detail view from the row.
2. Identify the intermediate role that is easiest to remove without breaking a legitimate workflow.
3. Remove the role assumption permission that creates that hop.

:::important
Removing an intermediate role assumption can break automation that depends on it. Confirm nothing
depends on the hop before removing it.
:::

## Data freshness

The report recalculates every 12 hours.

## Related

- [About the Idle Credential report](./sample-report-pass-1.md)

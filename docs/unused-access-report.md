---
title: About the Unused Access report
description: What the Unused Access report includes, how it is ordered, and what to do with a finding.
sidebar_position: 20
---

Unused Access finds connected integrations that hold access they were granted but never use, and
recommends narrower alternatives that keep the integration working. Use it to decide which
integrations to reduce access on first.

Open the report from **Access Center** > **Exposures** > **Unused Access**.

![The four overview cards at the top of the report: report scope, integration count, service account count, and team count](/img/unused-access-report-cards.png)
Unused Access requires no additional platform permissions. It reuses the permissions granted when
each integration was connected, and reads activity logs already available under them.

## What the report includes

Each row is one integration that holds at least one unused access right. Integrations include
service accounts. A team never appears as a row of its own - teams show up only as the way a grant
reaches an integration.

The report covers **excessive access**. It does not cover integration posture: stale credentials,
unreviewed external integrations, and missing review dates are findings from a different part of the
product, even though both appear on the integration card.

## How the report is ordered

Rows sort by **Reach score**, highest first, then by number of unused grants. The intent is that the
first screen holds the integrations where unused access matters most, rather than the ones with the
largest raw counts.

Unused Access has no score of its own and does not change an integration's total score.

An empty **Reach score** means no scenarios are defined for that environment. It is not a defect.

## Overview

The cards across the top of the report summarize its scope and contents.

![The integration table, sorted by Reach score, with a usage bar per row](/img/unused-access-report-table.png)

| Card | What it shows |
| --- | --- |
| **Report scope** | Which cloud platform the integrations sit in, and how many organizations and workspaces are actively monitored |
| **Integration count** | How many integrations are in the report, and how many are highly privileged |
| **Service account count** | How many non-human integrations are in the report, covering both workspace-assigned and system-assigned service accounts, and how many are highly privileged |
| **Team count** | How many teams appear in the report, and how many are highly privileged |

Integrations carrying broad administrative roles are labeled **Highly privileged**.
`[VERIFY: exact criteria for the Highly privileged label]`

## Integration table

The table lists your integrations in priority order.

`[SCREENSHOT: cropped view of the integration table header row and two data rows]`

| Column | What it shows |
| --- | --- |
| **Integration name** | Name of the integration. Opens the integration card |
| **Integration type** | Type of integration, including **Service account** |
| **Highly privileged** | Whether the integration carries broad administrative access |
| **Reach score** | How much of the environment the integration can affect. Primary sort |
| **Accessible services** | How many services the integration can reach |
| **Accessible resources** | How many individual resources it can reach within those services |
| **Access right usage** | For **Platform** grants only, how many individual rights are **Used**, **Unused**, or **Undetermined** |
| **Critical resources** | How many of the accessible resources are critical - resources whose compromise would have significant consequences, either reachable directly or through another resource |

Only **Platform** grants carry usage data, so **Access right usage** is blank for integrations whose
access comes entirely from **Directory** or **App-level** grants. Those two categories are assessed
on posture and best practice rather than on logged usage.

:::important
**Undetermined** rights are ones the activity logs cannot audit. They are treated as used, and
remediation advice never removes them. **Undetermined** is not a form of **Unused**.
:::

## What you can do

- **Find one integration.** Type its name into the search box above the table.
- **Add or remove columns.** Click **Configure columns** and select the columns you want.
- **Narrow the list.** Click the filter icon on a column header and choose the values to keep. To
  see only service accounts, filter **Integration type** to **Service account**.
- **Export the data.** Click the export icon to download a CSV. Applying filters first exports only
  the filtered rows. `[VERIFY: exported column set]`

## Working a finding

1. Click the integration's name to open its integration card.
2. Open the **Access** tab.
3. Review the grants that reach the integration, and which of their rights go unused.
4. Open the remediation recommendations and review the proposed narrower access.

For what each part of that tab shows and how to read it, see
[About the Access tab](about-the-access-tab.md).

## Data freshness

The report recalculates once a day. A grant added or used on the platform since the last run appears
after the next one.

## Related

- [About the Access tab](about-the-access-tab.md)

## Open items for SME review

- [ ] `[SCREENSHOT: report overview cards]` - cropped
- [ ] `[SCREENSHOT: integration table header and rows]` - cropped
- [ ] `[SCREENSHOT: full report]`
- [ ] `[VERIFY: exact criteria for the Highly privileged label]`
- [ ] `[VERIFY: exported CSV column set]`
- [ ] Confirm whether the 90-day usage window is configurable by the reader

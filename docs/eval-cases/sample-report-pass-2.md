---
title: About the Exposed Storage report
description: What the Exposed Storage report includes, how it is ordered, and what to do with a finding.
sidebar_position: 901
---

<!-- Gate test fixture for audit-report-pages (Session 22). Not real product
documentation - "Exposed Storage" is a fictional report used only to exercise
the gate's pass path with a different shape than sample-report-pass-1. -->

The Exposed Storage report finds cloud storage buckets reachable from outside the account, and
recommends the narrowest policy change that closes the exposure. Use it to decide which bucket to
lock down first.

Open the report from **Access Center** > **Exposures** > **Exposed Storage**.

## What the report includes

Each row is one storage bucket with a resource policy that grants access to a principal outside the
account, or to the public. A bucket with only same-account access never appears here, even if its
policy is broad.

The report covers **policy-level exposure**. It does not cover object-level ACL exceptions on
individual files within an otherwise-private bucket - those surface on the object detail page
instead.

## How the report is ordered

Rows sort by **Exposure score**, highest first. Exposure score weighs three things: whether access is
public or scoped to specific external accounts, whether write access is included, and whether the
bucket contains any tagged-sensitive object.

A bucket with an Exposure score of zero does not appear on this report at all - zero-scored buckets
are not exposed, so there is no empty-score row to explain.

## Columns

| Column | What it shows |
| --- | --- |
| Bucket name | The bucket's resource identifier |
| Exposure score | 0-100, see How the report is ordered |
| Access type | Public, or the external account IDs with access |
| Write access | Whether the exposed grant includes write, not just read |
| Sensitive content | Whether a tagged-sensitive object was found in the bucket |

## Filters and views

Filter by access type (public vs. external-account) or by write access. Column configuration and
export use the same generic controls available on every report in Access Center.

## Working a finding

1. Open the bucket's policy from the row.
2. Identify the statement granting external access, and confirm whether it is still needed.
3. Narrow the statement to the specific principals that need access, or remove it entirely if none do.

:::important
Removing public access from a bucket that a public website depends on will break that website.
Confirm what consumes the bucket before narrowing its policy.
:::

## Data freshness

Bucket policies are scanned every 4 hours. A policy change made outside this window will not appear
until the next scan.

## Related

- [About the Idle Credential report](./sample-report-pass-1.md)

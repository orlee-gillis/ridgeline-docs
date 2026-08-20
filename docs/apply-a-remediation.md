---
title: Apply a remediation recommendation
description: How to carry out a least-privilege recommendation on an integration's access grant from inside Ridgeline, what it changes, and how to reverse it.
sidebar_position: 40
template: workflow-methodology
---

`[UNRELEASED]` This page describes behavior that has not shipped. Its source story is still in review,
two of its sub-tasks are unfinished, and the feature has no final name. Do not publish it until the
release ships and the open items below are closed.

The Unused Access report and the Access tab identify integrations holding access they never use, and
recommend a narrower access grant that keeps the integration working. Until now, carrying out that
recommendation meant editing the role by hand in the platform's own admin console.

You apply a recommendation from an integration's [Access tab](about-the-access-tab.md), using the
**remediation wizard**.

Applying a recommendation is for:

- Platform and workspace administrators working through the Unused Access report
- Security engineers reviewing one integration in depth

## Prerequisites

| Requirement | Detail |
| --- | --- |
| Your role in Ridgeline | Platform administrator, Workspace administrator, or Security engineer |
| The grant's category | **Platform**. Directory and App-level grants have no usage data to work from |
| The grant's assignment | Direct. Grants inherited through a team are not supported in this release |
| A recommendation | Ridgeline has recommended a narrower role for the grant |
| Ridgeline's platform permissions | Read, plus write. See below |

### Write permission

| | |
| --- | --- |
| Read grants and activity logs | Covered by the platform permissions granted when the integration was connected |
| Write a change to the platform | Not covered. Requires additional platform permissions to change role definitions and the grants that attach roles |
| New connection | Requests the write permission during setup |
| Existing connection | Requires re-consent before **Apply** works. Ridgeline shows a banner: "This integration needs an updated connection before Ridgeline can apply changes to it. Reconnect to grant write access." |
| Write permission missing | Reports, usage classification, and recommendations are unaffected. **Apply** is shown disabled, with a tooltip explaining that write permission is missing and how to grant it. |

## What you can do

- Apply a recommendation to one directly assigned **Platform** grant.
- Narrow the grant's scope while applying, or keep its current scope.
- Reverse a completed apply within 24 hours.
- Review every apply and reversal in the integration's history.

## How an apply runs

1. Review the narrower role Ridgeline recommends for the grant.
2. Select **Apply**. Ridgeline shows **the proposed change review** - the change it proposes to
   write, for you to check before confirming.
3. Confirm the change. Ridgeline uses its write permission on the integration only after you confirm.
4. Ridgeline writes the change.
5. For 24 hours after the apply completes, you can reverse it and restore the grant to what it was.

![Review proposed role change — comparison of current and proposed access rights](/img/apply-confirmation.png)

Every apply and every reversal is recorded in the integration's history.

### How the role changes

An integration's access grant holds a role. When you apply a recommendation, Ridgeline edits that role, but doesn't edit the grant.

| The grant holds | What Ridgeline changes |
| --- | --- |
| A custom role | Edits the role definition, removing only the unused access rights |
| A built-in role | Replaces it with the narrowest built-in role that still covers every retained right |

### Which access rights are retained

Because the role determines the integration grant's access rights, editing the role changes those rights. Applying a recommendation retains every **Used** and **Undetermined** access right the integration grant holds.

Ridgeline determines whether an access right is in use by checking for a matching record in the platform's activity logs. The logs record actions that create or change a resource, but not actions that happen inside a resource afterward. If Ridgeline doesn't have a log record to check, the access right is defined as **Undetermined**. Ridgeline treats an Undetermined access right as used, so it never removes the access right.

As a result, if an integration depends on an Undetermined access right, an apply won't remove it — even though nothing in the logs proves that dependency exists.

A recommendation changes at most five access rights at a time. Keeping the list short lets you review every change before confirming it. An apply carries out exactly the changes in its recommendation, so it also changes at most five access rights. The cap is fixed at five for every customer - a usability decision to keep every change reviewable, not a technical ceiling.

### How to narrow the grant's scope

An access grant is limited to one scope level: Organization, Workspace group, Workspace, Project, or Resource. The grant's access rights only work within that level.

By default, an apply keeps the grant's current scope. You can choose a narrower one instead, and Ridgeline will apply that scope.

:::important
Ridgeline never reduces a grant's scope on its own. Narrowing scope during an apply is optional. If you don't narrow it, the grant keeps its original scope.
:::

### How to reverse an apply

You can reverse an apply within 24 hours of its completion. Reversing an apply restores the integration's grant to the role and scope it held beforehand. Once 24 hours has passed, the apply can no longer be reversed using Ridgeline - to restore the grant after that window, edit the role by hand in the platform's own admin console, the same method used before this feature existed.

### When changes appear

Ridgeline recalculates Unused Access data once nightly, at a fixed time in UTC regardless of your
own time zone. An applied change doesn't appear in the Unused Access report's prioritization
(Reach score, unused-grant counts) until the next recalculation - but the Access tab and the
integration's history reflect the change immediately, since Ridgeline writes it directly. Check
either of those, not the report, to confirm an apply worked.

When an apply succeeds, Ridgeline shows a confirmation: a toast notification, and the grant's row is highlighted in the table. A full change summary is out of scope for this release - to see what changed, open the grant on the Access tab or the integration's history.

![Completed apply on the Access tab, with the reversal option visible](/img/apply-completed.png)

### When an apply fails

A failed apply is a change that was only partially written, when one of Ridgeline's two writes succeeds and the other doesn't. This is different from a reversal, which undoes an apply that completed successfully.

Ridgeline performs an apply as two writes:

- Write 1: Changes the role
- Write 2: Updates the grant that attaches the role to the integration

If Write 1 succeeds but Write 2 fails, Ridgeline leaves the changed role definition in place and reports an error, without reversing anything automatically.

You can re-run the apply to complete the role change.

#### Failure vs. reversal

A failed apply can't be reversed, because reversal only applies to a completed apply.

## Limits and known gaps

A recommendation that cannot be applied is still a recommendation. Everything below can be remediated
by hand in the platform's admin console; what is unavailable is Ridgeline writing the change for you.

| Not supported | Why |
| --- | --- |
| Inherited grants | Reducing a grant a team holds affects every integration in that team, and that needs its own review. This release supports directly assigned grants only. |
| **Directory** and **App-level** grants | Neither category carries usage data, so there is no usage-derived change to derive an apply from. Their recommendations remain posture-based and best-practice guidance. |
| JIT grants | A Just-In-Time (JIT) grant is a sub-category of **Directory** and receives best-practice guidance rather than a rewritten role. This is permanent, not a gap to be closed later - a grant meant to be temporary can't be evaluated as though it were standing access. |
| Applying to several grants at once | Each apply covers one grant, by design - so every change stays individually reviewable before you confirm it. Not planned as a future capability. |

## Related documents

- [Unused Access report](unused-access-report.md)
- [Access tab](about-the-access-tab.md)

## Open items for SME review

**Blocking publication**

- [ ] `[UNRELEASED]` - the whole page. Source story is still in review and the feature has no final
      name. Do not publish until the release ships. (Session 24 resolved every open product-behavior
      question below - see `ai-workflow/decisions/UAX-2841.md` - but shipping status is a separate,
      real-world fact this documentation pass can't close.)
- [ ] `[VERIFY: the feature's name]` - the story uses four names for it and marketing has not chosen.
      This page is titled by the task rather than the feature to avoid guessing. The title, the
      sidebar label, the audience sentence, and every inbound link change if a product name lands.
- [ ] Naming constraints to hold: "auto-remediation" is prohibited in the interface and the
      documentation, and "one-click" carries the same implication that no human confirms the change.
      Neither appears on this page. Keep them out of the sidebar label and the description.

**Terminology still to settle**

- [ ] **failed apply** and **reversal** need entries in `glossary.md`, defined against each other,
      since the point of naming them separately was to stop one being read as a variety of the other.
      Neither is a UI label, so neither is bolded in prose.

**Edits required on sibling pages**

- [ ] `about-the-access-tab.md` states "Scope is never narrowed. The replacement applies at the grant's
      original scope" as an unconditional guarantee. Still accurate for the recommendation, and not
      accurate for a change the reader applies. Split the sentence: Ridgeline never reduces scope, and
      the reader can choose to.
- [ ] The Unused Access overview page states that the feature needs no additional platform permissions.
      Still true for reading, and no longer true for the write path. Qualify it rather than deleting it
      - readers look for that answer during evaluation.

**Placement**

- [ ] `sidebar_position: 40` is provisional. This page sits after Access tab and before
      Access tab reference; confirm against the family's existing numbering.

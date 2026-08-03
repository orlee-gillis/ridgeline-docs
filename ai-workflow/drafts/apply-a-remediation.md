---
title: Apply a remediation recommendation
description: How to carry out a least-privilege recommendation on an integration's access grant from inside Ridgeline, what it changes, and how to reverse it.
sidebar_position: 40
---

`[UNRELEASED]` This page describes behavior that has not shipped. Its source story is still in
review, two of its sub-tasks are unfinished, and the feature has no final name. Do not publish it
until the release ships and the open items below are closed.

The Unused Access report and the Access tab identify integrations holding access they never use, and
recommend a narrower access grant that keeps the integration working. Applying a remediation carries
out that recommendation on the platform from inside Ridgeline, so you no longer have to reproduce the
change by hand in the platform's own admin console.

You start an apply from the remediation recommendation for a single grant on an integration's
[Access tab](about-the-access-tab.md). Ridgeline shows what changes, waits for your confirmation,
writes the change to the platform, and then keeps the change reversible for a limited period.
`[VERIFY: the story calls this surface the remediation wizard - confirm the reader-facing name]`

## Who this is for

Whoever is accountable for an integration's access and has the authority to reduce it: a platform or
workspace administrator working through the Unused Access report, or a security engineer reviewing
one integration in depth. Reading a recommendation and applying one are different levels of
authority, so the two are separately gated - see Prerequisites below.

## Prerequisites

- The integration is connected, and at least one of its **Platform** grants has a remediation
  recommendation. Only Platform grants can be applied - see Limits and known gaps.
- The grant is assigned directly to the integration, not inherited through a team.
- Ridgeline holds platform permissions to change role definitions and the grants that attach roles
  to integrations.

Reading grants and activity logs needs no additional platform permissions beyond those granted when
the integration was connected. Writing a change back does. New connections request the additional
platform permissions at connection time; an integration that is already connected has to be
re-consented before an apply is possible.
`[VERIFY: what the reader sees prompting re-consent - the banner copy is undecided]`

Everything else in Unused Access behaves normally without write permission. Reports, usage
classification, and recommendations are unaffected; only **Apply** is unavailable.
`[VERIFY: whether Apply is hidden or shown disabled with an explanatory tooltip - design and
engineering have not agreed]`

## How applying a remediation works

1. Review the narrower role Ridgeline recommends for the grant.
2. Select **Apply**. Ridgeline shows the change it proposes to write, before anything is written.
   `[VERIFY: reader-facing name for this step - the story calls it a dry run]`
3. Confirm the change. Nothing is written to the platform until you confirm.
4. Ridgeline writes the change.
5. For 24 hours after the apply completes, you can reverse it and restore the grant to what it was.

Every apply and every reversal is recorded in the integration's history.
`[VERIFY: exact name of the history surface, and whether it is linkable from the apply confirmation]`

Unused Access data recalculates on a nightly run, so an applied change is reflected in the Unused
Access report after the next run.
`[VERIFY: whether the grant table on the Access tab updates immediately after an apply, or only
after the next nightly run - readers will otherwise read the unchanged report as a failed apply]`

The confirmation Ridgeline shows after a successful apply does not summarize what changed. To see the
applied change, open the grant on the Access tab or the integration's history.
`[VERIFY: the success state is a toast and a highlighted row; a change summary is out of scope for
this release]`

### What Ridgeline changes

| The grant holds | What Ridgeline changes |
| --- | --- |
| A custom role | Edits the role definition, removing only the unused access rights |
| A built-in role | Replaces it with the narrowest built-in role that still covers every retained right |

An apply retains every **Used** access right and every **Undetermined** access right.
**Undetermined** rights are ones the activity logs cannot audit at all. Ridgeline treats them as
used and never removes them, so an apply cannot strip access that an integration silently depends
on.

A single apply is capped at five updates, matching the cap on the recommendation itself.
`[VERIFY: whether the cap is documented as fixed - a higher cap for larger customers is under
discussion, and a cap the page cannot explain reads as arbitrary]`

### Scope

An access grant applies over a scope: **Organization**, **Workspace group**, **Workspace**,
**Project**, or **Resource**. A recommendation never changes it. The narrower role Ridgeline
recommends applies at the grant's original scope, whatever that scope is.

An apply defaults to the same original scope, and you can choose a narrower one. If you do, then the
change written to the platform is narrower than what was recommended.

:::important
Ridgeline never reduces a grant's scope on its own. Narrowing scope during an apply is a choice you
make, and leaving the default in place preserves the grant's original scope.
:::

### Reverse an apply

Within 24 hours of an apply completing, you can reverse it. A reversal restores the grant to the
role and scope it held before the apply.

After 24 hours, the apply can no longer be reversed from Ridgeline.
`[VERIFY: what the reader is expected to do after the window closes, and whether 24 hours is fixed -
the rollback sub-task is unfinished]`

### When an apply fails

An apply is two writes: Ridgeline changes the role, then updates the grant that attaches that role
to the integration. Either write can fail on its own.

If the role change succeeds and the grant update fails, then Ridgeline leaves the changed role
definition in place and reports an error. Nothing is reversed automatically. Re-run the apply to
complete the change.

A failed apply and a reversal are different things. A reversal undoes an apply that succeeded; a
failed apply is a change that was only half written, and the 24-hour reversal window does not cover
it.

:::important
A failed apply leaves the changed role definition on the platform. Ridgeline does not undo it, and
reversing it is not an option, because there is no completed apply to reverse. Re-run the apply.
:::

## What you can do

- Apply a recommendation to one directly assigned **Platform** grant at a time, from that grant's
  recommendation on the [Access tab](about-the-access-tab.md).
- Choose a narrower scope than the grant currently holds, or keep the original scope.
- Reverse a completed apply within 24 hours.
- Review every apply and reversal in the integration's history.

## Limits and known gaps

A recommendation that cannot be applied is still a recommendation. Everything below can be
remediated by hand in the platform's admin console; what is unavailable is Ridgeline writing the
change for you.

| Not supported | Why |
| --- | --- |
| Inherited grants | Reducing a grant a team holds affects every integration in that team, and that needs its own review. This release supports directly assigned grants only. |
| **Directory** and **App-level** grants | Neither category carries usage data, so there is no usage-derived change to derive an apply from. Their recommendations remain posture-based and best-practice guidance. |
| JIT grants | A Just-In-Time (JIT) grant is a sub-category of **Directory** and receives best-practice guidance rather than a rewritten role. `[VERIFY: whether JIT grants are ever intended to be applicable - an engineer has argued twice that they should not be, and nobody has answered]` |
| More than one grant per apply | Each apply covers one grant. `[VERIFY: whether to state that applying across several grants at once is planned, and whether to name a release]` |

`[SCREENSHOT: the confirmation step, showing the current grant and the proposed narrower grant side
by side before anything is written]`

`[SCREENSHOT: a completed apply on the Access tab, with the reversal option visible]`

## Related

- [About the Unused Access report](about-the-unused-access-report.md)
- [About the Access tab](about-the-access-tab.md)
- [Access tab reference](access-tab-reference.md)

## Open items for SME review

**Blocking publication**

- [ ] `[UNRELEASED]` - the whole page. Source story in review; the rollback and re-consent sub-tasks
      are unfinished. Do not publish until the release ships.
- [ ] `[VERIFY: the feature's name]` - the story uses four names for it and marketing has not chosen.
      This page is titled by the task rather than the feature to avoid guessing. The title, the
      sidebar label, and every inbound link change if a product name lands.
- [ ] Naming constraints to hold: "auto-remediation" is prohibited in the interface and the
      documentation, and "one-click" carries the same implication that no human confirms the change.
      Neither appears on this page. Keep them out of the sidebar label and the description.

**Unresolved product decisions**

- [ ] `[VERIFY: whether Apply is hidden or disabled when write permission is missing]` - engineering
      wants disabled with a tooltip, design wants hidden. The page cannot tell the reader what they
      see until this is settled.
- [ ] `[VERIFY: why the cap is five updates, and whether it rises for larger customers]`
- [ ] `[VERIFY: whether JIT grants are ever intended to be applicable]`
- [ ] `[VERIFY: the re-consent banner copy]`

**Gaps found while drafting, not covered by the SME answers**

- [ ] `[VERIFY: when an applied change appears in the Unused Access report and the grant table]` -
      if the report only refreshes on the nightly run, then a reader who applies a change and sees
      the old data will report it as a failed apply. This needs an answer before publication, not
      after the first ticket.
- [ ] `[VERIFY: what the reader does after the 24-hour reversal window closes]` - stated on the page
      as "no longer reversible from Ridgeline," which is accurate but leaves the reader without a
      next step.
- [ ] `[VERIFY: the reader-facing names for the remediation wizard, the pre-write comparison step,
      and the integration history surface]` - all three are engineering or story vocabulary.

**Edits required on sibling pages**

- [ ] `about-the-access-tab.md` states "Scope is never narrowed. The replacement applies at the
      grant's original scope" as an unconditional guarantee. It is still true of recommendations and
      is no longer true of applies. Split the sentence: Ridgeline never reduces scope, and the reader
      can choose to.
- [ ] The Unused Access overview page states that the feature needs no additional platform
      permissions. Still true for reading, and no longer true for the write path. Qualify it rather
      than deleting it - readers look for that answer during evaluation.
- [ ] Terminology decisions to add to `glossary.md`: **failed apply** and **reversal**, defined
      against each other, since the whole point of naming them was to stop one being read as a
      variety of the other. Neither is a UI label, so neither is bolded in prose.

**Placement**

- [ ] `sidebar_position: 40` is provisional. This page sits after About the Access tab and before
      Access tab reference; confirm against the family's existing numbering.

**Screenshots**

- [ ] Both `[SCREENSHOT: ...]` placeholders above. Neither can be captured until the feature ships.
      No fact on this page depends on a screenshot.

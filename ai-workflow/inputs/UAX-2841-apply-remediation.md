---
source: issue tracker export
key: UAX-2841
status: In Review
updated: 2026-07-30
---

# UAX-2841 · Apply a remediation recommendation from within Ridgeline

> **A fictional Jira story**, written as the kind of input this pipeline receives: a description that
> has gone stale, decisions living in the comment thread, and open questions the ticket does not know
> it has. Status is In Review - nothing in it has shipped, so anything drafted from it is
> `[UNRELEASED]`.

| Field | Value |
| --- | --- |
| **Type** | Story |
| **Status** | In Review |
| **Priority** | P1 |
| **Epic** | UAX-2100 · Close the remediation loop |
| **Sprint** | 26.14 |
| **Components** | Access Center, Integrations |
| **Labels** | `unused-access` `write-path` `needs-docs` `blocks-trial` |
| **Fix version** | 4.7 |
| **Reporter** | D. Reyes (PM) |
| **Assignee** | M. Bell |

---

## Description

Today Unused Access tells the customer what to change and then leaves them to go and do it in the
platform console. Two of the three customers currently trialling the product raised this unprompted last quarter. We want them to
apply the recommendation without leaving Ridgeline.

User is in the remediation wizard, reviews the proposed narrower role, clicks Apply. Dry run shows
what will change. User confirms. We write to the platform. There's a safety window afterwards where
the change can be rolled back to the original grant.

Internally we've been calling this one-click remediation; marketing don't love that phrase so the
final name may change. Eng call it the apply flow. Both appear below, sorry.

**In scope for 4.7**

- Platform grants with a custom role - edit the role definition, remove unused rights
- Platform grants with a built-in role - swap to the narrower built-in role
- One grant at a time

**Out of scope for 4.7**

- Bulk apply across grants. Universally requested, going to 4.8
- Directory and App-level grants - no usage data, nothing deterministic to apply
- JIT grants. S. Okafor's position is we should never touch these; not settled

Inherited grants should work since we already run the all-members analysis, but there was a
discussion about the larger reach and it may slip. TBD.

**Permissions change**

Ridgeline currently only reads from the platform, so connecting an integration was sufficient. The
write path needs permission to modify role definitions and assignments. Customers grant it at
connection time, or re-consent if already connected. Banner copy TBD.

Without write permission everything else still works and Apply is unavailable.

**Scope selection**

Trial customers asked for the ability to tighten scope while applying. The flow lets the user
optionally choose a narrower scope than the grant currently has. Defaults to the original scope.

**Limits**

Capped at 5 updates per apply, matching the recommendation cap. Enterprise have asked for 10.

---

## Acceptance criteria

- [ ] User can trigger Apply from the remediation wizard
- [ ] Dry run displays the proposed change before anything is written
- [ ] No write occurs without explicit confirmation
- [ ] Change is reversible within the safety window
- [ ] Apply is unavailable when write permission has not been granted
- [ ] Every apply and rollback is written to the integration's history
- [ ] Works correctly for inherited grants
- [ ] Handles failure gracefully

---

## Sub-tasks

| Key | Summary | Status |
| --- | --- | --- |
| UAX-2842 | Write path - custom role edit | Merged to Main |
| UAX-2843 | Write path - built-in role swap | Merged to Main |
| UAX-2844 | Dry run comparison view | In Review |
| UAX-2845 | Rollback and safety window | In Progress |
| UAX-2846 | Re-consent banner | To Do |
| UAX-2847 | History entries for apply and rollback | Merged to Main |

## Linked issues

- **blocks** UAX-2900 · Bulk apply
- **relates to** UAX-1780 · Remediation recommendations
- **relates to** UAX-2455 · Integration history export

## Attachments

- `apply-wizard-v3.fig`
- `dry-run-states.png`
- `rollback-sequence.pdf` *(from the architecture review, may be out of date)*

---

## Comments

**M. Bell** · 2026-07-22

> Description says one grant at a time but the API takes an array. We built it to accept a list
> because doing otherwise would have meant rewriting it for 2900. UI only sends one for now. Worth
> knowing that the constraint is UI-side, not backend.

**D. Reyes** · 2026-07-22

> Fine. Keep the UI at one.

**S. Okafor** · 2026-07-24

> Raising this again on JIT. A JIT grant is meant to be temporary. Applying a narrower standing role
> to something that was designed to expire changes what the grant *is*. I don't think we should
> support it in any version, not just 4.7. Nobody has responded to this.

**P. Shah** · 2026-07-25

> Design question that needs a decision: when write permission is missing, is Apply hidden or
> disabled? Eng prefer disabled with a tooltip explaining why. I think hidden is cleaner. Currently
> built as disabled because that's what was in the ticket.

**M. Bell** · 2026-07-28

> Partial failure: if the role edit succeeds and the assignment update fails, we currently leave the
> edited role in place and surface an error. No automatic rollback. This is not what the safety
> window covers - that only handles a *successful* apply the user then wants to undo. Two different
> things and I think the ticket conflates them.

**D. Reyes** · 2026-07-28

> Good catch, we'll need to name these differently. Not blocking the release.

**M. Bell** · 2026-07-29

> Scope selection is in and working. Note this means an applied remediation *can* narrow scope,
> where the recommendation engine never does. Different behaviour, same wizard.

**P. Shah** · 2026-07-30

> Success state: we show the updated grant in the table with a green flash and a toast that says
> "Remediation applied". No summary of what changed. Raised as UAX-2871, not in 4.7.

**D. Reyes** · 2026-07-30

> Legal have been clear that we cannot use "auto-remediation" anywhere in the UI or docs. A human
> confirms every change, and the copy has to make that unambiguous.

---

## Docs notes

Needs a new page or a section on the existing Access tab page - your call. The permissions change
probably affects the overview page too.

The rollback behaviour is described in more detail somewhere; I'll find the link.

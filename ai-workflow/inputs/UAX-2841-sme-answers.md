Four questions that have to be answered before the feature can be documented. This document is written after reviewing the PRD; the commit dates show that I found the gaps before anything was written.

**The capability UAX-2841 describes.**

| | |
|---|---|
| The setup | An integration is a third-party application or workload running on the customer's cloud platform. Ridgeline connects to that platform and reads the access each integration has been granted |
| The problem | Roles are usually broader than what the integration actually does. For example, a role might permit fifty actions on the cloud platform - creating resources, deleting them, changing who else can reach them - while the integration only ever performs six |
| What Unused Access does now | Reports the gap and recommends a narrower role covering the six |
| The gap this closes | The recommendation is only advice. The reader leaves Ridgeline, opens the platform's admin console, and edits the role by hand |
| What UAX-2841 adds | An **Apply** button. Ridgeline writes the change to the platform. The reader sees what will change, confirms, and can undo it |
| In release 4.7 | Platform grants only, one at a time. Whether inherited grants are included is unresolved - question 4 |
| Coming later | Bulk apply across several grants, planned for 4.8 |
| Not supported, and nobody has decided whether it ever will be | Directory and App-level grants, because there is no usage data to work from. JIT grants, unresolved - see below |

Answers are invented, since the SMEs are fictional. Numbers match the findings in
`../review/story-review-UAX-2841.md`.

---

## Questions that block the draft

Each one carries the evidence behind it, why it stops the page being written, and who can answer it.
Written to be readable alone, so a single question can go to the person who can settle it.

### 1. Can an applied remediation narrow a grant's scope?

A grant names a role and the scope it applies over - organization, workspace, project, or a single
resource. Recommendations have only ever changed the role and left the scope alone.

| | |
|---|---|
| Published page says | *"Scope is never narrowed. The replacement applies at the grant's original scope."* |
| Story says | The apply flow *"lets the user optionally choose a narrower scope than the grant currently has"* |
| M. Bell, 29 Jul | *"an applied remediation can narrow scope, where the recommendation engine never does"* |
| Why it blocks the page | An absolute guarantee becomes conditional. A reader who trusts the published version could narrow scope without realising it was possible |
| Who can answer it | M. Bell, engineer, for what the code does. Then D. Reyes, product manager - only she can decide whether the published guarantee gets rewritten |

> **Answer:**
>
> *Answered by:* · *Source:*

---

### 2. What happens when an apply partly fails, and what is each state called?

Applying is two writes: Ridgeline edits the role, then updates the grant attaching it to the
integration. Either can fail on its own.

| | |
|---|---|
| M. Bell, 28 Jul | Role edit succeeds, grant update fails, *"we leave the edited role in place and surface an error. No automatic rollback. This is not what the safety window covers"* |
| D. Reyes, same day | *"Good catch, we'll need to name these differently. Not blocking the release."* |
| Why it blocks the page | Two behaviours, one name between them - a half-applied failure, and a successful apply the reader undoes. I cannot describe either until they are named separately |
| Who can answer it | M. Bell, engineer. She raised it, and it is a question about how the code behaves |

> **Answer, with a name for each state:**
>
> *Answered by:* · *Source:*

---

### 3. How long is the safety window?

The period after a successful apply during which the reader can undo it and get the original grant
back.

| | |
|---|---|
| Story says | *"There's a safety window after apply where you can roll it back"* - no duration, twice |
| Sub-task UAX-2845 | *Rollback and safety window*, still In Progress |
| Why it blocks the page | The duration changes how carefully someone reviews before clicking Apply. Minutes and days are different features |
| Who can answer it | M. Bell, engineer. She owns the rollback sub-task |

> **Answer:**
>
> *Answered by:* · *Source:*

---

### 4. Are inherited grants included in release 4.7?

An integration gets access directly, or inherited through a team. Reducing an inherited grant affects
every member, so Ridgeline analyses what all of them use first.

| | |
|---|---|
| Description says | *"should work since we already run the all-members analysis, but there was a discussion about the larger reach and it may slip. TBD"* |
| Acceptance criteria say | *"Works correctly for inherited grants"* - listed as required |
| Why it blocks the page | The story contradicts itself, and inherited grants are a large share of what the report surfaces. The page has to either document them or exclude them |
| Who can answer it | D. Reyes, product manager. A decision about what goes in the release, not about how the code works |

> **Answer:**
>
> *Answered by:* · *Source:*

---

## Deliberately left unanswered

These go into the draft as `[VERIFY]` flags rather than invented answers.

| Open item | Why I am not answering it |
|---|---|
| The feature's final name - the story uses one-click remediation, apply flow, Apply, and guided apply | Marketing owns product naming and has not chosen. If I pick one and they choose another, the page is wrong and so is every link to it |
| Whether JIT grants will ever be supported | An engineer argued they should never be, twice, and nobody replied. There is no decision to document either way |
| Whether Apply is greyed out or absent when write permission is missing | Engineering wants it greyed out with a tooltip, design wants it hidden. Until they agree, I cannot tell the reader what they will see |
| Why the cap is five updates, and whether enterprise customers get ten | Product has not decided. A cap I cannot explain is one a reader will treat as arbitrary |
| The acceptance criterion *"handles failure gracefully"* | Nobody can verify it, so nobody can write it. Question 2 asks the answerable version instead |

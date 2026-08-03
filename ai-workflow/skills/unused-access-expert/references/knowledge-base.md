# Unused Access - knowledge base

The sourced facts behind the Unused Access feature, numbered so the skill body and any draft can
cite a section. Sections marked **Internal** inform answers but never appear on a page for readers.

**Contents:** §1 Scope · §2 Surfaces · §3 Prioritization and refresh · §4 The report ·
§5 Grant graph and grant table · §6 Measurement window and deleted resources · §7 Categories and
inheritance · §8 Usage classification · §9 Remediation engine and invariants ·
§10 Engine internals (Internal) · §11 Platform permissions · §12 Open questions · §13 Sources

---

## §1 What the feature covers, and what it does not

Unused Access identifies connected integrations holding **access they were granted but never use**,
and recommends least-privilege replacements that keep the integration working.

It is an *access* risk feature, not an integration *posture* feature. Excessive access is in scope.
Stale credentials, unreviewed external integrations, and missing review dates are posture findings
that belong to a different pillar of the product. Blurring the two is a recurring documentation
error, because both surface on the integration card.

The subject of the report is always an integration, including service accounts. Teams appear only as
the mechanism by which a grant is inherited - a team is never itself a row in the report.

## §2 Where the feature appears

| Surface | Location | What it is for |
| --- | --- | --- |
| Unused Access report | Access Center | Cross-environment prioritization: which integrations to work first |
| **Access** tab | Integration card | Per-integration investigation: which grants, which rights, what to do |

The Access tab has two views of the same data: the **grant graph** (visual, for understanding how
access reaches the integration) and the **grant table** (dense, for working through grants). The
table is the complete surface; the graph has a display condition (§5).

## §3 Prioritization and data refresh

The report sorts by **Reach score** descending, then by number of unused grants descending. The
intent is that the first screen holds the integrations where unused access matters most, not the
ones with the largest raw counts.

Unused Access has no score of its own, and it does not contribute to an integration's total score.
This is deliberate: adding a fourth score would fragment a score vocabulary readers have already
learned.

A null Reach score means no scenarios are defined for the environment. It is not a defect, and
documentation should say so, because it reliably generates support questions.

Data is recalculated on a nightly run. A grant added or used on the platform side appears after the
next run, which is the answer to "why doesn't my change show up yet."

## §4 The report

Rows are integrations. The columns readers work with most:

| Column | Notes |
| --- | --- |
| Integration | Name; links to the integration card |
| Integration type | Includes **Service account** as a value |
| Reach score | Primary sort |
| Unused grants | Count of grants with at least one unused access right |
| Grant categories | Which of Platform / Directory / App-level are present |
| Labels | Enrichment labels, including **Highly privileged** (definition unconfirmed - see §12) |

**Configure columns** and CSV export are available and behave as they do elsewhere in the product;
they need no feature-specific explanation beyond a pointer. The exact exported column set is
unconfirmed (§12).

## §5 The grant graph and the grant table

**Display condition.** The grant graph renders when the integration holds **10 or fewer grants**.
Above that threshold the table is the working surface, because a graph of dozens of grants stops
being readable. Documentation that omits this condition produces "where is my graph" tickets.

**Scope nodes** are formatted `<scope_type>: <scope_name>` - for example `Workspace: Contoso-IT-Dev`.

**Access right counts are scope- and inventory-relative.** Only rights that act on resource types
which (a) exist within the grant's scope and (b) are represented in the Integration Inventory are
counted. Consequence: the same role granted at two different scopes legitimately shows different
right counts. This is the answer to "why do two identical roles show different numbers." Never
present a count as the absolute size of the role definition.

## §6 The measurement window and deleted resources

Usage is derived by correlating access rights against activity-log records within a window of
**90 days by default**. The window is configurable internally; whether readers can configure it is
unconfirmed (§12).

**Usage on a resource that has since been deleted still counts as usage.** This is a deliberate
design decision, not a gap: create-use-delete workflows are legitimate, and an integration that
provisions and tears down resources would otherwise appear to hold unused access it genuinely needs.
Never describe deleted-resource usage as noise to be filtered out.

Activity logs audit control-plane actions only. Anything that happens purely inside a resource is
invisible to the logs, which is what produces the Undetermined classification (§8).

## §7 Grant categories, inheritance, and JIT

### Category asymmetry

| Category | What it governs | Usage data | Scopes and accessible services | Remediation basis |
| --- | --- | --- | --- | --- |
| **Platform** | Workspace platform infrastructure | Full, log-correlated | Yes | Data-driven: usage per right |
| **Directory** | The workspace directory | None | No | Security posture (external, inactive) |
| **App-level** | Access inside one application | None | No | Best practice (for example write to read-only) |

Only Platform grants carry usage data. Attributing usage analysis or data-driven remediation to
Directory or App-level grants is the most common plausible-sounding factual error in this feature,
because the three categories sit side by side in one table.

### Direct and inherited

A grant is **Direct** (assigned to the integration) or **Inherited** (assigned to a team the
integration belongs to). For inherited grants, the graph and table show only the team holding the
*direct* assignment - not the full nested-team chain - because remediation happens at that team.
Document this as remediation-oriented design, not as a display limitation.

The team members drawer lists the integrations affected by a team's grant, which is what makes an
inherited-grant recommendation reviewable before it is applied.

### JIT grants

**JIT grants** (Just-In-Time) provide temporary rather than standing access, and sit as a
sub-category under Directory. Only JIT grants detected as **active** are shown. They receive
best-practice recommendations rather than deterministic rewriting, because a grant that is meant to
be temporary cannot be evaluated as though it were standing access.

## §8 Usage classification - the safety guarantee

Every access right within a Platform grant is classified:

| Value | Meaning |
| --- | --- |
| **Used** | An activity-log record exists within the window |
| **Unused** | The right is auditable, and no record exists within the window |
| **Undetermined** | The right is not auditable in the activity logs at all |

**Undetermined rights are strictly treated as Used, and are never removed by remediation advice.**
The reason is asymmetric cost: removing access the integration silently depends on breaks a
production workload, while leaving an unaudited right in place carries a bounded risk. The feature
resolves that asymmetry in favour of not breaking things.

Consequences for documentation:

- Never present Undetermined as a variety of unused, a "probably unused," or a lower-confidence
  Unused. It is a distinct third state with the opposite remediation outcome.
- Never write a sentence that leaves open the possibility that remediation might strip an
  undetermined right.
- When a total is given, be explicit about which states it sums. "Unused rights" and "rights not
  observed in the logs" are different numbers.

## §9 Remediation engine and invariants

The engine proposes a least-privilege replacement for a grant, derived from the usage of its rights.

**Invariants that hold in every case:**

1. **Scope is preserved.** The replacement applies at the original scope. No recommendation ever
   narrows scope, and documentation must never describe one as doing so.
2. **Team membership is preserved.** Remediation never removes an integration from a team.
3. **Inherited grants are evaluated across all team members.** The union of what every member
   actually uses is retained, so applying the recommendation cannot strip access from an active
   member who was not the integration under investigation.
4. **Undetermined rights are retained** (§8).

**How the replacement is chosen:**

| Grant holds | Approach |
| --- | --- |
| A built-in role | Substitute the narrowest built-in role that still covers all retained rights |
| A custom role | Edit the role definition, removing only unused rights |
| An already-edited custom role | Recommend reviewing the existing definition rather than re-deriving it |
| A Directory grant | Posture-based guidance (external, inactive), not right-level rewriting |
| An App-level grant | Best-practice guidance, for example reducing write access to read-only |

Guidance is capped at **five updates at a time**, so that a recommendation stays reviewable. This is
a usability decision, not a technical ceiling.

## §10 Engine internals - Internal, never publish

The engine exposes configuration flags governing whether rights used in known risk scenarios are
removed, and how undetermined rights are weighted in the calculation. Defaults implement the
guarantees in §8 and §9. There is also an internal API surface used by the card and the report.

Use this section to answer behavior and support questions precisely. It never appears on a page
written for readers: flag names and internal endpoints date quickly, cannot be acted on by a reader,
and imply a configurability that is not exposed.

## §11 Platform permissions Ridgeline needs

Unused Access requires **no additional platform permissions**. It reuses the permissions granted
when the integration was connected, and reads activity logs already available under them.

This is asked in nearly every evaluation, so overview pages should state it proactively rather than
waiting to be asked. Note the terminology trap: "platform permissions" (what Ridgeline itself needs)
is a deliberately distinct concept from "access rights" (what the feature measures). Keep them
lexically separate - see `glossary.md`.

## §12 Open questions

| Question | Status |
| --- | --- |
| Exact definition and criteria of the **Highly privileged** label | Unconfirmed - do not define it in copy |
| The CSV export column set | Unconfirmed - describe export generically |
| Whether the 90-day window is reader-configurable | Unconfirmed - write "by default, 90 days" and stop there |
| Whether nested-team chains will become expandable | Unconfirmed - do not promise it |

When one of these surfaces, say it is unconfirmed and flag it for SME verification. Fold confirmed
answers back into this file with the source and date, and remove the row.

## §13 Sources and snapshot

Compiled from the feature notes in `ai-workflow/inputs/` and product walkthroughs. **Snapshot date:
2026-07-28.** Facts sourced from notes still marked *In development* at the snapshot describe
pre-release behavior; when a published page in `docs/` contradicts this file for a **Shipped**
feature note, the page wins and this file should be updated.

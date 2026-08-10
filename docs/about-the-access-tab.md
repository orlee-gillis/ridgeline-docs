---
title: About the Access tab
description: What each part of the Access tab shows, how to read the grant graph and grant table, and how to reach a remediation decision.
sidebar_position: 30
---

The **Access** tab on an integration's card is where you investigate one integration's access and
decide what to reduce. It answers three questions: what the integration can do, how it got that
access, and which of it goes unused.

You reach the tab either from a row in the [Unused Access report](unused-access-report.md), or by
opening an integration card from anywhere and selecting **Access**.

![The Access tab on an integration card, showing the access summary and grant table](/img/access-tab.png)

The tab has four parts, read in this order:

| Part | What it is for |
| --- | --- |
| **Integration information panel** | Context on the integration itself, before you look at its access |
| **Access summary** | The size of the problem, in four numbers |
| **Access analysis** | The grant graph and grant table, where you work out what to reduce |
| **Remediation recommendations** | The proposed narrower access, and how to apply it |

## Integration information panel

The panel gives you a quick read on the integration and its risk before you examine individual
grants.

![The integration information panel, showing basic details, labels, and Reach score](/img/information-panel.png)

| Section | What it shows |
| --- | --- |
| **Basic details** | Name of the integration as it appears in your **Integration Inventory** |
| **Action bar** | Actions for watching the integration, adding comments, and suppressing it |
| **Labels** | Enrichment labels Ridgeline adds automatically, and custom labels you or your cloud platform add |
| **Integration properties** | Integration fields from your **Integration Inventory**. Which properties appear varies by environment type |
| **Scores and impact** | **Reach score** - how much of the environment an attacker could affect by compromising this integration |

To collapse the panel and give the rest of the tab more room, click the button at its top right.

## Access summary

Four counters across the top of the tab size up the integration's access.

![The access summary, showing grant count, accessible services, accessible resources, and unused access rights](/img/access-summary.png)

| Counter | What it shows |
| --- | --- |
| **Access grants** | How many grants give this integration access |
| **Accessible services** | How many services it can reach |
| **Accessible resources** | How many individual resources it can reach within those services |
| **Unused access rights** | How many of its rights go unused, against the total it holds |

By default, a right counts as unused when the activity logs show no use of it for 90 days.

## Access analysis

Access analysis is where you decide what to reduce. It offers three views of the same data, and they
answer different questions:

- **Grant graph** - how access reaches the integration. Use it when you need to understand the
  shape of the access: which grants, through which teams, over which resource types.
- **Grant table** - every grant in one flat list, with drill-down to individual rights and the
  resources they touch. Use it when there is volume to work through, or when you need exact numbers.
- **Remediation recommendations** - what to change. Use it once you know which grants matter.

An integration with a handful of grants is usually fastest to understand in the graph. One with
dozens is faster in the table.

## Read the grant graph

The grant graph shows how access arrives at the integration. Each arrow is a relationship that
carries access.

:::note
The graph appears when the integration has 10 or fewer access grants. Above that, only the grant
table appears - a graph of dozens of grants stops being readable.
:::

Read each path from the integration outward:

**Integration → (Team membership →) Grant → Resources**

| Element | What it is |
| --- | --- |
| **Integration node** | The leftmost node: the integration you are investigating |
| **Team membership node** | Present when access is inherited. This is the team that holds the grant, and it contains the team's members |
| **Grant node** | The middle node: the grant itself, showing role name, **Type** (**Built-in** or **Custom**), **Category**, **Scope**, and whether it is a JIT grant |
| **Resource type group node** | The rightmost node: a service the integration can reach, containing each resource of that type |
| **Grant paths** | The lines between nodes, showing how access is derived |
| **Action bar** | **Reset graph** returns the graph to its default view. **Show legend** toggles the resource type legend |

![The grant graph, showing how access reaches the integration through direct and inherited paths](/img/grant-graph.png)

What the grant node's own fields tell you:

- **Category** is where the grant comes from. **Platform** grants manage cloud platform
  infrastructure and are the only category with usage data. **Directory** grants administer the
  workspace directory. **App-level** grants apply inside a single application.
- **Scope** is the range the grant's access applies over, from largest to smallest:
  **Organization**, **Workspace group**, **Workspace**, **Project**, **Resource**. A wider scope
  covers more resources, so it usually offers more to gain from reducing.
- **JIT** marks a grant providing Just-In-Time rather than standing access. Only JIT grants detected
  as active appear.

:::note
For inherited access, the graph shows the team that holds the grant directly. Nested teams above it
are not shown, because remediation happens at the team holding the grant.
:::

Use the graph to prioritize: the resource types a grant reaches, and how many resources, tell you
which grant is worth reducing first.

### Expand a node

Nodes with a number badge contain other items. Double-click to open one. Fewer than 20 items expand
in place; more open in a drawer.

- Expanding a **team membership** node shows every team member, including this integration.
- Expanding a **resource type** node shows every resource of that type the integration can reach.

### Resource type legend

Resource type nodes carry indicators as well as a count.

![A resource type node, with its resource count, critical-resource marker, and usage bands](/img/resource-node-legend.png)

| Indicator | What it shows |
| --- | --- |
| **Resource count** | Grey badge on the right: how many individual resources the node contains |
| **Critical resources** | Red hexagon at the top: the node contains at least one resource Ridgeline identifies as critical |
| **Used access rights** | Green band: the share of granted rights used across resources of this type |
| **Unused access rights** | Red band: the share not used |
| **Undetermined access rights** | Grey band: the share whose usage the activity logs cannot determine |

:::important
**Undetermined** rights are ones the activity logs cannot audit at all. Ridgeline treats them as
used, and remediation advice never removes them. **Undetermined** is not a lower-confidence form of
**Unused**.
:::

## Work through the grant table

The grant table lists every grant for the integration, one per row, and lets you drill down two
levels: from a grant to its individual access rights, and from a right to the resources it reaches.

![The grant table drilled down from a grant to its access rights and the resources they reach](/img/grant-drilldown.png)

Every grant has a **Grant category**, **Role type**, and **Grant type**. Only **Platform** grants
carry scope, accessible services, accessible resources, and usage data - **Directory** and
**App-level** rows leave those columns blank.

<details>
<summary>Grant table columns</summary>

| Column | What it shows |
| --- | --- |
| **Role name** | Name of the role granted to the integration |
| **Grant category** | Where the grant comes from: **Platform**, **Directory**, or **App-level** |
| **Role type** | **Built-in** or **Custom** |
| **Grant type** | **Direct** if the grant names the integration, **Inherited** if it reaches the integration through a team |
| **Accessible services** | How many services this grant opens up |
| **Accessible resources** | How many individual resources within those services |
| **Access right usage** | Distribution of **Used**, **Unused**, and **Undetermined** rights this grant confers. Hover the bar for exact counts |
| **Critical resources** | How many of the accessible resources are critical |
| **Scope type** | The scope level the grant applies at |
| **Scope name** | Name of that scope |
| **Inherited from** | For inherited grants, the team that holds the grant. Click the name to see its members |
| **JIT** | Whether this is a JIT grant |
| **Grant ID** | Non-default column: the grant's full unique identifier |

</details>

Access right counts are relative to scope and inventory. Only rights acting on resource types that
exist within the grant's scope and appear in your **Integration Inventory** are counted, so the same
role at two different scopes legitimately shows different numbers.

### How to prioritize

- Start with wide-scope grants. They reach the most.
- Review JIT grants and set activation to temporary where you can.
- Work on rights marked risky or unused first.
- Use the resource-level view to confirm whether a right is genuinely used, and where.

### Drill into a grant's rights

Click a grant row to see its individual access rights.

| Field | What it shows |
| --- | --- |
| **Resource type** | Which kind of resource this right acts on |
| **Resources** | How many resources of that type were detected |
| **Last used** | When the right was last used on any of those resources. Empty when **Undetermined usage** is **True** |
| **Unused period** | How long since that last use. Empty when **Last used** is empty |
| **Risky access right** | **True** when the right appears in known escalation paths |
| **Undetermined usage** | Non-default column. **True** means the activity logs carry no usage data for this right |

### Drill into a right's resources

Click an access right to see the resources it reaches, with usage for each one. Use it to find which
resource accounts for the last use, and when.

The **Deleted** column shows whether a resource has since been deleted. Usage on a deleted resource
still counts as usage - integrations that create, use, and tear down resources are doing legitimate
work, and would otherwise look like they hold access they do not need.

## Remediation recommendations

Every grant has a recommended action giving step-by-step instructions for reducing the integration's
access to what it uses. Apply them to enforce the Principle of Least Privilege once you have
finished investigating.

To open the recommendations, click **Show remediations** from either the graph or the table.

Two guarantees hold for every recommendation:

- **Scope is never narrowed.** The replacement applies at the grant's original scope.
- **Team membership is never changed.** No recommendation removes an integration from a team.

There is one recommendation per grant. Use the arrows in the wizard header to move between them.

![The remediation wizard, comparing the current role with the proposed narrower one](/img/remediation-wizard.png)

### What the wizard proposes

The proposed change depends on what the grant holds:

| Grant holds | Proposed change |
| --- | --- |
| A **Built-in** role | The narrowest built-in role that still covers every right in use |
| A **Custom** role | An edited version of the role, with unused rights removed |
| No suitable built-in alternative | A new custom role |
| An inherited grant | Access reduced to the minimum every team member uses |

Recommendations cap at five updates at a time, so each one stays reviewable.

### Remediation labels

Each recommendation carries labels describing what kind of change it is.

![A remediation card showing its characteristic labels: inherited grant, team-level remediation, and the team name](/img/remediation-labels.png)

| Label | What it means |
| --- | --- |
| **Direct grant** | The simplest case - the change affects only this integration |
| **Inherited grant** | The change applies to the whole team. Only rights that no team member has used are removed |
| **Team-level remediation** | Accompanies **Inherited grant**: confirms the recommendation accounts for every team member's usage |
| **Team** | Accompanies **Inherited grant**: the team's name and member count |

For inherited grants, the recommendation is calculated from the union of what every team member
actually uses, so applying it cannot strip access from an active member.

When you have reviewed the proposed changes, export the plan as a PDF.

## Related

- [About the Unused Access report](unused-access-report.md)

## Open items for SME review

- [ ] **Integration Inventory** has no page yet - referenced as plain text rather than linked
- [ ] `[VERIFY: whether the integration information panel carries a visible label in the UI, and what it is]`
- [ ] `[VERIFY: "escalation paths" as the description for a risky access right]` - awaiting terminology sign-off
- [ ] `[VERIFY: whether Grant ID is the correct column name]`
- [ ] Confirm whether the 90-day usage window is configurable by the reader

Please note this is a test, e.g. a deliberate one.
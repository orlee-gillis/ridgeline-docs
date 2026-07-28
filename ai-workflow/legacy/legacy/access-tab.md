# About the Access tab

## Introduction

The **Access** tab includes the following:

- [Integration information panel](#integration-information)

- [Access summary](#access-summary)

- [Access analysis](#access-analysis), where you can see the:

  - [Grant graph](#grant-graph)

  - [Grant table](#grant-table)

  - [Remediation recommendations](#remediation-recommendations)

The sections together provide detailed context for the integration and its access, explaining what the integration can do (i.e., which access rights it is granted) and how those rights are granted to it. Your goal is to understand the access an integration has and where it got it from.

## Integration information

The information panel provides a concise overview of risk scores and integration properties to quickly assess security status. It includes integration information such as labels, properties, and risk scores.

| **Section**                | **Description**                                                                                                                                                    |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Basic details**          | The name of the integration as it appears in your [Integration Inventory](integration-inventory.md).                                                                |
| **Action bar**             | Provides actions for watching the integration, adding comments, and suppressing the integration.                                                                     |
| **Labels**                 | Shows enrichment labels that Ridgeline adds automatically and custom labels that you or your workspace platform add.                                                |
| **Integration properties** | Shows integration fields from the [Integration Inventory](integration-inventory.md). The displayed properties vary by environment type.                             |
| **Scores and impact**      | **Reach score**: The degree of risk that an attacker may compromise an integration and affect critical assets. `[MAP-1]` `[MAP-2]`                                  |

If you understand the integration context and want to focus on the other sections of the **Access** tab, you can hide the integration information panel by clicking the button on the top right of the panel.

`[SCREENSHOT: the collapse button at the top right of the integration information panel]`

## Access summary

At the top is the integration's access summary that shows the following:

- **Access Grants**: The number of access grants that give the integration access.

- **Accessible Services**: The number of services (i.e., resource types) that the integration has access to. For more, see [here](access-tab-reference.md#accessible-resource-types).

- **Accessible Resources**: The number of resource instances that the integration has access to.

- **Unused Access Rights**: The number of unused access rights compared to the total rights that the integration has.

`[SCREENSHOT: the access summary strip showing the four counters across the top of the tab]`

Next, you use the [grant graph](#grant-graph) and table to analyze how the integration is granted access to each target resource, the type of access it has, and which rights it actually uses.

## Access analysis

The access analysis section is where you investigate the integration's effective access and decide what to remediate. It contains the [grant graph](#grant-graph), the [grant table](#grant-table), and [remediation recommendations](#remediation-recommendations).

### Grant graph

Use the **Grant graph** to visualize how the integration has access, and what access it has to each resource type. Each arrow is a relationship that carries (or enables) access flow.

**Note**: The grant graph appears if the integration has up to 10 access grants that give it access. If it has more, then only the [grant table](#grant-table) appears.

Each grant path consists of the following elements:

<table>
<thead>
<tr>
<th><p><strong>Element</strong></p></th>
<th><p><strong>Description</strong></p></th>
<th><p><strong>Example</strong></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><strong>Integration node</strong></p></td>
<td><p>The focal, left-most node that is the integration you're looking at.</p></td>
<td><p><code>[SCREENSHOT: a single integration node as it appears at the left edge of the graph]</code></p></td>
</tr>
<tr>
<td><p><strong>Team membership node</strong></p></td>
<td><p>If the integration has inherited access from a team, the second node in the path is the team that grants that access to the integration, and it contains all the team's members.</p>
<p><strong>Note</strong>: We only show teams with directly assigned roles - we don't show any nested teams under the team.</p></td>
<td><p><code>[SCREENSHOT: a team membership node with its member-count badge]</code></p></td>
</tr>
<tr>
<td><p><strong>Grant node</strong></p></td>
<td><p>The middle node that is the <a href="access-tab-reference.md#grant-inheritance">access grant</a> that gives the integration access. Includes the role name, <strong>Type</strong> (either <strong>Built-in</strong> or <strong>Custom</strong>), <a href="access-tab-reference.md#grant-categories">Category</a>, <a href="access-tab-reference.md#grant-scopes">Scope</a>, and whether it's a <a href="access-tab-reference.md#jit-grants">JIT grant</a>.</p></td>
<td><p><code>[SCREENSHOT: a grant node showing role name, Type, Category, and Scope]</code></p></td>
</tr>
<tr>
<td><p><strong>Resource type group node</strong></p></td>
<td><p>The right-most node that is the <a href="access-tab-reference.md#accessible-resource-types">resource type (i.e., service)</a> that the integration can access and contains each resource instance of its type.</p></td>
<td><p><code>[SCREENSHOT: a resource type group node with its resource-count badge]</code></p></td>
</tr>
<tr>
<td><p><strong>Resource type group legend</strong></p></td>
<td><p>Helps you understand the visual language of the resource type nodes - <a href="#resource-type-group-legend">Resource type group legend</a></p></td>
<td><p><code>[SCREENSHOT: the expanded resource type group legend]</code></p></td>
</tr>
<tr>
<td><p><strong>Grant paths</strong></p></td>
<td><p>Lines between nodes that represent how access is derived.</p></td>
<td><p><code>[SCREENSHOT: the connecting lines between two nodes]</code></p></td>
</tr>
<tr>
<td><p><strong>Action bar</strong></p></td>
<td><p>Options (icons) you can click on to customize your grant graph display:</p>
<ul>
<li><p><code>[SCREENSHOT: reset icon]</code> <strong>Reset graph</strong>: Click to return the graph to its default view.</p></li>
<li><p><code>[SCREENSHOT: legend icon]</code> <strong>Show legend</strong>: Click to toggle showing/hiding the <strong>Resource type legend</strong>.</p></li>
</ul></td>
<td><p><code>[SCREENSHOT: the vertical action bar beside the graph]</code></p></td>
</tr>
</tbody>
</table>

The graph's role is to help you prioritize the access to remediate based on the resource types and the number of resources an access grant gives access to.

You read each grant path from the integration outward to see how access is derived:
**Integration → (Team membership →) Grant → Resources**

#### Use the grant graph

The grant graph visualization includes expandable nodes containing underlying integrations. Expandable nodes have a number badge on the node that indicates how many items it contains. The two types of expandable nodes in the grant graph are **team membership** and **resource type** nodes. Double-click a node to view its underlying items. If the node contains fewer than 20 items, it expands within the graph to show them; otherwise, a drawer appears.

- Expand a team membership node to see all the team members, including the integration itself.

- Expand a resource type node to see all the resource instances of that type that the integration can access.

The resource type node also shows you indicators in addition to the number of resources it contains, which is explained in the legend.

##### **Resource type group legend** `[MAP-6]`

The legend shows an example resource type node as a reference:

`[SCREENSHOT: annotated resource type node showing count badge, critical-asset marker, and the used/unused/undetermined bands]`

- **Resource count**: The number in the grey badge on the right-hand side of the node. Shows how many individual resources (meaning resource instances) the node contains.

- **Critical assets**: The red hexagon at the top of nodes that contain at least one resource, which Ridgeline identifies as critical assets. `[MAP-2]`

- **Used access rights**: The green section of the node. Shows the ratio of the integration's granted rights that are used for all the resources of that type.

- **Unused access rights**: The red section of the node. Shows the ratio of the integration's granted rights that are not used for all the resources of that type.

- **Undetermined access rights**: The grey section of the node. Shows the ratio of the integration's granted rights with unknown usage across all resources of that type.

For more on access right usage, see [Access right usage calculations](access-tab-reference.md#access-right-usage-calculations).

### Grant table

The **Grant table** (i.e., the access grant table) shows a flat list of all access grants for a given integration. You use it to see what the integration can do and where it can do it. It has all the functionality of the [grant graph](#grant-graph) and also lets you drill down several levels:

1.  From each access grant to the access right list under the grant

2.  From each access right to the resources it gives access to

`[SCREENSHOT: the grant table with one row per access grant and the drill-down chevron on each row]`

Each row is an access grant. Every access grant has a **Grant category**, **Role type**, and **Grant type** value**.** Only access grants of the **Platform** category have the integration's granted scope type, accessible services, accessible resources, and access right usage from the grant.

Here are the grant table columns:

<details>
<summary>Click to view columns</summary>

| **Column**                | **Description**                                                                                                                                                                                                     |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Role name**             | The name of the role that's granted to the integration                                                                                                                                                              |
| **Grant category**        | The category of access that's granted, where it's assigned from (see [Grant categories](access-tab-reference.md#grant-categories))                                                                                   |
| **Role type**             | Whether it's a **Built-in** or **Custom** role                                                                                                                                                                      |
| **Grant type**            | Whether it's a **Direct** or **Inherited** access grant (see [Grant inheritance](access-tab-reference.md#grant-inheritance)) `[MAP-3]`                                                                               |
| **Accessible services**   | The number of [services (i.e., resource types)](access-tab-reference.md#accessible-resource-types) that the access grant gives the integration access to                                                             |
| **Accessible resources**  | The number of resources (i.e., instances) of the accessible services that the access grant gives the integration access to                                                                                           |
| **Access right usage**    | The total number and distribution of [used, unused, and undetermined access rights](access-tab-reference.md#access-right-usage-calculations) granted to the integration by the access grant across all the accessible services<br />*Hover over the bar to see exact counts* |
| **Critical assets**       | The number of resources, out of the total accessible resources, that Ridgeline identifies as critical assets `[MAP-2]`                                                                                               |
| **Scope type**            | The scope type of the access grant (see [Grant scopes](access-tab-reference.md#grant-scopes))                                                                                                                        |
| **Scope name**            | The name of the scope of the access grant (see [Grant scopes](access-tab-reference.md#grant-scopes))                                                                                                                 |
| **Inherited from**        | For **Inherited** access grants, the name of the team that grants the integration the role (see [Grant inheritance](access-tab-reference.md#grant-inheritance))<br />*Click the name to view the team members.*        |
| **JIT**                   | Whether it's a JIT grant (see [JIT grants](access-tab-reference.md#jit-grants))                                                                                                                                      |
| **Grant ID**              | A non-default column that shows the full unique identifier of the access grant `[MAP-4]`                                                                                                                             |

</details>

#### Investigate an access grant's rights

To investigate an integration's [grant table](#grant-table), click an access grant row to drill into its underlying individual access rights.

- **Resource type**: Which kind of resources the access right can act on.

- **Resources**: How many resources of those types we detected.

- **Last used**: The last time the access right was used across all those detected resources. Usage on any single resource counts. This is empty if the **Undetermined usage** value is **True**.

- **Unused period**: The length of time since the access right was last used. This is empty if the **Last used** value is empty, and might also be empty if the **Last used** value is **Unused**.

- **Risky access right**: True means the access right is used in known escalation paths. `[MAP-5]`

- **Undetermined usage**: A non-default column that shows whether we could read usage data for that access right. If **True**, the right is one for which usage data couldn't be determined. See [Access right usage calculations](access-tab-reference.md#access-right-usage-calculations) for more.

#### Investigate an access right's resources

Click an access right to drill into its accessible resources.

`[SCREENSHOT: the resource-level list under a single access right, showing per-resource usage and the Deleted column]`

The resource list shows the integration's access right usage for each specific resource. Use it to find which resource caused the last use, and when. It also shows the **Deleted** column, which tells you whether the resource was deleted.

**Table insights**:

- Start by looking at high-scope grants. They usually have the largest reach.

- Review JIT grants and set activations to temporary when possible.

- Focus first on access rights marked Risky or unused.

- Use the resource-level view to verify if an access right is actually used and where.

### Remediation recommendations

Each access grant in the [grant table](#grant-table) has a recommended remediation action that provides tailored, step-by-step instructions for reducing the integration's access to only what it needs. Use the recommended remediation to enforce the Principle of Least Privilege (PoLP) after you investigate an integration's access.

To see remediations, from either the [grant graph](#grant-graph) or [table](#grant-table), click **Show remediations** to open the integration's remediation wizard.

`[SCREENSHOT: the Show remediations button above the grant table]`

There's a remediation for each access grant. Each access grant displays labels for characteristics relevant to the remediation under the grant name.

`[SCREENSHOT: a remediation card with the grant name and its characteristic labels beneath]`

The possible labels are:

- **Direct grant**: Simplest remediation, as you only remove access for the individual integration.

- **Inherited grant**: You remediate the access for the entire team. The recommended remediation only removes access rights that no one on the team has used. With this label comes another two labels:

  - **Team-level remediation**: Reminder that the recommendation accounts for the access right usage of all the team members

  - **Team**: The team name and the number of members

See [here](access-tab-reference.md#grant-inheritance) for more about grant inheritance.

Click the arrows to navigate through the different access grants' remediations:

`[SCREENSHOT: the previous/next arrows in the remediation wizard header]`

The wizard proposes context-aware actions, for example:

- Refining a custom role

- Creating a new custom role if a built-in role cannot be edited

- Adjusting team-based grants to the minimal usage level of all the team members.

After you review the proposed changes, export the plan as a PDF: `[SCREENSHOT: the export-to-PDF icon]`

For more information, see [How we determine recommendations](access-tab-reference.md#how-we-determine-recommendations).


Screenshots are placeholders throughout and need to be captured against the Ridgeline UI.

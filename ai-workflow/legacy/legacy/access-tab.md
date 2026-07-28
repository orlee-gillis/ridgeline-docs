# About the Permissions tab

## Introduction

The **Permissions** tab includes the following:

- [Entity information panel](https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2565832708/About+the+Permissions+tab#Entity-information)

- [Permissions summary](https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2565832708/About+the+Permissions+tab#Permissions-summary)

- [Permissions analysis](https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2565832708#PermissionAnalysis), where you can see the:

  - [Permission graph](https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2565832708#PermissionGraph)

  - [Permission table](https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2565832708#PermissionTable)

  - [Remediation recommendations](https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2565832708#RemediationRecommendations)

The sections together provide detailed context for the identity and its permissions, explaining what the identity can do (i.e., which permissions it is granted) and how those permissions are granted to it. Your goal is to understand the access an identity has and where it got it from.

## Entity information

The information panel provides a concise overview of risk scores and identity properties to quickly assess security status. It includes entity information such as entity labels, properties, and risk scores.

| **Section**           | **Description**                                                                                                                                                                     |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Basic details**     | The name of the entity as it appears in your [Entity Inventory](https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/237502465/Entity+Inventory).                                    |
| **Action bar**        | Provides actions for watching the identity, adding comments, and suppressing the entity.                                                                                            |
| **Labels**            | Shows enrichment labels that XM Cyber adds automatically and custom labels that you or your cloud platform add.                                                                     |
| **Entity properties** | Shows entity fields from the [Entity Inventory](https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/237502465/Entity+Inventory). The displayed properties vary by environment type. |
| **Scores and impact** | **Choke point score**: The degree of risk that an attacker may compromise an entity and impact critical assets.                                                                     |
|                       | **Compromise score**: The risk that an attacker might compromise the entity.                                                                                                        |
|                       | **Outbound risk**: The number of critical assets compromised by the entity. Hover to see the compromised entities and critical assets.                                              |

If you understand the entity context and want to focus on the other sections of the **Permissions** tab, you can hide the identity information panel by clicking the button on the top right of the panel.

![image-20260517-115730.png](images/image-20260517-115730.png)

## Permissions summary

At the top is the identity’s permissions summary that shows the following:

- **Role Assignments**: The number of role assignments that grant the identity permissions.

- **Accessible Services**: The number of services (i.e., resource types) that the identity has permissions over. For more, see [here](https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2566357009/Permissions+tab+reference#AccessibleResourceTypes-services).

- **Accessible Resources**: The number of resource instances that the identity has permissions over.

- **Unused Permissions**: The number of unused permissions compared to the total permissions that the identity has.

![image-20260623-125529.png](images/image-20260623-125529.png)

Next, you use the [permission graph](https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2565832708#PermissionGraph) and table to analyze how the identity is granted permissions to access each target resource, the type of access it has, and which permissions it actually uses.

## Permission analysis

The permission analysis section is where you investigate the identity's effective permissions and decide what to remediate. It contains the [permission graph](https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2565832708#PermissionGraph), the [permission table](https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2565832708#PermissionTable), and [remediation recommendations](https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2565832708#RemediationRecommendations).

### Permission graph

Use the **Permission graph** to visualize how the identity has permissions, and what access it has to each resource type. Each arrow is a relationship that carries (or enables) permission flow.

**Note**: The permission graph appears if the identity has up to 10 role assignments that grant it access. If it has more, then only the [permission table](https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2565832708#PermissionTable) appears.

Each permission path consists of the following elements:

<table>

<thead>
<tr class="header">
<th><p><strong>Element</strong></p></th>
<th><p><strong>Description</strong></p></th>
<th><p><strong>Example</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Identity node</strong></p></td>
<td><p>The focal, left-most node that is the identity you’re looking at.</p></td>
<td><img src="images/image-20260514-110634.png" alt="image-20260514-110634.png" /></td>
</tr>
<tr class="even">
<td><p><strong>Group membership node</strong></p></td>
<td><p>If the identity has inherited permissions from a group, the second node in the path is the group that grants those permissions to the identity, and it contains all the group's members.</p>

<p><strong>Note</strong>: We only show groups with directly assigned roles - we don’t show any nested groups under the group.</p>

</td>
<td><img src="images/image-20260514-110742.png" alt="image-20260514-110742.png" /></td>
</tr>
<tr class="odd">
<td><p><strong>Role assignment node</strong></p></td>
<td><p>The middle node that is the <a href="https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2566357009/Permissions+tab+reference#RoleAssignmentInheritance">role assignment</a> that grants the identity permissions. Includes the role name, <strong>Type</strong> (either <strong>Built-in</strong> or <strong>Custom</strong>), <a href="https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2566357009/Permissions+tab+reference#RoleCategories">Category</a>, <a href="https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2566357009/Permissions+tab+reference#RoleAssignmentScopes">Scope</a>, and whether it’s a <a href="https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2566357009/Permissions+tab+reference#PimRoleAssigments">PIM assignment</a>.</p></td>
<td><img src="images/image-20260514-115159.png" alt="image-20260514-115159.png" /></td>
</tr>
<tr class="even">
<td><p><strong>Resource type group node</strong></p></td>
<td><p>The right-most node that is the <a href="https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2566357009/Permissions+tab+reference#AccessibleResourceTypes-services">resource type (i.e., service)</a> that the identity can access and contains each resource instance of its type.</p></td>
<td><img src="images/image-20260514-115850.png" alt="image-20260514-115850.png" /></td>
</tr>
<tr class="odd">
<td><p><strong>Resource type group legend</strong></p></td>
<td><p>Helps you understand the visual language of the resource type nodes - <a href="https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2565832708#ResourceTypeGroupLegend">Resource type group legend</a></p></td>
<td><img src="images/image-20260514-114524.png" alt="image-20260514-114524.png" /></td>
</tr>
<tr class="even">
<td><p><strong>Permission paths</strong></p></td>
<td><p>Lines between nodes that represent how access is derived.</p></td>
<td><img src="images/image-20260514-114422.png" alt="image-20260514-114422.png" /></td>
</tr>
<tr class="odd">
<td><p><strong>Action bar</strong></p></td>
<td><p>Options (icons) you can click on to customize your permission graph display:</p>
<ul>
<li><p><img src="images/image-20260429-113441.png" alt="image-20260429-113441.png" /> <strong>Reset graph</strong>: Click to return the graph to its default view.</p></li>
<li><p><img src="images/image-20260514-131900.png" alt="image-20260514-131900.png" /> <strong>Show legend</strong>: Click to toggle showing/hiding the <strong>Resource type legend</strong>.</p></li>
</ul></td>
<td><img src="images/image-20260514-132053.png" alt="image-20260514-132053.png" /></td>
</tr>
</tbody>
</table>

The graph’s role is to help you prioritize the permissions to remediate based on the resource types and the number of resources a role assignment grants access to.

You read each permission path from the identity outward to see how access is derived:
**Identity → (Group membership →) Assignment → Resources**

#### Use the permission graph

The permission graph visualization includes expandable nodes containing underlying entities. Expandable nodes have a number badge on the node that indicates how many entities it contains. The two types of expandable nodes in the permission graph are **group membership** and **resource type** nodes. Double-click a node to view its underlying entities. If the node contains fewer than 20 entities, it expands within the graph to show them; otherwise, a drawer appears.

- Expand a group membership node to see all the group members, including the identity itself.

- Expand a resource type node to see all the resource instances of that type that the identity can access.

The resource type node also shows you indicators in addition to the number of resources it contains, which is explained in the legend.

##### **Resource type group legend**

The legend shows an example resource type node as a reference:

![image-20260514-114524.png](images/image-20260514-114524.png)

- **Resource count**: The number in the grey badge on the right-hand side of the node. Shows how many individual resources (meaning resource instances) the node contains.

- **Critical assets**: The red hexagon at the top of nodes that contain at least one resource, which XM CEM identifies as critical assets.

- **Used permissions**: The green section of the node. Shows the ratio of the identity’s granted permissions that are used for all the resources of that type.

- **Unused permissions**: The red section of the node. Shows the ratio of the identity’s granted permissions that are not used for all the resources of that type.

- **Undetermined permissions**: The grey section of the node. Shows the ratio of the identity’s granted permissions with unknown usage across all resources of that type.

For more on permission usage, see [Permission usage calculations](https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2566357009/Permissions+tab+reference#PermissionUsageCalculations).

### Permission table

The **Permission table** (i.e., the role assignment table) shows a flat list of all role assignments for a given identity. You use it to see what the identity can do and where they can do it. It has all the functionality of the [permission graph](https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2565832708#PermissionGraph) and also lets you drill down several levels:

1.  From each role assignment to the permission list under the role assignment

2.  From each permission to the resources it grants access to

![image-20260518-114949.png](images/image-20260518-114949.png)

Each row is a role assignment. Every role assignment has a **Role category**, **Role type**, and **Assignment type** value**.** Only role assignments of the **Azure** category have the identity’s granted scope type, accessible services, accessible resources, and permission usage from the assignment.

Here are the permission table columns:

<details>
<summary>Click to view columns</summary>

<table>

<thead>
<tr class="header">
<th><p><strong>Column</strong></p></th>
<th><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Role name</strong></p></td>
<td><p>The name of the role that’s assigned to the identity</p></td>
</tr>
<tr class="even">
<td><p><strong>Role category</strong></p></td>
<td><p>The category of role that’s granted, where it’s assigned from (see <a href="https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2566357009/Permissions+tab+reference#RoleCategories">Role assignment categories</a>)</p></td>
</tr>
<tr class="odd">
<td><p><strong>Role type</strong></p></td>
<td><p>Whether it’s a <strong>Built-in</strong> or <strong>Custom</strong> role assignment</p></td>
</tr>
<tr class="even">
<td><p><strong>Assignment type</strong></p></td>
<td><p>Whether it’s a <strong>Direct</strong> or <strong>Inherited</strong> role assignment (see <a href="https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2566357009/Permissions+tab+reference#RoleAssignmentInheritance">Role assignment inheritance</a>)</p></td>
</tr>
<tr class="odd">
<td><p><strong>Accessible services</strong></p></td>
<td><p>The number of <a href="https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2566357009/Permissions+tab+reference#AccessibleResourceTypes-services">services (i.e., resource types)</a> that the role assignment grants the identity access to</p></td>
</tr>
<tr class="even">
<td><p><strong>Accessible resources</strong></p></td>
<td><p>The number of resources (i.e., instances) of the accessible services that the role assignment grants the identity access to</p></td>
</tr>
<tr class="odd">
<td><p><strong>Permission usage</strong></p></td>
<td><p>The total number and distribution of <a href="https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2566357009/Permissions+tab+reference#374cc95e-bc2c-46de-b165-5f66600334e1">used, unused, and undetermined permissions</a> granted to the identity by the role assignment across all the accessible services</p>
<p><em>Hover over the bar to see exact counts</em></p></td>
</tr>
<tr class="even">
<td><p><strong>Critical assets</strong></p></td>
<td><p>The number of entities, out of the total accessible resources, that XM CEM identifies as critical assets</p></td>
</tr>
<tr class="odd">
<td><p><strong>Scope type</strong></p></td>
<td><p>The scope type of the permission grant (see <a href="https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2566357009/Permissions+tab+reference#RoleAssignmentScopes">Role assignment scopes</a>)</p></td>
</tr>
<tr class="even">
<td><p><strong>Scope name</strong></p></td>
<td><p>The name of the scope of the permission grant (see <a href="https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2566357009/Permissions+tab+reference#RoleAssignmentScopes">Role assignment scopes</a>)</p></td>
</tr>
<tr class="odd">
<td><p><strong>Inherited from</strong></p></td>
<td><p>For <strong>Inherited</strong> role assignments, the name of the group that grants the identity the role (see <a href="https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2566357009/Permissions+tab+reference#RoleAssignmentInheritance">Role assignment inheritance</a>)</p>
<p><em>Click the name to view the group members.</em></p></td>
</tr>
<tr class="even">
<td><p><strong>PIM</strong></p></td>
<td><p>Whether it’s a PIM assignment (see <a href="https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2566357009/Permissions+tab+reference#PimRoleAssigments">PIM role assignments</a>)</p></td>
</tr>
<tr class="odd">
<td><p><strong>Role assignment ID</strong></p></td>
<td><p>A non-default column that shows the full unique identifier of the role assignment</p></td>
</tr>
</tbody>
</table>

</details>

#### Investigate a role assignment's permissions

To investigate an identity’s [permission table](https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2565832708#PermissionTable), click a role assignment row to drill into its underlying individual permissions.

- **Resource type**: Which kind of resources the permission can act on.

- **Resources**: How many resources of those types we detected.

- **Last used**: The last time the permission was used across all those detected resources. Usage on any single resource counts. This is empty if the **Undetermined usage** value is **True**.

- **Unused period**: The length of time since the permission was last used. This is empty if the **Last used** value is empty, and might also be empty if the **Last used** value is **Unused**.

- **Risky permission**: True means the permission is used in known lateral movement exposures.

- **Undetermined usage**: A non-default column that shows whether we could read usage data for that permission. If **True**, the permission is one for which usage data couldn’t be determined. See [Permission usage calculations](https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2566357009/Permissions+tab+reference#PermissionUsageCalculations) for more.

#### Investigate a permission’s resources

Click a permission to drill into its accessible resources.

![image-20260519-002055.png](images/image-20260519-002055.png)

The resource list shows the identity’s permission usage for each specific resource. Use it to find which resource caused the last use, and when. It also shows the **Deleted** column, which tells you whether the resource was deleted.

**Table insights**:

- Start by looking at high-scope assignments. They usually have the largest blast radius.

- Review PIM assignments and set activations to temporary when possible.

- Focus first on permissions marked Risky or unused.

- Use the resource-level view to verify if a permission is actually used and where.

### Remediation recommendations

Each role assignment in the [permission table](https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2565832708#PermissionTable) has a recommended remediation action that provides tailored, step-by-step instructions for reducing the identity's permissions to only what it needs. Use the recommended remediation to enforce the Principle of Least Privilege (PoLP) after you investigate an identity's permissions.

To see remediations, from either the [permission graph](https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2565832708#PermissionGraph) or [table](https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2565832708#PermissionTable), click **Show remediations** to open the identity’s remediation wizard.

![image-20260525-114310.png](images/image-20260525-114310.png)

There’s a remediation for each role assignment. Each role assignment displays labels for characteristics relevant to the remediation under the assignment name.

![image-20260526-115327.png](images/image-20260526-115327.png)

The possible labels are:

- **Direct assignment**: Simplest remediation, as you only remove permissions for the individual entity.

- **Inherited assignment**: You remediate the permissions for the entire group. The recommended remediation only removes permissions that no one in the group has used. With this label comes another two labels:

  - **Group-level remediation**: Reminder that the recommendation accounts for the permission usage of all the group members

  - **Group**: The group name and the number of members

See [here](https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2566357009/Permissions+tab+reference#RoleAssignmentInheritance) for more about role assignment inheritance.

Click the arrows to navigate through the different role assignments' remediations:

![image-20260525-114038.png](images/image-20260525-114038.png)

The wizard proposes context-aware actions, for example:

- Refining a custom role

- Creating a new custom role if a built-in role cannot be edited

- Adjusting group-based assignments to the minimal usage level of all the group members.

After you review the proposed changes, export the plan as a PDF: ![image-20260525-114132.png](images/image-20260525-114132.png)

For more information, see [How we determine recommendations](https://xmcyber.atlassian.net/wiki/spaces/XCD/pages/2566357009/Permissions+tab+reference#HowWeDetermineRecommendations).

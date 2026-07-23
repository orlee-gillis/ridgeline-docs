# Access tab reference

## Introduction

This page explains in depth the access data that we show and what it represents. We also explain how the platform visualization works and how we calculate some of the values. This page explains:

* [Access grant inheritance](#access-grant-inheritance)
* [Grant categories](#grant-categories)

    * [JIT grants](#jit-grants)

* [Access grant scopes](#access-grant-scopes)
* [Accessible resource types (services)](#accessible-resource-types-services)
* [Access usage calculations](#access-usage-calculations)
* [How we determine recommendations](#how-we-determine-recommendations)

### Access grant inheritance

There are two ways of granting integrations access: directly or via inheritance. **Direct** grants are when the integration itself is listed in the access grant. **Inherited** grants occur when a team the integration is a member of is listed in the access grant, and the integration only has the access as long as it’s a member of that team.

**Transitive team chains:** When a grant is inherited through nested teams, we show the team that has the grant directly assigned to it. We don’t show the intermediate nested teams, because remediation happens on the directly assigned team.

In the [grant graph]([CHILD URL: About the Access tab]), direct grants show the path directly from the integration to the access grant, whereas inherited grants show the Team membership node between them. Double-click the node to see all the team members.

In the [grant table]([CHILD URL: About the Access tab]), inheritance is shown for each access grant in the **Grant type** column. If the grant is **Inherited**, then you see the team name in the **Inherited from** column. Click the team name to open the team members drawer.

`[SCREENSHOT: the grant table showing the Grant type and Inherited from columns]`

### Access grant categories

The grant category indicates where the grant is assigned from. Unused Access shows three grant categories:

* **App-level**: Grants access or defines specific feature access within a single application.
* **Directory**: Grants administrative rights to manage the workspace directory itself. These can be [JIT grants](#jit-grants).
* **Platform:** Grants access to manage the workspace platform infrastructure.

Of these types, only **Platform** grants show full access usage information.

* In the [grant graph]([CHILD URL: About the Access tab]), only the **Platform** grants have the scope, and the access path shows accessible resource types, resources, and access usage.
* In the [grant table]([CHILD URL: About the Access tab]), the same is true, and also the access drill-down of grant > rights > resource usage is only for **Platform** grants.

#### JIT grants

JIT grants are a sub-category of access grants that provide Just-In-Time access rather than standing access. They differ from regular grants, as they are intended to provide short-lived access. We only show JIT grants that we detected as active. Your JIT grants, if they are configured as temporary, could be configured as follows:

* To mark an integration as eligible for a grant, dependent on the eligibility being approved. In this case, when eligibility is approved, the grant becomes active.
* To grant short, active access grants for a limited time window. In this case, the grant is only active during the defined time window.
* A combination of both, in which case both the approval and the time window conditions need to be met for the grant to be active.

**Best practice**: Ensure JIT grants use temporary activation where possible.

* In the [grant graph]([CHILD URL: About the Access tab]), the JIT icon appears when we detect an active JIT grant.

    `[SCREENSHOT: the JIT icon on a grant node in the grant graph]`

* In the [grant table]([CHILD URL: About the Access tab]), the **JIT** column is **True** when we detect an active JIT grant.

### Access grant scopes

Every access grant defines the scope over which its access applies. Generally, a higher scope covers more items, which means it has a larger reach if misused. So in most cases, the larger the scope type, the greater the ROI from remediating it. Each access grant’s remediation advice maintains the original scope, as changing it is highly likely to disrupt your systems and affect business continuity.

For **Platform** grants, the scope types are as follows, from largest to smallest: **Organization**, **Workspace group**, **Workspace**, **Project**, and **Resource**.

Both the **Grant Graph** and the **Table** show the **Scope type** and the **Scope name** (for grants in the **Platform** category only):

* In the [grant graph]([CHILD URL: About the Access tab]) the access grant node lists them as **<scope_type>:<scope_name>**. For example: **Workspace: Contoso-IT-Dev**
* In the [grant table]([CHILD URL: About the Access tab]), they’re listed in the **Scope type** and **Scope name** columns. For example, **Type**: Workspace, **Scope name**: Contoso-IT-Dev

### Accessible resource types (services)

We show the same accessible resource types (or accessible services) that we harvest in general for the Ridgeline platform.

**Note**: In the **Unused Access** report, we use **resource type** and **service** interchangeably. Each resource is defined under a resource namespace that corresponds to a service, so grouping resources by resource type also groups them by service.

* In the [grant graph]([CHILD URL: About the Access tab]), each resource type node represents an accessible service. Double-click the node to see all the accessible resource instances.
* In the [grant table]([CHILD URL: About the Access tab]), the **Accessible services** column shows the number of resource types each access grant grants access to.

### Access usage calculations

Access usage is calculated by correlating logs with access rights. Usage is determined by reading platform activity logs. These only audit control-plane actions, and not data-plane or read actions. For example, List actions aren’t audited.

A used action means that we saw a record in the activity log. Unused means that there are no records of usage within the defined window of time (default is 90 days), and it’s a type of access right that is audited in the activity logs. Undetermined means it’s an access right that isn’t audited in the activity logs. We assume that undetermined rights ARE used, and so the remediation advice will keep these rights in any suggested policy edits.

### How we determine recommendations

Based on historical usage data, our [remediations]([CHILD URL: About the Access tab]) recommend policies that include only the access the integration actually uses and remove unused access. Two principles guide every recommendation:

* **Scope is preserved.** Each remediation targets a specific access grant and does not reduce its scope.
* **Team membership is preserved.** If access is inherited through a team, we do not modify team membership, as doing so can disrupt other purposes that the team serves.

The remediation logic differs by grant category.

#### Platform grants

For **Platform** grants, we analyze access usage from activity logs and base recommendations on the role type and the grant type.

| **Factor** | **What we recommend** |
| --- | --- |
| **Built-in role** | We first check whether one or more lower-level built-in roles cover the integration's used access. If no suitable built-in alternative exists, then we suggest creating a custom role.   Some organizations prefer to avoid custom roles (because the platform limits the number of custom roles per organization), so we prioritize built-in alternatives when possible.   We include the number of updates required for the built-in roles so you can also evaluate how much effort the built-in strategy will require. We recommend up to 5 updates. In those cases, the more updates you implement, the more access you remove. |
| **Custom role** | We suggest an edited version of the existing custom role that removes unused access. |
| **Inherited grant** | For access grants inherited through a team, we consider the access usage of all team members - not just the integration you are investigating - when recommending the policy. This ensures that the recommendation does not remove access that other team members actively use. |

#### Directory grants

For **Directory** grants, activity logs are not available for right-level usage analysis. Instead, we evaluate the integration from a security posture perspective and weigh risk factors, such as whether it’s external or inactive.

#### App-level grants

For **App-level** grants, we provide general best-practice recommendations, such as reducing write access to read-only where appropriate.

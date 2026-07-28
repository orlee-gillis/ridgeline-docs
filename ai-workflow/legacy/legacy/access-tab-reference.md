# Access tab reference

## Introduction

This page explains in depth the access data that we show and what it represents. We also explain how the platform visualization works and how we calculate some of the values. This page explains:

* [Access grant inheritance][CHILD URL: this page - inheritance anchor]
* [Grant categories][CHILD URL: this page - categories anchor]

    * [JIT access grants][CHILD URL: this page - JIT anchor]

* [Access grant scopes][CHILD URL: this page - scopes anchor]
* [Accessible resource types (services)][CHILD URL: this page - accessible resource types anchor]
* [Access right usage calculations][CHILD URL: this page - usage calculations anchor]
* [How we determine recommendations][CHILD URL: this page - recommendations anchor]

### Access grant inheritance

There are two ways of granting integrations access rights: directly or via inheritance. **Direct** grants are when the integration itself is listed in the access grant. **Inherited** grants occur when a team the integration is a member of is listed in the access grant, and the integration only has the access rights as long as it’s a member of that team.

**Transitive team chains:** When a role is inherited through nested teams, we show the team that has the role directly assigned to it. We don’t show the intermediate nested teams, because remediation happens on the directly assigned team.

In the [grant graph][CHILD URL: About the Access tab - grant graph anchor], direct grants show the path directly from the integration to the access grant, whereas inherited grants show the Team membership node between them. Double-click the node to see all the team members.

In the [grant table][CHILD URL: About the Access tab - grant table anchor], inheritance is shown for each access grant in the **Assignment type** column. If the role is **Inherited**, then you see the team name in the **Inherited from** column. Click the team name to open the team members drawer.

`[SCREENSHOT: the grant table showing Assignment type and Inherited from columns]`

### Access grant categories

The access grant category indicates where the role is assigned from. For integrations, Unused Access shows three grant categories:

* **App-level**: Grants access rights or defines specific feature access within a single application.
* **Directory**: Grants administrative rights to manage the workspace directory itself. These can be [JIT access grants][CHILD URL: this page - JIT anchor].
* **Platform:** Grants access rights to manage workspace platform infrastructure.

Of these types, only **Platform** grants show full access right usage information.

* In the [grant graph][CHILD URL: About the Access tab - grant graph anchor], only the **Platform** access grants have the scope, and the access path shows accessible resource types, resources, and access right usage.
* In the [grant table][CHILD URL: About the Access tab - grant table anchor], the same is true, and also the access rights drill-down of grant > access rights > resource usage is only for **Platform** access grants.

#### JIT access grants

JIT grants are a sub-category of access grants that are managed from the workspace platform’s Just-In-Time access service. They differ from regular grants, as they are intended to provide Just-In-Time access. We only show JIT access grants that we detected as active. Your JIT access grants, if they are configured as temporary, could be configured as follows:

* To mark an integration as eligible for a role, dependent on the eligibility being approved. In this case, when eligibility is approved, the role becomes active.
* To grant short, active access grants for a limited time window. In this case, the grant is only active during the defined time window.
* A combination of both, in which case both the approval and the time window conditions need to be met for the grant to be active.

**Best practice**: Ensure JIT grants use temporary activation where possible.

* In the [grant graph][CHILD URL: About the Access tab - grant graph anchor], the JIT icon appears when we detect an active JIT grant.

    `[SCREENSHOT: the JIT icon on an access grant node]`
* In the [grant table][CHILD URL: About the Access tab - grant table anchor], the **JIT** column is **True** when we detect an active JIT grant.

### Access grant scopes

Every access grant defines the scope over which its access rights are applied. Generally, a higher scope covers more items, which means it has a larger reach if misused. So in most cases, the larger the scope type, the greater the ROI from remediating it. Each access grant’s remediation advice maintains the original scope, as changing it is highly likely to disrupt your systems and affect business continuity.

For **Platform** access grants, the scope types are as follows, from largest to smallest: **Organization**, **Workspace group**, **Workspace**, **Project**, and **Resource**.

Both the **Grant Graph** and the **Table** show the **Scope type** and the **Scope name** (for grants in the **Platform** category only):

* In the [grant graph][CHILD URL: About the Access tab - grant graph anchor] the access grant node lists them as **<scope_type>:<scope_name>**. For example: **Workspace: Contoso-IT-Dev**
* In the [grant table][CHILD URL: About the Access tab - grant table anchor], they’re listed in the **Scope type** and **Scope name** columns. For example, **Type**: Workspace, **Scope name**: Contoso-IT-Dev

### Accessible resource types (services)

We show the same accessible resource types (or accessible services) that we harvest in general for the Ridgeline platform.

**Note**: In the **Unused Access** report, we use **resource type** and **service** interchangeably. In the workspace platform, each resource is defined under a resource provider namespace that corresponds to a service, so grouping resources by resource type also groups them by service.

* In the [grant graph][CHILD URL: About the Access tab - grant graph anchor], each resource type node represents an accessible service. Double-click the node to see all the accessible resource instances.
* In the [grant table][CHILD URL: About the Access tab - grant table anchor], the **Accessible services** column shows the number of resource types each access grant grants access to.

### Access right usage calculations

Access right usage is calculated by correlating logs with access rights. Access right usage is determined by reading activity logs. These only audit control-plane actions, and not data-plane or read actions. For example, List actions aren’t audited.

A used action means that we saw a record in the activity log. Unused means that there are no records of usage within the defined window of time (default is 90 days), and it’s a type of access right that is audited in the activity logs. Undetermined means it’s an access right that isn’t audited in the activity logs. We assume that undetermined access rights ARE used, and so the remediation advice will keep these access rights in any suggested policy edits.

### How we determine recommendations

Based on historical usage data, our [remediations][CHILD URL: About the Access tab - remediation recommendations anchor] recommend policies that include only the access rights the integration actually uses and remove unused ones. Two principles guide every recommendation:

* **Scope is preserved.** Each remediation targets a specific access grant and does not reduce its scope.
* **Team membership is preserved.** If access rights are inherited through a team, we do not modify team membership, as doing so can disrupt other purposes that the team serves.

The remediation logic differs by access grant category.

#### Platform access grants

For **Platform** access grants, we analyze access right usage from activity logs and base recommendations on the role type and the assignment type.

| **Factor** | **What we recommend** |
| --- | --- |
| **Built-in role** | We first check whether one or more lower-level built-in roles cover the integration's used access rights. If no suitable built-in alternative exists, then we suggest creating a custom role.<br />Some organizations prefer to avoid custom roles (because the workspace platform limits the number of custom roles per organization), so we prioritize built-in alternatives when possible.<br />We include the number of updates required for the built-in roles so you can also evaluate how much effort the built-in strategy will require. We recommend up to 5 updates. In those cases, the more updates you implement, the more access rights you remove. |
| **Custom role** | We suggest an edited version of the existing custom role that removes unused access rights. |
| **Inherited grant** | For access grants inherited through a team, we consider the access right usage of all team members - not just the integration you are investigating - when recommending the policy. This ensures that the recommendation does not remove access rights that other team members actively use. |

#### Directory access grants

For **Directory** access grants, activity logs are not available for access-right-level usage analysis. Instead, we evaluate the integration from a security posture perspective and weigh risk factors, such as whether it’s external or inactive.

#### App-level access grants

For **App-level** access grants, we provide general best-practice recommendations, such as reducing write access rights to read-only where appropriate.

# Unused Access

## Introduction

Unused Access is where you focus on removing unused access grants and enforcing least privilege for integrations across your environment. Unused Access maps who can do what, where they can do it, and how they have the access to do it. It then prioritizes what to fix based on risk and usage. Use Unused Access to enforce least privilege, reduce reach, and clarify roles for security and platform operations teams. Remove granted-but-unused integration entitlements without affecting business continuity. By default, we consider an access right that wasn’t used for 90 days to be **Unused**.

The report provides a unified view across multiple workspace platforms.

Unused Access doesn’t require any special permissions - it uses the same permissions that were already required for connecting your integrations.

## Unused Access report

The **Unused Access** report shows a prioritized list of integrations that have excessive access. You can find the report by selecting **Access Center** > **Exposures** > **Unused Access** from the menu:

`[SCREENSHOT: the Access Center menu with Exposures expanded and Unused Access selected]`

Here is what the report looks like:

`[SCREENSHOT: the full Unused Access report - summary dashboard on top, integration table below]`

At the top is the [report summary][CHILD URL: Unused Access - report summary anchor], followed by the [integration table][CHILD URL: Unused Access - integration table anchor], explained below.

### Report summary

The Unused Access report, in Access Center > Exposures > Unused Access, shows a prioritized list of integrations with unused access rights. The report dashboard shows the following sections:

* **Report scope**: Which workspace platform the integrations are located in. How many of each account type, such as organizations and workspaces, are actively being monitored by the Unused Access service (the accounts we harvest from).
* **Integration count**: How many integrations are in the report, and how many of them are highly privileged.
* **Service account count**: How many non-human integrations are in the report, which includes service accounts (both workspace-assigned and system-assigned), and how many of them are highly privileged.
* **Team count**: How many teams are in the report, and how many of them are highly privileged.

We classify an integration as **Highly privileged** based on specific roles for each workspace platform. For more, see the **Highly privileged** label description in [Integration labels reference][CHILD URL: Integration labels reference].

### Integration table

The report’s integration table shows your integrations, sorted by [Reach score][CHILD URL: Scores in Ridgeline] and then by unused access rights. Use the table to review the prioritized list to decide which integration to analyze first. Use filters to focus on integration types (for example, service accounts) or privileged accounts. Consider both Reach score and Unused Access columns (accessed resources vs. total unused access rights).

These are the default columns for the integration table:

| **Column** | **Description** |
| --- | --- |
| **Integration name** | The name of the integration |
| **Integration type** | The type of the integration (for example, service account) |
| **Highly privileged** | Whether the integration is highly privileged |
| **Reach score** | The Reach score of the integration |
| **Accessible services** | How many services the integration has access rights to access |
| **Accessible resources** | How many resources within the accessible services the integration has access rights to access |
| **Access right usage** | For the Platform access grant category, how many of the individual access rights that the integration has been granted are either **Used**, **Unused**, or **Undetermined**, based on activity logs (see more [here][CHILD URL: Access tab reference - usage calculations anchor]) |
| **Critical resources** | How many critical resources the integration can access from all resources - either directly or indirectly |

Use the integration table to prioritize which integrations to analyze. You can:

* Search for an integration.
* Add non-default columns by clicking the (Configure columns) button.
* Filter specific table columns to narrow down results based on the values in that column.
  For example, you can filter the **Integration type** column to display only **Service account** integrations.
* Export the data:

    * Export a CSV file of all the data
    * Filter the report and export only the filtered data

After prioritization, you analyze each integration by clicking its name to open the [Access tab][CHILD URL: Access tab] in its integration card. From there, you choose which access grant to remediate.

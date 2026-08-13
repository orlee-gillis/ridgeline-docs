cat > docs/test-eval-case-1.md << 'EOF'
---
template: parent-report
---

# Unused Access

## Introduction

Unused Access identifies access grants held by integrations that are not actively being used, based on activity log analysis. As teams manage multiple integrations across different platforms, excessive permissions accumulate — granting access that is never exercised and creating unnecessary security risk.

Unused Access helps security teams discover which integrations hold access they don't need, and provides a clear remediation path to narrow those permissions to only what is actively used. This follows the principle of least privilege: integrations should hold only the access required for their specific function.

This hub introduces the Unused Access feature and guides you through its surfaces and investigation workflows.

## Requirements

- **Role:** [VERIFY: minimum role required to view Unused Access reports]
- **Platform support:** on-prem and [CHILD URL: cloud platform name]
- **Feature availability:** [VERIFY: which versions/tiers include this feature]

## Explore Unused Access

The Unused Access feature includes:

- **Unused Access Report** — A summary view in the Access Center showing integrations with unused grants, ranked by risk
- **Access Tab** — The investigation surface on an integration card, displaying the grant graph and grant table with usage classification
- **Remediation Engine** — Step-by-step guidance for narrowing grants to actively used access, preserving scope and team membership

## Next Steps

- [CHILD URL: About the Unused Access Report] — Learn what the report shows and how to interpret it
- [CHILD URL: Understanding Access Grants] — Understand the concepts: Direct vs. Inherited, Platform/Directory/App-level categories, JIT grants
- [CHILD URL: How to Remediate Unused Access] — Follow the step-by-step process for narrowing permissions

## See Also

- [CHILD URL: Least Privilege Overview] — The broader principle behind access remediation
- [CHILD URL: Access Center] — The hub for all access-related features
- [CHILD URL: Glossary] — Terminology reference for all Unused Access concepts

---

## Open items for SME review

- [VERIFY: minimum role required to view Unused Access reports]
- [VERIFY: which versions/tiers include this feature]
- [CHILD URL: cloud platform name] — confirm the correct name for the cloud platform
- Confirm child report page titles and links are correct
- Confirm secondary "See also" links exist and are correct

EOF

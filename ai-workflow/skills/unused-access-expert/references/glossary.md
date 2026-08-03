# Ridgeline glossary

The terminology authority for Ridgeline documentation, in a Definition / Use in copy / Avoid
pattern. One term, one meaning, enforced everywhere. The upstream copy lives at `glossary.md` in
the repo root; this bundled copy travels with the skill so the skill is self-contained.

Ridgeline's domain is **connected integrations in a workspace platform**. The "Avoid" notes below
target the confusions a Ridgeline writer actually makes: using a container term for an atom, reusing
a word that already names a scope level, or borrowing vocabulary from a neighbouring domain that
makes the page ambiguous about what it is describing.

---

## access grant

**Definition:** The assignment that confers access on an integration - a role or policy attached to
the integration, directly or inherited through a team, at a defined scope. The container: one grant
bundles many access rights. Remediation operates on grants.

**Use in copy:** "access grant" on first use in a section, "grant" thereafter. "The integration has
14 grants." "Each grant defines the scope over which its access applies."

**Avoid:** "entitlement" (see below); "permission" at this level - that is the atom, not the
container. Do not call a grant a "role": a grant attaches a role at a scope, and the two are counted
differently.

## access right

**Definition:** A single capability within a grant - the ability to perform one kind of action on
one kind of resource. The atom: usage (Used / Unused / Undetermined) is measured per right.

**Use in copy:** "access right" wherever the grant/right distinction is in play; "right" on close
repetition. Where no contrast with grants is needed, "access" as a mass noun often reads better:
"access that integrations were granted but never use."

**Avoid:** Using "rights" and "grants" interchangeably - they are different levels, and the feature
behaves differently at each. Avoid "permission" except in the fixed phrase "platform permissions."

## entitlement

**Definition:** Not used in Ridgeline copy. Decision on record: enterprise jargon that adds no
precision the grant/right pair does not already carry.

**Use in copy:** Never. Rewrite around it: "Unused Access - access that integrations were granted
but never use."

**Avoid:** The word itself, in any construction.

## integration

**Definition:** A connected third-party application or workload operating in the workspace platform,
and the subject of the Unused Access report. Umbrella term for all subject types, including service
accounts.

**Use in copy:** "integration"; "connected integration" is acceptable on first use for warmth.

**Avoid:** "user" - an integration is not a person, and the report contains no human accounts.
Avoid "app" as a standalone noun, because **App-level** already names a grant category.

## service account

**Definition:** A non-human integration credentialed to act autonomously. A sub-type of integration;
appears as an **Integration type** value in the report.

**Use in copy:** "service account" in prose; bold when citing the UI value: **Service account**.

**Avoid:** "bot," "robot account," or any synonym invented for variety. The report shows one value,
so the docs use one word.

## team

**Definition:** A named collection of integrations. Grants assigned to a team are inherited by its
members. Remediation never modifies team membership.

**Use in copy:** "team"; "Inherited from" a team; "team members drawer" for the UI surface.

**Avoid:** "group" - it collides with the **Workspace group** scope type.

## Reach score

**Definition:** Ridgeline's prioritization score for an integration, reflecting how much of the
environment the integration can affect. Primary sort of the Unused Access report, followed by unused
grant count.

**Use in copy:** "Reach score," capitalized as a named metric. Lowercase "reach" for the general
concept: "a larger reach if misused."

**Avoid:** Inventing additional scores, or implying Unused Access contributes to an integration's
total score - it does not. Do not use "impact," "severity," or "exposure" as loose synonyms for reach.

## Used / Unused / Undetermined

**Definition:** The usage classification of an access right, derived from activity-log correlation.
**Used** - a log record exists. **Unused** - auditable, but no record within the window (90 days by
default). **Undetermined** - not auditable in activity logs, and treated as used, so never removed by
remediation advice. That treatment is the feature's core safety guarantee.

**Use in copy:** Bold as UI values in tables and when naming the classification. The window is
always "by default, 90 days."

**Avoid:** Conflating Undetermined with Unused, or any phrasing implying an undetermined right might
be removed. This is the single most damaging error available in this feature's documentation.

## JIT grant

**Definition:** A grant providing Just-In-Time access rather than standing access. Only JIT grants
detected as active are shown. A sub-category under the Directory grant category.

**Use in copy:** "JIT grant," spelling out "Just-In-Time" on first mention.

**Avoid:** Describing a JIT grant as standing access, or implying that inactive JIT grants appear
in the report - only active ones do.

## grant categories: Platform / Directory / App-level

**Definition:** Where a grant comes from. **Platform** - manages the workspace platform
infrastructure; the only category with full usage information. **Directory** - administers the
workspace directory; evaluated by security posture, not logs. **App-level** - access within a single
application; receives best-practice recommendations.

**Use in copy:** Bold as labeled values. Keep the asymmetry explicit - only Platform grants show
scopes, accessible services, and usage data.

**Avoid:** Attributing usage data to Directory or App-level grants; treating the three categories as
interchangeable when only one of them carries usage information.

## scope types: Organization / Workspace group / Workspace / Project / Resource

**Definition:** The ladder over which a grant's access applies, largest to smallest. Remediation
always preserves the original scope.

**Use in copy:** Bold as labeled values. Node format is code: `<scope_type>: <scope_name>`.

**Avoid:** Describing any remediation as narrowing scope; writing "group" where **Workspace group**
is meant.

## platform permissions

**Definition:** The permissions Ridgeline itself holds in order to read an integration's grants and
activity logs. Deliberately distinct from **access rights**, which are what the feature measures.

**Use in copy:** "platform permissions," always as the full two-word phrase, and only about
Ridgeline's own access. Unused Access requires no additional platform permissions beyond those
granted at connection time.

**Avoid:** Shortening to "permissions" - the bare word invites confusion with access rights.

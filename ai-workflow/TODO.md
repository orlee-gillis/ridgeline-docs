# Repo-wide work

Items that affect more than one page. Page-level decisions live in `ai-workflow/decisions/`.

Nothing here blocks session 15, which is the human editing pass on one page.

Each item lists where the change is made and what artifact shows it was done. An item with no entry in the
evidence column is not finished, however done it feels.

## CI gates

| Item | When | Change made in | Evidence it works |
| --- | --- | --- | --- |
| Vale prohibited terms - fails on "auto-remediation" and "one-click". Legal requires that no copy imply a change is applied without a person confirming it | Module 4 | `styles/Ridgeline/Prohibited.yml` | The rule file, a deliberately failing run in the Actions log, and a line in the README's CI gates list |
| Vale terminology swaps - flags "role assignment" and "entitlement" and names the correct term. Both are on the glossary's "Avoid" list, and "role assignment" would break the fiction | Module 4 | `styles/Ridgeline/Terminology.yml` | Same three: rule file, failing run, README line |
| Glossary copies compared - runs `diff` on the two copies of `glossary.md`. Exit code 1 fails the step and blocks the merge | Any spare 10 minutes - independent of the roadmap | `.github/workflows/docs-ci.yml` | The workflow diff, and a failing run produced by changing one word in one copy on a branch, then reverting |

To demonstrate a gate, break it on a branch, capture the failing run, then revert. A check that has never
failed has not been shown to test anything. The failing run is the evidence, not the rule file.

## Skill and template gaps

| Item | When | Change made in | Evidence it was done |
| --- | --- | --- | --- |
| `audit-checklist.md` has no feature-overview genre. It covers report, investigation surface, hub, and reference pages. `ridgeline-doc-writer` routes to three templates, one of which is feature overview, so a page drafted from it has no genre standard to be audited against | Before the next audit - it is the reason the first audit could not report genre findings | `skills/ridgeline-doc-auditor/references/audit-checklist.md` | The diff adding the genre, and a re-run of the audit on `apply-a-remediation.md` reporting genre findings the first pass could not |
| No how-to template exists. Needed once Figma mockups supply UI steps | After the mockups exist, before the how-to is drafted | `skills/ridgeline-doc-writer/assets/templates/` and the routing list in its `SKILL.md` | The new template file, and the `SKILL.md` diff adding it to the genre list |
| "Who this is for" as a heading. "This" is ambiguous - the page or the feature - and it addresses the document rather than its subject. Removed on `apply-a-remediation.md` only | After session 15. Changing the template mid-edit would put the page and the template out of step | `skills/ridgeline-doc-writer/assets/templates/feature-overview.md` | The template diff, and diffs on every sibling page in `docs/` still using the old heading. A template change with no page changes means the family is now inconsistent |
| "Prerequisites" renamed "What you need" on one page, to pair with "What you can do" | With the heading decision above - one template commit, not two | Same template | Same: template diff and sibling page diffs |
| Skill folders should be self-checking - every path a `SKILL.md` cites should resolve. Two did not today: the auditor's checklist and two doc-writer templates | Module 4, with the other gates | `.github/workflows/docs-ci.yml` | The workflow diff, and a failing run produced by deleting a cited file on a branch |

## Page work

| Item | When | Change made in | Evidence it was done |
| --- | --- | --- | --- |
| Audit `about-the-access-tab.md` and the Unused Access report page. Both are in `docs/` with the wrong heading order | Next session after 15. Needs a fresh read and your own list first | `ai-workflow/audits/`, then `docs/` | One audit file per page, one issue per approved finding, and a fix-forward commit per page closing its issues. The before-and-after diff is the evidence; the current versions stay in history |
| Work out why the pipeline passed them. Three possibilities: the auditor was never run, it ran and missed the problem, or it caught it and the fix was dropped | During that audit, not separately | A diagnosis section in each audit file | The named cause, and whichever fix it points at - a workflow step, a skill edit, or nothing if an action item was simply dropped |
| Split `apply-a-remediation.md`. Error reference to `troubleshoot-applying-a-remediation.md`; the five-step sequence to a how-to once mockups exist. Deferred so session 15 produces a single-file diff | After session 15 merges. The how-to part waits for mockups | `docs/` | The new page files, and an entry in `decisions/UAX-2841.md` recording the split and why it came after session 15 rather than during it |
| Attribution. The legacy pages are fictionalized versions of documentation written by someone else - inherited structure and substance, my fictionalized text | Before anything else in `docs/` is published | `ai-workflow/legacy/README.md` | The README diff. Stated once at folder level, not per page |

## Terminology decisions

| Item | When | Change made in | Evidence it was done |
| --- | --- | --- | --- |
| "an apply" as a countable noun. Used throughout the draft, not in the glossary. Decide whether it is reader-facing vocabulary or internal shorthand. It is load-bearing in the failed apply / reversal pair | During session 15 - the term is used throughout the page being edited | Both copies of `glossary.md` | The glossary diff in both copies, caught by the glossary CI gate if only one is edited |
| **failed apply** and **reversal** - add both, defined against each other. They were named separately so neither reads as a variety of the other, which only holds if the glossary says so | During session 15, same reason | Both copies of `glossary.md` | The glossary diff, and the two terms used consistently in `docs/apply-a-remediation.md` |
| Role-based access control. The three access layers on the apply page are an RBAC model. Neither the full term nor "RBAC" is in the glossary, and `style-guide.md` prohibits inventing abbreviations | Not blocking. Decide when the RBAC framing is next needed on a page | Both copies of `glossary.md`, or a recorded decision not to adopt it | Either the glossary diff, or a line in this file saying it was rejected and why. A decision not to adopt a term is still a decision worth recording |

## Roadmap corrections

| Item | When | Change made in | Evidence it was done |
| --- | --- | --- | --- |
| Session 15 says "Notes, prompt, draft, final all land in `ai-workflow/`". The final belongs in `docs/` - `conventions.md` reserves `ai-workflow/drafts/` for AI first drafts | Before starting session 15 | `roadmap.md`, practice repo | The roadmap diff. Private repo, so this one is not portfolio evidence |
| Session 15 says "Commit draft and final separately so the diff is the editorial story". Two files at two paths produce two additions, not a diff. Name the method: branch, commit the draft at the `docs/` path, then the editing pass as a second commit, read the diff in the pull request | Before starting session 15 | `roadmap.md`, practice repo | The roadmap diff, and the session 15 pull request itself demonstrating the method |

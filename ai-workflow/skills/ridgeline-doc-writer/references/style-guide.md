# Ridgeline documentation style guide

Voice, grammar, and formatting rules for Ridgeline documentation, plus the Docusaurus-specific rules
and the publish-readiness checklist. Terminology is not covered here - `glossary.md` is the authority
for every named surface, metric, and concept.

**Contents:** Voice · Tense and person · Structure and headings · Formatting · Punctuation ·
Grammar · Lists and tables · Notes and warnings · Links · Docusaurus deltas · Release notes ·
Publish-readiness checklist

---

## Voice

Write as a knowledgeable colleague: direct, specific, helpful. The reader is competent and busy.

- No hype, no marketing adjectives, no "powerful," "seamless," or "simply."
- No "please." An instruction is an instruction.
- No first-person singular. Use "we" for Ridgeline, "you" for the reader.
- Explain the why when a behavior looks surprising. A reader who understands a design decision stops
  filing it as a bug.

## Tense and person

- **Present tense** throughout. The report *sorts* by Reach score; it does not *will sort*.
- Second person for the reader's actions. "You can filter by grant category."
- Avoid "will" for system behavior entirely - it reads as a promise about the future.

## Structure and headings

- **Title case for headings.** Capitalize proper names (ridgeline-specific-terms) and named surfaces inside them.
- A heading named after a capitalized surface stays capitalized: "The Access tab."
- UI tab names are Title Case, including tabs inside a drawer.
- Never skip heading levels. Body headings start at `##` (the title lives in frontmatter).
- Put the key concept in the heading. "Configure columns," not "Configuration." Never "Details."
- Add a sub-heading roughly every 500 words. Short paragraphs; no walls of text.

## Formatting

- **Bold** for exact UI control labels only: **Configure columns**, **Service account**. Never bold
  for emphasis in prose, and never bold link text.
- `Inline code` for filenames, literal values, field formats, and paths.
- Spell out an acronym on first mention with the acronym in parentheses, then use the acronym.
  Reintroduce it inside a long self-contained section when that aids lookup.
- Do not invent abbreviations for names that do not have one. "Unused Access" is never shortened.

## Punctuation

- Oxford comma in lists.
- Straight quotes only. Curly quotes and typographic dashes pasted from other tools must be replaced.

## Grammar

- Pair every **if** with **then**. Use **whether** for uncertainty that is not conditional.
- Prefer **that** over **which** for restrictive clauses.
- Resolve ambiguous pronouns. In a paragraph about a grant and a team, "it" needs a noun.
- Keep parallel structure across list items and table cells.

## Lists and tables

- **Bulleted list** when one criterion organizes the items.
- **Table** when two or more criteria organize the rows. Bold the header row; sentence case headers.
- Keep punctuation consistent within a list or a column: either every item ends in a period or none
  does.
- Numbered lists only for ordered steps.

## Notes and warnings

- **Note** for supplementary information a reader can safely skip.
- **Important** for a risk of failure, confusion, or a messy outcome.
- **Warning** only for a genuinely destructive or irreversible outcome.

Never use a note to carry a fact the surrounding text needs. If it is load-bearing, it belongs in the
prose.

## Links

- Link the first mention of any feature, report, or concept that has its own page.
- Do not bold link text.
- Internal links are relative paths to the `.md` file. Same-page links use the auto-generated anchor:
  the heading lowercased with spaces replaced by hyphens.
- Use "following:" only when the referenced content comes immediately after. Otherwise "below."

## Docusaurus deltas

These override anything above that assumes a wiki-style editor.

- **The page title lives in frontmatter** as `title:`. Never write a `#` H1 in the body.
- **Sidebar order is `sidebar_position`** in frontmatter. Gaps are fine and are good practice - use
  10, 20, 30 so a page can be inserted later without renumbering the family.
- **Every page gets a deliberate `description:`** in frontmatter. It is what search engines and the
  site's own search surface, and a missing one silently falls back to the first sentence.
- **Notes become admonitions.** Note becomes `:::note`, Important becomes `:::important`, Warning
  becomes `:::warning`. Close every admonition with `:::`.
- **MDX strictness: bare angle brackets can break the build.** Wrap patterns like `<scope_name>` in
  backticks. This is the single most common build failure in prose.
- **Commands the reader runs** go in fenced blocks with a language identifier. Inline code is for
  values and filenames inside a sentence.
- Frontmatter template:

```yaml
---
title: About the Unused Access report
description: What the Unused Access report includes, how it sorts, and what to do with a finding.
sidebar_position: 20
---
```

## Publish-readiness checklist

Run this against the draft before handing it over. Every unchecked item goes in
`## Open items for SME review`.

**Frontmatter and placement**

- [ ] `title`, `description`, and `sidebar_position` all present and deliberate
- [ ] No `#` H1 in the body; heading levels do not skip
- [ ] The page's place in the sidebar is stated, and its neighbours are named

**Terminology**

- [ ] Every named surface, metric, and concept checked against `glossary.md`
- [ ] No term on any "Avoid" list appears anywhere
- [ ] "Unused Access" is unabbreviated throughout
- [ ] Access grant and access right are used at the correct level, never interchangeably

**Facts**

- [ ] Every claim about product behavior is traceable to the knowledge base, the glossary, or the
      conversation
- [ ] Undetermined is never presented as a kind of unused, and no sentence leaves open that an
      undetermined right might be removed
- [ ] No remediation is described as narrowing scope or changing team membership
- [ ] The 90-day window is written as a default
- [ ] Usage data is attributed only to Platform grants
- [ ] Content from an unshipped feature note is marked `[UNRELEASED]`

**Style**

- [ ] Present tense; no "will" for system behavior
- [ ] Bold used only for exact UI labels; no bolded link text
- [ ] Spaced hyphens, Oxford commas, straight quotes
- [ ] Every **if** has a **then**
- [ ] Lists and tables chosen by the one-criterion / multi-criterion rule

**Build safety**

- [ ] All angle-bracket patterns wrapped in backticks
- [ ] All internal links are relative `.md` paths; anchors match their headings
- [ ] Every admonition is closed

**Open items**

- [ ] Every `[SCREENSHOT: ...]`, `[CHILD URL: ...]`, `[VERIFY: ...]`, and `[UNRELEASED]` is collected
      in the open-items section
- [ ] No template comment blocks remain

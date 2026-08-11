---
title: Design system
description: The colours, type, spacing, and writing rules this documentation site is built on.
sidebar_position: 110
---

This page records the visual and editorial system behind the site: the colours, the type scale, the
spacing unit, and the writing rules every page follows. It exists so a new page can be made to match
the existing ones without guesswork.

The site runs the Docusaurus classic theme with a single visual override, the primary colour ramp in
`src/css/custom.css`. Everything else is the theme's default, which is a deliberate choice: the
writing carries the page, not the styling.

## Colours

One brand hue is used, for links, active navigation, and the current breadcrumb.

<div style={{display:'grid',gridTemplateColumns:'repeat(7,1fr)',height:'72px',fontSize:'11px',margin:'0 0 1.25rem'}}>
  <div style={{background:'#3a26c9',color:'#fff',display:'flex',alignItems:'flex-end',padding:'8px'}}>#3a26c9</div>
  <div style={{background:'#503ee0',color:'#fff',display:'flex',alignItems:'flex-end',padding:'8px'}}>#503ee0</div>
  <div style={{background:'#5a48e2',color:'#fff',display:'flex',alignItems:'flex-end',padding:'8px'}}>#5a48e2</div>
  <div style={{background:'#6d5ce6',color:'#fff',display:'flex',alignItems:'flex-end',padding:'8px'}}>#6d5ce6</div>
  <div style={{background:'#8070ea',color:'#fff',display:'flex',alignItems:'flex-end',padding:'8px'}}>#8070ea</div>
  <div style={{background:'#8a7aec',color:'#fff',display:'flex',alignItems:'flex-end',padding:'8px'}}>#8a7aec</div>
  <div style={{background:'#a99df1',color:'#fff',display:'flex',alignItems:'flex-end',padding:'8px'}}>#a99df1</div>
</div>

| Token | Value | Where it appears |
| --- | --- | --- |
| `--ifm-color-primary` | `#6d5ce6` | Links, active sidebar row, current breadcrumb |
| `--ifm-color-primary-darkest` | `#3a26c9` | Dark-mode contrast pairings |
| `--ifm-color-primary-lightest` | `#a99df1` | Tints and hover fills |

Everything else is the theme's neutral ramp, from `#f5f6f7` to `#1c1e21` on a white page. Semantic
colour appears only inside admonitions: green `#00a400`, blue `#54c7ec`, amber `#ffba00`, and red
`#fa383e`. There are no gradients and no second brand colour.

## Type

No webfont is loaded. The site uses the system font stack, so a page renders in the reader's own
interface font.

| Element | Size | Weight |
| --- | --- | --- |
| Page title | 3rem | 700 |
| Section heading | 2rem | 700 |
| Sub-heading | 1.5rem | 700 |
| Body | 1rem at 1.65 line-height | 400 |
| Sidebar link | 0.9375rem | 400 |
| Table of contents | 0.8rem | 400 |

## Spacing

A 1rem base unit, with 1.25rem between block elements. Every paragraph, table, list, and admonition
is separated by that one value, and headings take 2rem above. Table cells are 0.75rem.

## Admonitions

Which one to use is a rule, not a preference.

| Type | Use it for |
| --- | --- |
| **Note** | Supplementary information a reader can safely skip |
| **Important** | A risk of failure, confusion, or a messy outcome |
| **Warning** | Only a genuinely destructive or irreversible outcome |

:::note
Never use an admonition to carry a fact the surrounding text needs. If it is load-bearing, then it
belongs in the prose.
:::

## Writing rules

The full guide lives in
[`ai-workflow/skills/ridgeline-doc-writer/references/style-guide.md`](https://github.com/orlee-gillis/ridgeline-docs/blob/main/ai-workflow/skills/ridgeline-doc-writer/references/style-guide.md).
The rules that shape most sentences:

- **Voice.** A knowledgeable colleague, writing for a reader who is competent and busy. No hype, and
  never "powerful," "seamless," or "simply." No "please."
- **Person.** "You" for the reader, "we" for Ridgeline.
- **Tense.** Present, always. The report *sorts* by Reach score; it does not *will sort*.
- **Headings.** Sentence case, with named surfaces staying capitalized inside them.
- **Bold.** Exact UI labels only, such as **Configure columns**. Never for emphasis, never on link
  text.
- **Punctuation.** Oxford commas, straight quotes, and a spaced hyphen in place of any dash.
- **Grammar.** Every **if** is paired with a **then**.
- **Honesty.** Unconfirmed claims stay in the page as `[VERIFY: ...]` and are collected into an
  `## Open items for SME review` section at the foot.

Emoji are not used anywhere, in the interface or the copy.

## Related

- [What changed, and why](what-changed.md)
- [Pipeline and AI terms](pipeline-and-ai-terms.md)

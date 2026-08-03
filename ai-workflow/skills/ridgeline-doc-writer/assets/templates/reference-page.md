---
title: <Surface name> reference
description: Reference tables for every field, value, and state on the <Surface name>.
sidebar_position: <10 / 20 / 30 ...>
---

<!-- REFERENCE PAGE TEMPLATE
     Purpose: lookup, not reading. A reader arrives here from search or from a link, wanting one
     value's meaning, and leaves as soon as they have it.
     Design rules for this genre:
       - Tables carry the content. Prose exists only to say what a table covers.
       - Completeness is the whole promise. A partial table reads as exhaustive and quietly misleads,
         so any set you could not complete gets a [VERIFY:] flag saying it is incomplete.
       - One heading per field or field group, named for the field, so the anchor and the site search
         both land on the right row.
     Delete every comment block before handing over the draft. -->

<One or two sentences: which surface this documents and what a reader can look up here. Link to the
conceptual page for readers who arrived needing explanation rather than lookup.>

## <Field or group name>

<One sentence on what the field is, if the name does not fully carry it.>

| Value | Meaning |
| --- | --- |
| **<Value>** | |
| **<Value>** | |

<!-- Bold each value exactly as the UI renders it. Where a classification carries a behavioral
     consequence - a state that changes what the product does - put the consequence in the Meaning
     cell rather than in a note below the table. A reader scanning one row will not read the note. -->

## <Field or group name>

<Where values differ in what data backs them, add the asymmetry as a column rather than a caveat.
An asymmetry hidden in prose under a table is an asymmetry readers will miss:>

| Value | What it governs | Data available | Consequence |
| --- | --- | --- | --- |
| **<Value>** | | | |

## <Format or notation>

<Any literal format a reader has to recognize or reproduce. Use inline code, and wrap angle-bracket
patterns in backticks so the build does not break:>

- `<placeholder_type>: <placeholder_name>` - for example `Workspace: Contoso-IT-Dev`

## <Hierarchy or ladder>

<Ordered sets get a numbered list with the ordering criterion stated, largest to smallest or
first to last:>

1. **<Level>** - <scope of the level>
2. **<Level>** - <scope of the level>

:::note
<Only for genuinely supplementary lookup aids. Never put a value's meaning here.>
:::

## Related

- [<Conceptual page for this surface>](<relative-path>.md)
- [<Report page>](<relative-path>.md)

## Open items for SME review

<!-- Any table you could not complete belongs here, named explicitly as incomplete. -->

- [ ] `[VERIFY: complete value set for <field> - table below may be partial]`

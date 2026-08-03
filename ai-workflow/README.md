
The working files behind the pages in `docs/`. Nothing here is published to the site - it is the
record of how each page came to exist.

Read in this order:

| Folder | What it holds |
|---|---|
| `legacy/` | Documentation as it was before this project. Deliberately unedited - it is the "before" |
| `inputs/` | What arrives from the product team. Jira stories, feature notes. Raw, not cleaned up |
| `review/` | What I found in an input before writing anything. Written and committed before the draft exists |
| `drafts/` | The AI first draft, with every unverified claim flagged |

The finished page ships to `docs/`. Draft and final are committed separately, so the difference
between them is visible in the history rather than described.

## Why the order matters

The review is committed before the draft. That means the sequence - read the input, find its gaps,
then write - is checkable in the commit history instead of being something I assert.

Same reason `legacy/` is never edited. It is the comparison point for the improved pages, and
tidying it would remove the evidence.

## Conventions

| Marker | Meaning |
|---|---|
| `[VERIFY: ...]` | A claim no source confirms. Resolved with a subject-matter expert, never guessed |
| `[SCREENSHOT: ...]` | An image the page needs, described rather than faked |
| `[UNRELEASED]` | Drawn from an input describing behaviour not yet available to customers |

Every open marker is collected at the end of the file it appears in, so nothing unresolved is left
buried mid-page.

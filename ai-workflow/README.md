# ai-workflow

Artifacts of the AI-assisted authoring pipeline, preserved so the editorial story is visible in the repo history.

| Folder | Contents |
|---|---|
| `legacy/` | Stage 1 legacy articles and their audit report (do not edit - the improved versions live in `docs/`) |
| `inputs/` | Feature notes (the PM register) |
| `prompts/` | Versioned prompt templates for drafting and style review |
| `drafts/` | AI first drafts with `[VERIFY: ...]` flags, committed unedited |
| `scripts/` | The CI AI reviewer |

Drafts and finals are committed separately so the diff between them is the visible editorial work.

---
title: Pipeline and AI terms
description: The terms used across this repository, each with a definition and how it manifests technically - files, mechanisms, and where to look.
---

This site is written and published through a docs-as-code pipeline with AI assistance at the drafting
stage. Both halves bring vocabulary that is easy to use loosely, so this page fixes what each term
means here.

Every entry has two parts: what the term means, and how it shows up in practice - the file that holds
it, the mechanism that enforces it, or where to look to see it working. The second part is the more
useful half. "Skill" is a familiar word; a directory containing a `SKILL.md` with capped frontmatter
is a thing you can inspect.

## How models read input

**Context window.** Everything the model can see at once - system prompt, skills, files, the
conversation, and the current message. Measured in tokens.

*Technically:* a fixed integer limit per model. Every request sends the whole window again; the model
holds no state between turns. Exceeding it truncates or errors.

**Token.** The unit a model reads in. Roughly three quarters of a word in English.

*Technically:* text is split by a tokenizer before the model sees it. Billing, rate limits, and
context limits are all counted in tokens, not words.

**Context rot.** Accuracy falling as the context window fills.

*Technically:* measured by retrieval benchmarks - hide a fact in a long input and ask for it back.
Scores drop as input length rises, across models. It is the reason this project curates context
rather than loading everything available.

**Attention budget.** Informal name for the same limit.

*Technically:* not a setting or a number that can be read. It describes the effect of attention
spreading across more input.

## Instructions given to a model

**Prompt.** The instruction for one turn.

*Technically:* one message in the `messages` array sent to the API, with `role: "user"`.

**System prompt.** Standing instructions given before the user's message, usually not visible to the
reader.

*Technically:* a separate `system` parameter on the API request, not part of `messages`. Project
instructions and style settings are folded into it.

**Skill.** A folder of instructions and reference material, loaded only when its description matches
the request.

*Technically:* a directory containing `SKILL.md` with YAML frontmatter (`name`, `description`), an
optional body, and optional `references/` and `assets/` subfolders.

**Progressive disclosure.** Only a skill's description sits in context by default.

*Technically:* three levels. Frontmatter always loaded, roughly 30 to 50 tokens per skill. The body
loads when the skill fires. Reference files load only when the body points to them. This is why many
skills can be installed without a context penalty.

**Trigger description.** The sentences in a skill's frontmatter that decide whether it loads.

*Technically:* the `description` field, capped at 1,024 characters. The only text the model reads
before deciding, so nothing in the body affects whether the skill fires.

**Source hierarchy.** A statement inside a skill saying which source wins when sources conflict.

*Technically:* prose in the `SKILL.md` body. Nothing enforces it - the model reads it and complies or
does not, which is why it is worth testing rather than assuming.

## Tools, agents, and MCP

**Tool.** Something a model can do rather than know - read a file, run a command, call an API.

*Technically:* a JSON schema declaring a name, a description, and typed parameters. The model emits a
tool-use block; the client runs the code and returns the result.

**Agent.** A model running in a loop: decide, act, read the result, decide again.

*Technically:* a program that calls the API, executes any tool the response requests, appends the
result to `messages`, and calls again until the model stops requesting tools.

**Subagent.** A separate agent instance given part of a task, with its own context window.

*Technically:* the parent agent calls a tool that starts a fresh conversation with its own system
prompt and window, then receives only that conversation's final output.

**MCP, or Model Context Protocol.** The standard for connecting a model to external tools and data.

*Technically:* a JSON-RPC protocol over stdio or HTTP. A client asks a server what it offers through
`tools/list`, `resources/list`, and `prompts/list`, then calls `tools/call` to run one.

**MCP server.** A program that exposes tools, resources, and prompts over that protocol.

*Technically:* any process that speaks it. What a server reports can be captured as JSON and read
directly, which is the starting point for documenting one.

**Tool description.** The text a model reads to decide whether to call a tool.

*Technically:* the `description` field in the tool's JSON schema. Often generated from a docstring or
annotation in the server's source, so changing it may require a code change rather than a docs change.

**Connector.** A packaged MCP server that a product can switch on.

*Technically:* a stored server URL plus credentials. Enabling one injects all of its tool definitions
into the context window before the first message, so each active connector has a cost.

## Files that agents read

**`CLAUDE.md`.** Read by Claude Code when it opens a repository.

*Technically:* a markdown file at the repository root, loaded into every session automatically. A
plain link to another file is read on demand; an `@path` import inlines that file every turn.

**`AGENTS.md`.** The same purpose, read by coding agents other than Claude Code.

*Technically:* also a markdown file at the repository root. There is no shared schema - each tool
decides what to do with it. Maintaining both files fully means they drift, so the rules belong in one
with a pointer from the other.

**`llms.txt`.** A machine-readable map of a published site, for models reading it from outside.

*Technically:* a markdown file served at the site root, listing pages and their purpose. Unrelated to
the two files above, which govern an agent working inside the repository.

## Git, GitHub, and CI

**Docs as code.** Documentation kept in a repository, reviewed through pull requests, and published by
a build process.

*Technically:* markdown files in git, a static site generator, and continuous integration. Here:
Docusaurus building `docs/` and publishing to GitHub Pages.

**Branch.** A named line of work, and a snapshot of the files at that point.

*Technically:* a pointer to one commit. Checks run against what that commit contains, not against the
repository's newest state, so a branch created before a fix keeps failing on the thing the fix
corrected.

**Pull request.** A request to merge a branch, with a diff to review and checks to pass.

*Technically:* a GitHub object linking two branches. Opening one, or pushing to it, triggers any
workflow with an `on: pull_request` trigger.

**GitHub Actions.** GitHub's automation service.

*Technically:* reads YAML from `.github/workflows/`, provisions a temporary virtual machine per job,
runs the steps, and reports each job back as a named check on the pull request.

**Workflow.** A YAML file saying what runs and when.

*Technically:* a file in `.github/workflows/`, with `on:` for the trigger and `jobs:` for the work.

**Job.** One unit inside a workflow.

*Technically:* a key under `jobs:` with its own `runs-on` and `steps`. Jobs run in parallel unless
told otherwise.

**Action.** A reusable step published by someone else.

*Technically:* referenced as `uses: owner/repo@version` inside a step.

**Actions secret.** An encrypted value a workflow can read.

*Technically:* stored under Settings, then Secrets and variables, then Actions. Read in a workflow as
`${{ secrets.NAME }}`. A separate list from Codespaces secrets, which are injected as environment
variables into a development container instead.

**Ruleset.** The repository setting that makes named checks required.

*Technically:* configured under Settings, then Rules. Needs enforcement set to active, a target
branch, and each check named exactly as its job's `name` field. Without it a failed check appears on
the pull request but the merge still goes through.

**Gate.** A required check.

*Technically:* no separate mechanism - a check becomes a gate when a ruleset lists it. A style guide
states a rule; a gate prevents a merge that breaks it.

## Linters and checkers

**Vale.** A prose linter.

*Technically:* reads `.vale.ini` for `StylesPath` and `BasedOnStyles`, loads YAML rule files, and
prints the file, line, and rule for each violation. Every rule file needs an `extends` key naming its
type, or Vale refuses to load and exits without checking anything.

**Rule scope.** Which files a linter runs on.

*Technically:* set per tool - `files` for the Vale action, `globs` and `ignores` for markdownlint, path
arguments for a link checker. Scope decides whether a gate is usable: pointed at deliberately
unpolished archive files, no pull request would ever pass.

**markdownlint.** Checks markdown structure, including heading spacing, blank lines, and list
formatting.

*Technically:* configured by `.markdownlint-cli2.jsonc`. Rules are numbered from `MD001` upward, and
setting one to `false` disables it. A CI action and a local install can be different versions, which
enforce different rule sets against the same file.

**Link checker.** Reports links pointing at things that do not exist.

*Technically:* here, lychee run through a GitHub action. Needs a root directory pointing at `static/`
or root-relative image paths are reported as broken, and an offline flag to skip external URLs, which
fail for reasons a repository cannot fix.

## Conventions used in this repository

**`[VERIFY: ...]`.** A claim no source confirms.

*Technically:* plain text in a markdown file, collected into an open-items section at the end of the
page. Nothing enforces it - a convention, not a check.

**`[UNRELEASED]`.** Content drawn from an input describing behaviour that is not yet available.

*Technically:* the same - a text marker, removed by hand once the release ships.

**Baseline.** A measurement taken before any change, so a later measurement can be compared against
it.

*Technically:* a recorded score plus frozen copies of the files being measured. Editing them before
recording the baseline destroys the comparison permanently, which is why the two skills under
measurement carry a freeze rule.

**Trigger score.** Out of a fixed set of test prompts, how many load the intended skill.

*Technically:* run by hand. Each prompt goes into a fresh conversation and the skill that fires is
recorded. No harness and no code.

## Adding a term

Add the entry to the section it belongs in, alphabetically is not required - grouping by section
matters more than ordering inside one. Give it a definition and a `*Technically:*` line. If the
technical line would only restate the definition, the term probably does not need an entry.

Leave a blank line between the definition and its technical line, or markdownlint will report the
heading spacing.
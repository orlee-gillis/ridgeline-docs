---
title: Ridgeline documentation
slug: /
sidebar_position: 10
description: Customer documentation for Ridgeline, published through a docs-as-code pipeline.
---

Welcome to the Ridgeline documentation site.

Ridgeline is a fictional security product. This site is a portfolio artifact: it demonstrates a complete docs-as-code pipeline - Markdown source in Git, pull-request review, CI quality gates, and automated deployment to GitHub Pages.

## How this site is built

Every page is a Markdown file in the `docs/` folder of the [ridgeline-docs repository](https://github.com/YOUR-GITHUB-USERNAME/ridgeline-docs). Changes ship through pull requests. CI builds the site on every pull request and blocks merges that would break it. Merging to `main` deploys the site automatically.

## What's coming

Documentation for the Ridgeline Unused Access feature, produced through an AI-assisted authoring workflow with human editorial control. The `ai-workflow/` folder in the repository preserves the editorial story: feature inputs, prompt templates, flagged AI drafts, and finished pages, committed separately so the diffs show the writer's judgment at work.

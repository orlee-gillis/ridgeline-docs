# Module 3 - decisions

## Model choice for the advisory PR reviewer

Claude Haiku 4.5, not Opus.

The reviewer runs on every pull request, so cost and latency matter in a way they do not when
drafting a page once. Its job is narrow - flag claims with no source, and pages that have drifted
from their purpose - which does not need the strongest model available.

The change is one line in `.github/scripts/review-docs.py` if it turns out to miss things a human
reviewer catches.

## Scope of the reviewer's prompt

The prompt tells the model what not to comment on: spelling, punctuation, banned terms, heading
spacing, and broken links. Vale, markdownlint, and the link checker already cover all of those, and a
comment repeating four checks is a comment nobody reads.
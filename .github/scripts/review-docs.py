#!/usr/bin/env python3
"""Advisory documentation review for a pull request.

Reads a diff of docs/ from stdin, asks a model to review it, and posts the result as a
pull request comment. Advisory only - the workflow that calls this never fails the build.

Deliberately does not check anything the deterministic gates already cover. Vale checks
banned terms and punctuation, markdownlint checks structure, lychee checks links, and the
Docusaurus build checks that the site compiles. Repeating those here would produce noise
and teach the reader to skim the comment.

Same principle applies to the three genre-specific gates (validate-parent-report.py,
validate-child-report.py, validate-workflow-methodology.py, all in this directory): a page
tagged `template: parent-report` / `child-report` / `workflow-methodology` already gets a
dedicated review against that genre's real requirements. Reviewing it again here too would
mean two separately-worded AI comments about the same underlying issue on the same file -
so files carrying one of those tags are stripped from the diff before this review runs.

Also incorporates the core checks from `ai-workflow/skills/stop-slop/SKILL.md` (AI writing
tells - filler phrases, passive voice, formulaic structures) rather than running that skill
as a second automated bot. One advisory voice, broader criteria, no duplicate comments. The
full skill (phrase lists, structure catalog, before/after examples) stays available as an
interactive pass for a deeper look than this summary check gives.
"""

import json
import os
import re
import sys
import urllib.request

MODEL = "claude-haiku-4-5-20251001"
MAX_DIFF_CHARS = 60000

# Genres already covered by their own dedicated gate - see the module docstring.
COVERED_TEMPLATE_VALUES = {"parent-report", "child-report", "workflow-methodology"}


def file_template(filepath: str):
    """Read a file's current `template:` frontmatter value, if any. Reads from the
    working tree (not the diff) since the diff for an unrelated line change won't show
    unchanged frontmatter."""
    try:
        with open(filepath, "r") as f:
            content = f.read()
    except OSError:
        return None

    match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not match:
        return None
    for line in match.group(1).split("\n"):
        if line.strip().startswith("template:"):
            return line.split(":", 1)[1].strip()
    return None


def strip_covered_files(diff: str) -> str:
    """Remove diff hunks for files whose current template: tag is already covered by a
    dedicated genre gate."""
    blocks = re.split(r"(?=^diff --git )", diff, flags=re.MULTILINE)
    kept = []
    for block in blocks:
        match = re.search(r"^diff --git a/(\S+) b/\S+", block, re.MULTILINE)
        if match and file_template(match.group(1)) in COVERED_TEMPLATE_VALUES:
            continue
        kept.append(block)
    return "".join(kept)

PROMPT = """You are reviewing a change to a documentation site. The site documents a cloud
security product called Ridgeline, and its pages are written for a security engineer who has
opened a report and needs to decide what to do next.

Review the diff below and comment only on things a human reviewer would raise. Be specific,
cite the file and the line, and keep the whole comment under 300 words.

Look for:

- A claim stated as fact that the diff gives no source for. The repository convention is to
  mark unverified claims `[VERIFY: what needs confirming]` rather than asserting them.
- A page that has stopped serving its stated purpose - for example a procedure that explains
  a screen instead of telling the reader what to do.
- A term used in more than one sense within the change, or a term introduced without
  explanation.
- A statement that contradicts something else in the diff.
- An instruction the reader could not act on, because it names no control, or no outcome.
- AI writing tells: throat-clearing openers, needless adverbs, passive voice, a vague
  declarative standing in for a specific claim ("the reasons are structural"), an inanimate
  thing performing a human action ("the decision emerges"), a "not X, it's Y" contrast doing
  the work a direct statement should, or an em dash. Flag the pattern and quote the sentence;
  do not rewrite it.

Do not comment on:

- Spelling, punctuation, capitalisation, banned words, or heading spacing. Automated checks
  already cover all of these, and repeating them wastes the reader's attention.
- Broken links or missing images. A link checker covers those.
- Style preferences. Say what is wrong, not what you would have written.

If the change is fine, say so in one sentence and stop. A short comment that says nothing is
wrong is more useful than a long one that pads.

Diff:

```diff
{diff}
```
"""


def call_api(diff: str) -> str:
    key = os.environ["ANTHROPIC_API_KEY"]
    body = json.dumps({
        "model": MODEL,
        "max_tokens": 1000,
        "messages": [{"role": "user", "content": PROMPT.replace("{diff}", diff)}],
    }).encode()

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=body,
        headers={
            "content-type": "application/json",
            "x-api-key": key,
            "anthropic-version": "2023-06-01",
        },
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.load(r)

    return "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")


def post_comment(text: str) -> None:
    token = os.environ["GITHUB_TOKEN"]
    repo = os.environ["GITHUB_REPOSITORY"]
    pr = os.environ["PR_NUMBER"]

    comment = (
        "## Advisory documentation review\n\n"
        f"{text}\n\n"
        "---\n\n"
        f"*Generated by `{MODEL}`. Advisory only - this check never blocks a merge, and "
        "disagreeing with it is a legitimate outcome. Style, structure, and links are "
        "checked by the deterministic gates instead. Pages tagged `template: parent-report` / "
        "`child-report` / `workflow-methodology` are reviewed by their own dedicated gate "
        "instead of here, to avoid two overlapping AI comments on the same file. Also checks "
        "for AI writing tells (see `ai-workflow/skills/stop-slop/SKILL.md`) - ask for that "
        "skill directly for a deeper pass than this summary check gives.*"
    )

    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}/issues/{pr}/comments",
        data=json.dumps({"body": comment}).encode(),
        headers={
            "authorization": f"Bearer {token}",
            "accept": "application/vnd.github+json",
            "content-type": "application/json",
        },
    )
    urllib.request.urlopen(req, timeout=60)


def main() -> int:
    diff = strip_covered_files(sys.stdin.read())

    if not diff.strip():
        print("No changes under docs/ outside the genre gates' scope. Nothing to review.")
        return 0

    if len(diff) > MAX_DIFF_CHARS:
        diff = diff[:MAX_DIFF_CHARS] + "\n\n[diff truncated]"

    try:
        review = call_api(diff)
    except Exception as e:
        print(f"Review call failed: {e}")
        return 0

    if not review.strip():
        print("Model returned nothing. Skipping comment.")
        return 0

    try:
        post_comment(review)
        print("Comment posted.")
    except Exception as e:
        print(f"Could not post comment: {e}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
"""Shared logic for the three genre-validation gates (parent-report, child-report,
workflow-methodology). Each gate is a thin wrapper calling run(genre) with its own
`template:` value - the genre name doubles as the audit-checklist.md section heading.

Two modes, selected by CLI args:
  python validate-<genre>.py                    CI mode - checks every docs/**/*.md file
                                                  tagged template: <genre>, exits non-zero
                                                  if any page scores a blocker.
  python validate-<genre>.py --test-file <path>  Local test mode - runs fixtures from a
                                                  JSON file, compares actual vs. expected
                                                  severity.
"""

import glob
import json
import os
import re
import sys

import urllib.request

MODEL = "claude-sonnet-5"
CHECKLIST_PATH = "ai-workflow/skills/ridgeline-doc-auditor/references/audit-checklist.md"


def response_schema(genre):
    return {
        "type": "object",
        "properties": {
            "purpose_summary": {
                "type": "string",
                "description": "One or two sentences: what this page is for, and whether it does that.",
            },
            "highest_severity": {"type": "string", "enum": ["none", "should-fix", "blocker"]},
            "findings": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "severity": {"type": "string", "enum": ["should-fix", "blocker"]},
                        "description": {"type": "string"},
                        "source": {
                            "type": "string",
                            "description": f"The checklist row this cites, e.g. 'audit-checklist.md, {genre}'",
                        },
                        "suggestion": {
                            "type": "string",
                            "description": "A concrete fix - specific text or section to add, not a restatement of the problem.",
                        },
                    },
                    "required": ["severity", "description", "source", "suggestion"],
                    "additionalProperties": False,
                },
            },
        },
        "required": ["purpose_summary", "highest_severity", "findings"],
        "additionalProperties": False,
    }


def parse_frontmatter(content):
    match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not match:
        return {}
    frontmatter = {}
    for line in match.group(1).split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            frontmatter[key.strip()] = value.strip()
    return frontmatter


def extract_checklist_section(checklist_text, heading):
    lines = checklist_text.split("\n")
    start = next((i for i, l in enumerate(lines) if l.strip() == f"## {heading}"), None)
    if start is None:
        raise ValueError(f'Could not find "## {heading}" in {CHECKLIST_PATH}')
    end = len(lines)
    for i in range(start + 1, len(lines)):
        if lines[i].startswith("## "):
            end = i
            break
    return "\n".join(lines[start:end]).strip()


def build_prompt(genre, page_content):
    with open(CHECKLIST_PATH, "r") as f:
        checklist_text = f.read()
    section = extract_checklist_section(checklist_text, genre)

    return f"""You are auditing a Ridgeline documentation page against the {genre} genre.

Below is the genre's required elements (from the project's audit checklist):

{section}

Audit the page below against these requirements. Only report a finding if you can cite the specific
checklist row it violates - if you cannot, do not report it. A missing required element is
"should-fix" unless the checklist row says otherwise (a missing safety/guarantee statement is
"blocker"). If the page satisfies every requirement, return an empty findings array and
highest_severity: "none".

Page content:

---
{page_content}
---"""


def call_claude(genre, prompt):
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY is not set.")

    body = json.dumps(
        {
            "model": MODEL,
            "max_tokens": 2000,
            "output_config": {
                "effort": "medium",
                "format": {"type": "json_schema", "schema": response_schema(genre)},
            },
            "messages": [{"role": "user", "content": prompt}],
        }
    ).encode()

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=body,
        headers={
            "content-type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.load(r)

    text_block = next((b for b in data.get("content", []) if b.get("type") == "text"), None)
    if text_block is None:
        raise RuntimeError("Claude response contained no text block.")
    return json.loads(text_block["text"])


def audit_page(genre, filepath):
    with open(filepath, "r") as f:
        content = f.read()
    return call_claude(genre, build_prompt(genre, content))


def run_ci(genre):
    files = glob.glob("docs/**/*.md", recursive=True)
    matched = []
    blocking = False

    for filepath in files:
        with open(filepath, "r") as f:
            content = f.read()
        frontmatter = parse_frontmatter(content)
        if frontmatter.get("template") != genre:
            continue

        matched.append(filepath)
        try:
            result = call_claude(genre, build_prompt(genre, content))
        except Exception as e:
            print(f"⚠️ {filepath}: check failed to run - {e}")
            continue

        if result["highest_severity"] == "none":
            print(f"✅ {filepath}: passes {genre} audit")
        else:
            if result["highest_severity"] == "blocker":
                blocking = True
            print(f"⚠️ {filepath}: {result['highest_severity']}")
            for finding in result["findings"]:
                print(f"   [{finding['severity']}] {finding['description']}")
                print(f"       source: {finding['source']}")
                print(f"       suggestion: {finding['suggestion']}")

    if not matched:
        print(f"ℹ️ No {genre} files found to validate")

    return 1 if blocking else 0


def run_test_file(genre, test_file_path):
    with open(test_file_path, "r") as f:
        suite = json.load(f)

    failures = 0
    for case in suite["testCases"]:
        print(f"{case['id']} ({case['name']})... ", end="")
        try:
            result = audit_page(genre, case["filepath"])
            expected = case["expectedSeverity"]
            # A list means "any of these are acceptable" - for cases where the correct
            # answer is a genuine judgment call the model won't make identically every
            # run (see workflow-methodology-test.json's real-page case for why this
            # exists), not a way to paper over an actually-wrong result.
            acceptable = expected if isinstance(expected, list) else [expected]
            actual = result["highest_severity"]
            if actual in acceptable:
                print(f"PASS (severity: {actual})")
            else:
                failures += 1
                print(f'FAIL - expected severity in {acceptable}, got "{actual}"')
                for finding in result["findings"]:
                    print(f"    [{finding['severity']}] {finding['description']} - {finding['source']}")
                    print(f"        suggestion: {finding['suggestion']}")
        except Exception as e:
            failures += 1
            print(f"ERROR - {e}")

    total = len(suite["testCases"])
    print(f"\n{total - failures}/{total} test cases passed.")
    return 1 if failures else 0


def run(genre):
    """Entry point each thin per-genre script calls. Returns a process exit code."""
    if "--test-file" in sys.argv:
        idx = sys.argv.index("--test-file")
        if idx + 1 >= len(sys.argv):
            print("--test-file requires a path argument.")
            return 1
        return run_test_file(genre, sys.argv[idx + 1])
    return run_ci(genre)

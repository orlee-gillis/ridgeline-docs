# .github/scripts/validate-parent-report.py

import os
import sys
import glob
import re
import json
from pathlib import Path
import anthropic

def parse_frontmatter(content):
    """Extract YAML frontmatter from markdown."""
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not match:
        return {}

    frontmatter_text = match.group(1)
    frontmatter = {}
    for line in frontmatter_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            frontmatter[key.strip()] = value.strip()
    return frontmatter

def extract_sections(content):
    """Extract section headings from markdown."""
    # Skip frontmatter
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

    sections = {}
    current_section = None
    section_content = []

    for line in content.split('\n'):
        if line.startswith('## '):
            if current_section:
                sections[current_section] = '\n'.join(section_content).strip()
            current_section = line[3:].strip()
            section_content = []
        elif current_section:
            section_content.append(line)

    if current_section:
        sections[current_section] = '\n'.join(section_content).strip()

    return sections

def validate_parent_report_mechanical(sections):
    """Check that required sections exist and are non-empty."""
    required = ['Introduction', 'Requirements']
    missing = []
    empty = []

    for section in required:
        if section not in sections:
            missing.append(section)
        elif not sections[section].strip():
            empty.append(section)

    return missing, empty

def validate_parent_report_ai(filepath, sections):
    """Use Claude to validate template compliance of Introduction section."""
    client = anthropic.Anthropic(api_key=os.environ.get("CLAUDE_API_KEY").strip()

    intro = sections.get('Introduction', '')

    prompt = f"""Review this parent-report Introduction section against the template requirements.

The Introduction should:
1. State the problem the hub solves
2. Explain the value proposition
3. Explain why this hub exists
4. Be 1-2 paragraphs

Here's the Introduction from the page:

{intro}

Respond with JSON:
{{
  "valid": true/false,
  "issues": ["issue1", "issue2"]
}}

If valid is true, issues should be empty. If valid is false, list 1-3 specific issues."""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=200,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    try:
        response_text = message.content[0].text
        result = json.loads(response_text)
        return result.get('valid', False), result.get('issues', [])
    except:
        return False, ["Claude validation failed"]

def main():
    # Find all markdown files in docs/
    files = glob.glob('docs/**/*.md', recursive=True)

    parent_reports = []

    for filepath in files:
        with open(filepath, 'r') as f:
            content = f.read()

        frontmatter = parse_frontmatter(content)

        # Only validate files marked as parent-report
        if frontmatter.get('template') != 'parent-report':
            continue

        parent_reports.append(filepath)
        sections = extract_sections(content)

        # Mechanical validation
        missing, empty = validate_parent_report_mechanical(sections)

        if missing:
            print(f"❌ {filepath}: Missing sections: {', '.join(missing)}")
        if empty:
            print(f"❌ {filepath}: Empty sections: {', '.join(empty)}")

        # AI validation
        if not missing and not empty:
            valid, issues = validate_parent_report_ai(filepath, sections)
            if not valid:
                print(f"⚠️ {filepath}: Template compliance issues:")
                for issue in issues:
                    print(f"   - {issue}")
            else:
                print(f"✅ {filepath}: Passes validation")

    if not parent_reports:
        print("ℹ️ No parent-report files found to validate")
        sys.exit(0)

if __name__ == "__main__":
    main()

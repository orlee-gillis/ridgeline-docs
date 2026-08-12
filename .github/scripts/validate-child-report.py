# .github/scripts/validate-child-report.py

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

def validate_child_report_mechanical(sections):
    """Check that required sections exist and are non-empty."""
    required = ['Introduction', 'Requirements', 'Where to find the report']
    missing = []
    empty = []

    for section in required:
        if section not in sections:
            missing.append(section)
        elif not sections[section].strip():
            empty.append(section)

    return missing, empty

def validate_child_report_ai(filepath, sections):
    """Use Claude to validate Introduction section has one-line value prop and glossary-aligned definition."""
    client = anthropic.Anthropic(api_key=os.environ.get("CLAUDE_API_KEY"))

    intro = sections.get('Introduction', '')

    prompt = f"""Review this child-report Introduction section against the template requirements.

The Introduction should:
1. Start with a one-line value proposition (what this report shows/does)
2. Include 1-2 paragraphs of glossary-aligned definition of key concepts
3. Be grounded in the glossary, not invented terminology

Here's the Introduction:

{intro}

Respond with JSON:
{{
  "valid": true/false,
  "issues": ["issue1", "issue2"]
}}

Issues might include: missing value proposition, vague definitions, undefined terms, lacks glossary grounding."""

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
    files = glob.glob('docs/**/*.md', recursive=True)

    child_reports = []

    for filepath in files:
        with open(filepath, 'r') as f:
            content = f.read()

        frontmatter = parse_frontmatter(content)

        if frontmatter.get('template') != 'child-report':
            continue

        child_reports.append(filepath)
        sections = extract_sections(content)

        # Mechanical validation
        missing, empty = validate_child_report_mechanical(sections)

        if missing:
            print(f"❌ {filepath}: Missing sections: {', '.join(missing)}")
        if empty:
            print(f"❌ {filepath}: Empty sections: {', '.join(empty)}")

        # AI validation
        if not missing and not empty:
            valid, issues = validate_child_report_ai(filepath, sections)
            if not valid:
                print(f"⚠️ {filepath}: Template compliance issues:")
                for issue in issues:
                    print(f"   - {issue}")
            else:
                print(f"✅ {filepath}: Passes validation")

    if not child_reports:
        print("ℹ️ No child-report files found to validate")
        sys.exit(0)

if __name__ == "__main__":
    main()

# .github/scripts/validate-workflow-methodology.py

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

def count_steps(sections):
    """Count how many step sections exist (## Step 1, ## Step 2, etc)."""
    step_count = 0
    for section in sections.keys():
        if re.match(r'^Step \d+', section):
            step_count += 1
    return step_count

def validate_workflow_mechanical(sections):
    """Check that required sections exist and are non-empty."""
    required = ['Introduction', 'Requirements']
    missing = []
    empty = []

    for section in required:
        if section not in sections:
            missing.append(section)
        elif not sections[section].strip():
            empty.append(section)

    # Check that at least 3 steps exist
    step_count = count_steps(sections)
    if step_count < 3:
        missing.append(f"At least 3 steps (found {step_count})")

    # Check all steps are non-empty
    for i in range(1, step_count + 1):
        step_key = f"Step {i}"
        if step_key in sections and not sections[step_key].strip():
            empty.append(step_key)

    return missing, empty

def validate_workflow_ai(filepath, sections):
    """Use Claude to validate that steps explain their benefits/goals."""
    client = anthropic.Anthropic(api_key=os.environ.get("CLAUDE_API_KEY"))

    # Collect all steps
    steps = {}
    for section in sections.keys():
        if re.match(r'^Step \d+', section):
            steps[section] = sections[section]

    steps_text = '\n\n'.join([f"{name}:\n{content}" for name, content in steps.items()])

    prompt = f"""Review these workflow steps against the template requirements.

Each step should:
1. Explain the benefit or goal of that step (what it accomplishes)
2. Be clearly sequenced (the order makes sense)
3. Include actionable instructions

Here are the steps:

{steps_text}

Respond with JSON:
{{
  "valid": true/false,
  "issues": ["issue1", "issue2"]
}}

Issues might include: unclear goal, poor sequencing, missing instructions, steps too vague."""

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

    workflows = []

    for filepath in files:
        with open(filepath, 'r') as f:
            content = f.read()

        frontmatter = parse_frontmatter(content)

        if frontmatter.get('template') != 'workflow-methodology':
            continue

        workflows.append(filepath)
        sections = extract_sections(content)

        # Mechanical validation
        missing, empty = validate_workflow_mechanical(sections)

        if missing:
            print(f"❌ {filepath}: Missing sections: {', '.join(missing)}")
        if empty:
            print(f"❌ {filepath}: Empty sections: {', '.join(empty)}")

        # AI validation
        if not missing and not empty:
            valid, issues = validate_workflow_ai(filepath, sections)
            if not valid:
                print(f"⚠️ {filepath}: Template compliance issues:")
                for issue in issues:
                    print(f"   - {issue}")
            else:
                print(f"✅ {filepath}: Passes validation")

    if not workflows:
        print("ℹ️ No workflow-methodology files found to validate")
        sys.exit(0)

if __name__ == "__main__":
    main()

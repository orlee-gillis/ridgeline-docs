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
    """Use Claude to validate template compliance of

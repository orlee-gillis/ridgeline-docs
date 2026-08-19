#!/usr/bin/env python3
"""Validates docs/**/*.md pages tagged `template: parent-report` against the parent-report
genre requirements in ai-workflow/skills/ridgeline-doc-auditor/references/audit-checklist.md.

See gate_common.py for the shared implementation and --test-file usage.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from gate_common import run

if __name__ == "__main__":
    sys.exit(run("parent-report"))

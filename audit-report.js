#!/usr/bin/env node
// Session 22: audit-report-pages gate.
//
// Reviews report-style doc pages against the Report page requirements in
// ai-workflow/skills/ridgeline-doc-auditor/references/audit-checklist.md,
// using the same audit lens as the ridgeline-doc-auditor skill. Blocks the
// pull request when any page scores "high"; "medium" and "low" are
// report-only. See GATES-DESIGN.md and .claude/gates-architecture.md.
//
// Two modes:
//   node audit-report.js                          CI mode (default) - diffs
//                                                  the PR, audits changed
//                                                  report pages, posts a PR
//                                                  comment, exits non-zero
//                                                  on any "high" finding.
//   node audit-report.js --test-file <path.json>   Local test mode - runs
//                                                  the fixtures in the given
//                                                  file, compares actual vs.
//                                                  expected severity.

'use strict';

const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const MODEL = 'claude-sonnet-5';
const REPO_ROOT = __dirname;
const AUDITOR_SKILL_PATH = path.join(REPO_ROOT, 'ai-workflow/skills/ridgeline-doc-auditor/SKILL.md');
const CHECKLIST_PATH = path.join(REPO_ROOT, 'ai-workflow/skills/ridgeline-doc-auditor/references/audit-checklist.md');
const TRIGGER_GLOBS = [/docs\/.*report.*\.md$/i, /docs\/.*\/child-.*\.md$/i];

const RESPONSE_SCHEMA = {
  type: 'object',
  properties: {
    purpose_summary: {
      type: 'string',
      description: 'One or two sentences: what this page is for, and whether it does that.',
    },
    highest_severity: { type: 'string', enum: ['none', 'low', 'medium', 'high'] },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          severity: { type: 'string', enum: ['low', 'medium', 'high'] },
          class: {
            type: 'string',
            enum: ['genre', 'structure', 'order', 'fact', 'term', 'consistency'],
          },
          description: { type: 'string' },
          source: {
            type: 'string',
            description: 'The rule or section this finding is based on, e.g. "audit-checklist.md, Report page"',
          },
        },
        required: ['severity', 'class', 'description', 'source'],
        additionalProperties: false,
      },
    },
  },
  required: ['purpose_summary', 'highest_severity', 'findings'],
  additionalProperties: false,
};

function extractSection(markdown, heading) {
  const lines = markdown.split('\n');
  const start = lines.findIndex((l) => l.trim() === `## ${heading}`);
  if (start === -1) return null;
  let end = lines.length;
  for (let i = start + 1; i < lines.length; i++) {
    if (/^## /.test(lines[i])) {
      end = i;
      break;
    }
  }
  return lines.slice(start, end).join('\n').trim();
}

function buildPrompt(pageContent) {
  const skill = fs.readFileSync(AUDITOR_SKILL_PATH, 'utf8');
  const checklist = fs.readFileSync(CHECKLIST_PATH, 'utf8');
  const reportSection = extractSection(checklist, 'Report page');
  if (!reportSection) {
    throw new Error(`Could not find "## Report page" section in ${CHECKLIST_PATH}`);
  }

  return `You are auditing a Ridgeline documentation page against the Report page genre.

Below is the audit method and severity framework this project uses (the ridgeline-doc-auditor skill):

${skill}

Below is the Report page genre's required sections (from the audit checklist this skill cites):

${reportSection}

Map this skill's severity vocabulary to the gate's severity vocabulary:
  blocker    -> high    (blocks the pull request)
  should-fix -> medium  (reported on the pull request, does not block)
  optional   -> low     (informational only)

Audit the page below. Only report a finding if you can cite a source for it (a section of the
checklist, or a specific unsupported/undefined claim within the page itself) - if you cannot cite
one, do not report it. If the page has no problems, return an empty findings array and
highest_severity: "none".

Page content:

---
${pageContent}
---`;
}

async function callClaude(prompt) {
  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey) {
    throw new Error('ANTHROPIC_API_KEY is not set.');
  }

  const res = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'content-type': 'application/json',
      'x-api-key': apiKey,
      'anthropic-version': '2023-06-01',
    },
    body: JSON.stringify({
      model: MODEL,
      max_tokens: 2000,
      output_config: {
        effort: 'medium',
        format: { type: 'json_schema', schema: RESPONSE_SCHEMA },
      },
      messages: [{ role: 'user', content: prompt }],
    }),
  });

  if (!res.ok) {
    const body = await res.text();
    throw new Error(`Claude API request failed: ${res.status} ${body}`);
  }

  const data = await res.json();
  const textBlock = (data.content || []).find((b) => b.type === 'text');
  if (!textBlock) {
    throw new Error('Claude response contained no text block.');
  }
  return JSON.parse(textBlock.text);
}

async function auditPage(filepath) {
  const content = fs.readFileSync(path.join(REPO_ROOT, filepath), 'utf8');
  const prompt = buildPrompt(content);
  return callClaude(prompt);
}

// ---- Local test mode ----

async function runTestFile(testFilePath) {
  const suite = JSON.parse(fs.readFileSync(testFilePath, 'utf8'));
  let failures = 0;

  for (const testCase of suite.testCases) {
    process.stdout.write(`${testCase.id} (${testCase.name})... `);
    try {
      const result = await auditPage(testCase.filepath);
      const expected = testCase.expectedSeverity;
      const actual = result.highest_severity;
      if (actual === expected) {
        console.log(`PASS (severity: ${actual})`);
      } else {
        failures++;
        console.log(`FAIL - expected severity "${expected}", got "${actual}"`);
        for (const f of result.findings) {
          console.log(`    [${f.severity}] (${f.class}) ${f.description} - ${f.source}`);
        }
      }
    } catch (err) {
      failures++;
      console.log(`ERROR - ${err.message}`);
    }
  }

  console.log(`\n${suite.testCases.length - failures}/${suite.testCases.length} test cases passed.`);
  if (failures > 0) process.exitCode = 1;
}

// ---- CI mode ----

function getChangedDocFiles() {
  const baseRef = process.env.GITHUB_BASE_REF ? `origin/${process.env.GITHUB_BASE_REF}` : 'origin/main';
  const diffOutput = execFileSync('git', ['diff', '--name-only', `${baseRef}...HEAD`], {
    cwd: REPO_ROOT,
    encoding: 'utf8',
  });
  return diffOutput
    .split('\n')
    .map((l) => l.trim())
    .filter(Boolean)
    .filter((f) => TRIGGER_GLOBS.some((re) => re.test(f)))
    .filter((f) => fs.existsSync(path.join(REPO_ROOT, f)));
}

function formatComment(results) {
  if (results.length === 0) return null;

  const lines = ['## Audit report pages', ''];
  const blocking = results.some(({ result }) => result.highest_severity === 'high');

  for (const { filepath, result } of results) {
    lines.push(`### \`${filepath}\``);
    lines.push('');
    lines.push(result.purpose_summary);
    lines.push('');
    if (result.findings.length === 0) {
      lines.push('No problems found.');
    } else {
      lines.push('| Severity | Class | Problem | Source |');
      lines.push('| --- | --- | --- | --- |');
      for (const f of result.findings) {
        lines.push(`| ${f.severity} | ${f.class} | ${f.description} | ${f.source} |`);
      }
    }
    lines.push('');
  }

  lines.push('---');
  lines.push(
    blocking
      ? '*This check blocks the pull request because at least one page scored high severity.*'
      : '*Advisory findings only - none of these block the pull request.*'
  );
  lines.push(`*Generated by \`${MODEL}\` via \`audit-report.js\`.*`);

  return lines.join('\n');
}

async function postComment(body) {
  const token = process.env.GITHUB_TOKEN;
  const repo = process.env.GITHUB_REPOSITORY;
  const pr = process.env.PR_NUMBER;
  if (!token || !repo || !pr) {
    console.log('GITHUB_TOKEN, GITHUB_REPOSITORY, or PR_NUMBER not set - skipping comment post.');
    return;
  }

  const res = await fetch(`https://api.github.com/repos/${repo}/issues/${pr}/comments`, {
    method: 'POST',
    headers: {
      authorization: `Bearer ${token}`,
      accept: 'application/vnd.github+json',
      'content-type': 'application/json',
    },
    body: JSON.stringify({ body }),
  });

  if (!res.ok) {
    console.log(`Could not post comment: ${res.status} ${await res.text()}`);
  } else {
    console.log('Comment posted.');
  }
}

async function runCiMode() {
  const files = getChangedDocFiles();
  if (files.length === 0) {
    console.log('No changed files match docs/**/*report*.md or docs/**/child-*.md. Nothing to audit.');
    return;
  }

  const results = [];
  for (const filepath of files) {
    console.log(`Auditing ${filepath}...`);
    const result = await auditPage(filepath);
    results.push({ filepath, result });
  }

  const comment = formatComment(results);
  if (comment) await postComment(comment);

  const blocking = results.some(({ result }) => result.highest_severity === 'high');
  if (blocking) {
    console.error('\nBlocking: at least one page scored high severity.');
    process.exitCode = 1;
  } else {
    console.log('\nNo blocking findings.');
  }
}

// ---- Entry point ----

async function main() {
  const args = process.argv.slice(2);
  const testFileIdx = args.indexOf('--test-file');

  if (testFileIdx !== -1) {
    const testFilePath = args[testFileIdx + 1];
    if (!testFilePath) {
      console.error('--test-file requires a path argument.');
      process.exitCode = 1;
      return;
    }
    await runTestFile(path.resolve(REPO_ROOT, testFilePath));
  } else {
    await runCiMode();
  }
}

main().catch((err) => {
  console.error(err);
  process.exitCode = 1;
});

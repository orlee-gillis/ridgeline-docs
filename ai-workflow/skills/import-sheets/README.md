# import-sheets Skill

This skill automates importing CSV files into Google Sheets as separate worksheet tabs.

## Installation

Copy the `import-sheets` folder to `~/.claude/skills/`:

```bash
cp -r import-sheets ~/.claude/skills/
```

## Usage

Invoke the skill by typing:

```
/import-sheets
```

Or describe your task naturally:
- "I need to import CSVs into Google Sheets"
- "How do I upload these CSV files to a spreadsheet?"
- "Import my data files into Google Sheets"

The skill will guide you through:
1. Providing your CSV folder path
2. Providing your Google Sheets ID
3. Running the automated import

## Files included

- **SKILL.md** - Skill definition and instructions
- **scripts/import_csvs_to_sheets.py** - The actual Python script for importing

## One-time setup

Before using this skill, you need Google Cloud credentials:

1. Create a Google Cloud Project
2. Enable Google Sheets API and Google Drive API
3. Create a Service Account and download credentials as JSON
4. Save `credentials.json` in your CSV folder
5. Share your Google Sheet with the service account email

See SKILL.md for detailed steps.

## Notes

- CSV files must be in the same folder as `credentials.json`
- The script works on Mac, Linux, and Windows
- Python 3 is required (most systems have this already)
- The script auto-installs required Python libraries on first run

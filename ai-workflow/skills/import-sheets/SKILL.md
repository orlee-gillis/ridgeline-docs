---
name: import-sheets
description: Automate importing CSV files into Google Sheets as separate tabs. Use this whenever the user needs to import multiple CSV files into a Google Sheets spreadsheet, whether for a renovation project, inventory tracking, data organization, or any other use case. Handles all authentication, sheet creation, and data population. Trigger when the user mentions importing CSVs, uploading data to Google Sheets, or organizing spreadsheet data from files.
---

# CSV to Google Sheets Importer

Automates importing multiple CSV files into Google Sheets as separate worksheet tabs. Requires only two inputs: the folder path containing your CSV files and your Google Sheets ID.

## What you need before starting

1. **CSV files** in a single folder (any names, they'll become sheet tab names)
2. **credentials.json** - Google Cloud Service Account credentials in the same folder
3. **Google Sheets ID** - from your spreadsheet URL
4. **Python 3** installed on your machine

## Getting Google Cloud credentials (one-time setup)

If you don't have credentials.json yet:

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create or select a project
3. Enable these APIs:
   - Google Sheets API
   - Google Drive API
4. Create a Service Account:
   - Click "Create Credentials" → "Service Account"
   - Fill in the details, click "Create and Continue"
5. Go to the Service Account page, click the **Keys** tab
6. Click "Add Key" → "Create new key" → select **JSON**
7. Save the downloaded file as `credentials.json` in your CSV folder
8. Copy the service account email (looks like `something@...iam.gserviceaccount.com`)
9. Open your Google Sheet, click **Share**, and share it with that service account email

## How to use this skill

When you want to import CSVs to Google Sheets:

1. **Provide your CSV folder path**
   - Example: `/Users/yourname/Documents/MyProject/` or `C:\Users\yourname\Documents\MyProject\`
   - Make sure `credentials.json` is in this folder

2. **Provide your Google Sheets ID**
   - Open your spreadsheet in a browser
   - Copy the ID from the URL: `https://docs.google.com/spreadsheets/d/COPY_THIS_PART/edit`
   - Paste just the ID part (no slashes or `/edit`)

3. **Wait** - The script discovers all CSV files, authenticates, creates/updates sheets, and populates your data

## What happens

- **New sheets** are created for each CSV file
- **Existing sheets** are cleared and replaced with new data
- **Sheet names** match your CSV filenames (minus the `.csv` extension)
- **All data** from your CSV is imported, including headers

## Troubleshooting

| Error | Fix |
| --- | --- |
| `credentials.json not found` | Make sure it's in the same folder as your CSV files |
| `Failed to open spreadsheet` | Check the ID is correct; make sure you shared the sheet with the service account email |
| `Permission denied` | Share the Google Sheet with the service account email from your credentials |
| `Module not found: gspread` | Run: `pip install gspread google-auth-httplib2 google-auth-oauthlib` |
| `No CSV files found` | Check that CSV files end with `.csv` and are in the correct folder |

## Running manually (if you prefer)

If you want to run the import script directly without this skill:

```bash
python import_csvs_to_sheets.py
```

The script will prompt you for the folder path and spreadsheet ID interactively.

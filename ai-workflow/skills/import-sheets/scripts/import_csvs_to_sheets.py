#!/usr/bin/env python3
"""
Simple CSV to Google Sheets Importer
Just point it to your CSV folder and spreadsheet - that's it!
"""

import os
import csv
import sys
from pathlib import Path

try:
    import gspread
    from google.oauth2.service_account import Credentials
except ImportError:
    print("Installing required libraries...")
    os.system(f"{sys.executable} -m pip install gspread google-auth-httplib2 google-auth-oauthlib")
    import gspread
    from google.oauth2.service_account import Credentials

def main():
    print("\n" + "="*70)
    print("SIMPLE CSV TO GOOGLE SHEETS IMPORTER")
    print("="*70)

    # Get CSV folder path
    print("\nEnter the folder path with your CSV files:")
    print("(Example: /Users/orleegillis/Documents/Duchifat26)")
    csv_folder = input("Folder path: ").strip()

    if not csv_folder:
        print("❌ No folder provided")
        sys.exit(1)

    csv_folder = os.path.expanduser(csv_folder)

    if not os.path.isdir(csv_folder):
        print(f"❌ Folder not found: {csv_folder}")
        sys.exit(1)

    # Check for credentials
    creds_path = os.path.join(csv_folder, 'credentials.json')
    if not os.path.exists(creds_path):
        print(f"❌ credentials.json not found in {csv_folder}")
        print("Make sure credentials.json is in your CSV folder")
        sys.exit(1)

    # Get spreadsheet ID
    print("\nEnter your Google Sheets ID:")
    print("From: https://docs.google.com/spreadsheets/d/YOUR_ID_HERE/edit")
    spreadsheet_id = input("Spreadsheet ID: ").strip()

    if not spreadsheet_id:
        print("❌ No ID provided")
        sys.exit(1)

    # Find CSV files
    csv_files = {}
    for file in os.listdir(csv_folder):
        if file.endswith('.csv') and file != 'credentials.json':
            name = file[:-4]  # Remove .csv
            csv_files[name] = file

    if not csv_files:
        print(f"❌ No CSV files found in {csv_folder}")
        sys.exit(1)

    print(f"\n✓ Found {len(csv_files)} CSV file(s)")

    # Authenticate
    print("\nAuthenticating with Google Sheets...")
    try:
        scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = Credentials.from_service_account_file(creds_path, scopes=scopes)
        gc = gspread.authorize(creds)
        print("✓ Authentication successful!")
    except Exception as e:
        print(f"❌ Authentication failed: {e}")
        sys.exit(1)

    # Open spreadsheet
    print(f"\nOpening spreadsheet...")
    try:
        spreadsheet = gc.open_by_key(spreadsheet_id)
        print(f"✓ Opened: {spreadsheet.title}")
    except Exception as e:
        print(f"❌ Failed to open spreadsheet: {e}")
        print("\nMake sure:")
        print("  1. The spreadsheet ID is correct")
        print("  2. You've shared the sheet with the service account email")
        sys.exit(1)

    # Import files
    print("\n" + "="*70)
    print("IMPORTING")
    print("="*70)

    created = 0
    updated = 0
    existing = {ws.title for ws in spreadsheet.worksheets()}

    for tab_name, filename in sorted(csv_files.items()):
        filepath = os.path.join(csv_folder, filename)
        print(f"\n{tab_name}:")

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                rows = list(csv.reader(f))

            if not rows:
                print(f"  (empty file)")
                continue

            if tab_name in existing:
                worksheet = spreadsheet.worksheet(tab_name)
                worksheet.clear()
                print(f"  Cleared existing sheet")
                updated += 1
            else:
                worksheet = spreadsheet.add_worksheet(title=tab_name, rows=len(rows)+10, cols=8)
                print(f"  Created new sheet")
                created += 1

            worksheet.append_rows(rows)
            print(f"  ✓ Added {len(rows)} rows")

        except Exception as e:
            print(f"  ❌ Error: {e}")

    # Done
    print("\n" + "="*70)
    print("✓ COMPLETE!")
    print("="*70)
    print(f"Sheets created: {created}")
    print(f"Sheets updated: {updated}")
    print(f"\nView your spreadsheet:")
    print(f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}")

if __name__ == '__main__':
    main()

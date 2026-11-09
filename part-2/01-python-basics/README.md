# Step 1: What I automated and the time it saves

**Date:** 9 Nov 2026

## What I built

I wrote two small Python scripts, both run in Google Colab.

1. **API to CSV** (`api_to_csv.py`). The script asks a public test website for 100 posts and saves each post's id and title to a spreadsheet file (`posts.csv`). I checked the result by counting the lines: 101, which is the header row plus 100 posts.
2. **Page dates for the Ridgeline docs** (`page_dates.py`). The script lists the 21 pages in the `docs/` folder of this repo, finds the date each one last changed, and saves them oldest first to `page_dates.csv`.

## What I learned

- A script asks a service for data, reads the reply, and writes the useful parts into a file. Both scripts follow this pattern.
- A "post" in the test script is a made-up blog post. The POST request method is a different thing.
- Checking the result is part of the job. I counted the lines and read the first rows before trusting the file.

## Time saved

- **Copying 100 titles by hand:** about 30 minutes (my estimate).
- **Checking 21 pages by hand:** roughly 5 minutes to open each page's history on GitHub (my estimate). The script does it in seconds.
- Reviewing the list still takes time, because someone has to decide which pages to update.

## What the results show

Of the 21 pages, 19 haven't changed since August. The oldest is `index.md`, from 27 July, and the newest are the marketing work sample pages, from 4 October. The dates come from the edit history in GitHub, not from a "last updated" line on the site, so they show when the source file changed, not when the page was last reviewed.

## Limits

- The scripts read public data without a key. For a private system like Confluence, the script would need a secret key, which I'd keep out of the code.
- GitHub limits anonymous requests to about 60 an hour. This run used about 22, so it's fine for now.

## Next steps

- Review the oldest pages first.
- Point the page-dates script at the help center or Pendo once I have access to them.

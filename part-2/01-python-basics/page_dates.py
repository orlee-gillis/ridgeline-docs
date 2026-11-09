import csv
import requests

owner = "orlee-gillis"
repo = "ridgeline-docs"
branch = "main"

# 1. Get the list of all files in the repo
tree_url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
tree = requests.get(tree_url).json()["tree"]

# 2. Keep only the site's pages (files in docs/ ending in .md or .mdx)
pages = [item["path"] for item in tree
         if item["path"].startswith("docs/")
         and item["path"].endswith((".md", ".mdx"))]
print("Pages found:", len(pages))

# 3. For each page, get the date of its latest change
rows = []
for path in pages:
    commits_url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    commits = requests.get(commits_url, params={"path": path, "per_page": 1}).json()
    last_changed = commits[0]["commit"]["committer"]["date"][:10]
    rows.append([path, last_changed])

# 4. Sort oldest first, so the most out-of-date pages are at the top
rows.sort(key=lambda r: r[1])

# 5. Save to a file
with open("page_dates.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["page", "last_changed"])
    writer.writerows(rows)

print("Saved page_dates.csv")

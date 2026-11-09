import csv
import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
print("Status:", response.status_code)

posts = response.json()
print("Number of posts:", len(posts))

with open("posts.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "title"])
    for post in posts:
        writer.writerow([post["id"], post["title"]])

print("Saved posts.csv")

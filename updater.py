"""from scraper import get_total_additions_deletions
from bs4 import BeautifulSoup
import requests

with open("README_template.md", "r") as f:
    readme_template = f.read()

total_additions = 0
total_deletions = 0

repos = requests.get("https://github.com/DerSchinken?tab=repositories")
repos = BeautifulSoup(repos.content, "html.parser").find_all(itemprop="name codeRepository")
for repo in repos:
    gtad = get_total_additions_deletions("DerSchinken", repo.string.strip()).values()
    total_additions += gtad["total_additions"]
    total_deletions += gtad["total_deletions"]

with open("README.md", "w") as f:
    f.write(readme_template.format(adds=total_additions, removes=total_deletions))
"""
import os
from github import Github

# Get token
token = os.environ.get("GITHUB_TOKEN")

g = Github(token)


def get_total_additions_deletions(username: str) -> dict:
    total_additions = 0
    total_deletions = 0

    for repo in g.get_user(username).get_repos():
        for commit in repo.get_commits():
            total_additions += commit.stats.additions
            total_deletions += commit.stats.deletions

    return {"total_additions": total_additions, "total_deletions": total_deletions}


with open("README_template.md", "r") as f:
    template = f.read()
    
with open("README.md", "w") as f:
    f.write(template.format(**get_total_additions_deletions("DerSchinken")))

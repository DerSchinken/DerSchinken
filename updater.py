import os
from github import Github

# Get token
token = os.environ.get("GITHUB_TOKEN")

g = Github(token)


def get_total_additions_deletions(username: str) -> dict:
    total_additions = 0
    total_deletions = 0

    for repo in g.get_user(username).get_repos():
        for weekly_code_frequency in repo.get_stats_code_frequency():
            total_additions += weekly_code_frequency.additions
            total_deletions += weekly_code_frequency.deletions

    return {"total_additions": total_additions, "total_deletions": total_deletions}


with open("README_template.md", "r") as f:
    template = f.read()
    
with open("README.md", "w") as f:
    f.write(template.format(**get_total_additions_deletions("DerSchinken")))

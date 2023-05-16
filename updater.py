import os
from github import Github
from datetime import datetime

# Get token
token = os.environ.get("GITHUB_TOKEN")

g = Github(token)


def get_total_additions_deletions(username: str) -> dict:
    total_additions = 0
    total_deletions = 0

    # if g.get_user(username).avatar_url != g.get_user().avatar_url:
    for repo in g.get_user(username).get_repos(visibility="all"):
        for weekly_code_frequency in repo.get_stats_code_frequency():
            total_additions += weekly_code_frequency.additions
            total_deletions += weekly_code_frequency.deletions
    """
    else:
        # not working bcc for some reason some repos are restricted 403 {"message": "Repository access blocked", ...}
        for repo in g.get_repos(visibility="all"):
            if not repo.get_stats_code_frequency():
                continue
            for weekly_code_frequency in repo.get_stats_code_frequency():
                total_additions += weekly_code_frequency.additions
                total_deletions += weekly_code_frequency.deletions
    """

    return {"total_additions": total_additions, "total_deletions": abs(total_deletions)}


with open("README_template.md", "r") as f:
    template = f.read()
    
with open("README.md", "w") as f:
    f.write(template.format(**get_total_additions_deletions("DerSchinken"), age=eval(f"int({datetime.now().year}.{datetime.now().month}-2005.12-1)")))

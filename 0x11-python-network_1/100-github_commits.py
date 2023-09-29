#!/usr/bin/python3
"""Lists 10 commits of a given repository of a given user
    Using the GitHub API.

    Usage:
        ./100-github_commits.py <repository name> <owner name>
"""
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    headers = {
            "Accept": "application/vnd.github+json",
    }

    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        commits = res.json()
        length = min(len(commits), 10)

        for i in range(length):
            commit = commits[i]
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author}")

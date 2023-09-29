#!/usr/bin/python3
"""Gets the id of the user with the credentials passed in as arguments.
    Using the GitHub API.

    Usage:
        ./10my_github.py <username> <password or PAT>
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = sys.argv[1]
    pwd = sys.argv[2]
    headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {pwd}"
    }

    res = requests.get(url, headers=headers)

    obj = res.json()
    if obj:
        print(f"{obj.get('id')}")

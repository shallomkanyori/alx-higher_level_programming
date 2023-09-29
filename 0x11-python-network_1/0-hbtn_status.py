#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status.
    Displays a formatted response body.
"""
import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        res = response.read()
        print("Body response:")
        print(f"    - type: {type(res)}")
        print(f"    - content: {res}")
        print(f"    - utf8 content: {res.decode('UTF-8')}")

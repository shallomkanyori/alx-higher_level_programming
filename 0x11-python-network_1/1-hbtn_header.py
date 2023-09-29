#!/usr/bin/python3
"""Fetches URL and displays value of the X-Request-Id header.

    Usage:
        1-hbtn_header.py <URL>
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        res = response.info().get("X-Request-Id")
        print(res)

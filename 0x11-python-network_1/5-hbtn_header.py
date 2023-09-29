#!/usr/bin/python3
"""Fetches URL and displays value of the X-Request-Id header using requests.

    Usage:
        ./5-hbtn_header.py <URL>
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    res = requests.get(url).headers.get("X-Request-Id")
    print(res)

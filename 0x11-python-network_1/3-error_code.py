#!/usr/bin/python3
"""Sends a request to the given URL and displays a decoded response body.
    Manages urllib.error.HTTPError exceptions by printing the status code.

    Usage:
        ./3-error_code.py <URL>
"""
import urllib.request
import urllib.parse
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            res = response.read()
            print(res.decode('UTF-8'))

    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

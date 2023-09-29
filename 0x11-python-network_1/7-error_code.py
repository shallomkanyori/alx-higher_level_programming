#!/usr/bin/python3
"""Sends a request to the given URL and displays a decoded response body.
    Prints the status code if it is greater than or equal to 400.

    Usage:
        ./7-error_code.py <URL>
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    res = requests.get(url)

    if res.status_code < 400:
        print(res.text)
    else:
        print(f"Error code: {res.status_code}")

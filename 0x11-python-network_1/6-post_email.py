#!/usr/bin/python3
"""Sends a POST request to the given URL with the given email as a parameter.
    Displays the body of the response (decoded in utf-8).

    Usage:
        ./6-post_email.py <URL> <email>
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    res = requests.post(url, data={"email": email})
    print(res.text)

#!/usr/bin/python3
"""Sends a POST request to the given URL with the given email as a parameter.
    Displays the body of the response (decoded in utf-8).

    Usage:
        ./2-post_email.py <URL> <email>
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    params = {"email": email}
    data = urllib.parse.urlencode(params).encode("utf-8")

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        res = response.read()
        print(res.decode('UTF-8'))

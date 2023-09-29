#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user.
    Sends the letter argument passed in as a parameter.
    Displays the body of the response if it is properly JSON formatted.

    Usage:
        ./8-post_email.py <letter>
"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    res = requests.post(url, data={"q": letter})

    try:
        obj = res.json()
        if not obj:
            print("No result")
        else:
            print(f"[{obj.get('id')}] {obj.get('name')}")

    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")

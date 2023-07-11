#!/usr/bin/python3
"""This module defines a script that saves its arguments to a file.

    It adds all its program arguments to a list then saves that list to a file.
"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """Saves all arguments to a file as a list."""

    filename = "add_item.json"
    args = None

    try:
        args = load_from_json_file(filename)
    except Exception:
        pass

    args = [] if args is None else args
    args.extend([arg for arg in sys.argv[1:]])

    try:
        save_to_json_file(args, filename)
    except Exception:
        pass


if __name__ == "__main__":
    main()

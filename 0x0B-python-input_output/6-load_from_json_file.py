#!/usr/bin/python3
"""This module defines the load_from_json_file function."""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file.

        Args:
            filename (str): the name of the file.
    """
    obj = None

    with open(filename, encoding="utf-8") as f:
        obj = json.load(f)

    return obj

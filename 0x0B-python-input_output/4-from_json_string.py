#!/usr/bin/python3
"""This module defines the from_json_string function."""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string.

        Args:
            my_str (str): the JSON string.
    """
    return json.loads(my_str)

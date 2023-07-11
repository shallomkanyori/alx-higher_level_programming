#!/usr/bin/python3
"""This module defines the to_json_string function."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object.

        Args:
            my_object (obj): the object.
    """
    return json.dumps(my_obj)

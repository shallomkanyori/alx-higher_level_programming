#!/usr/bin/python3
"""This module defines the save_to_json_file function."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation.

        Args:
            my_obj (obj): the object to write.
            filename (str): the name of the file to write to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)

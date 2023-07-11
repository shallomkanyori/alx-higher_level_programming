#!/usr/bin/python3
"""This module defines the class_to_json function."""


def class_to_json(obj):
    """Returns the dictionary description for Json serialization of an object.

        Args:
            obj (obj): an instance of a class.
    """
    return obj.__dict__

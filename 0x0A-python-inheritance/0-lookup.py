#!/usr/bin/python3
"""This module defines the lookup function."""


def lookup(obj):
    """Returns the list of available attributes and methods of an object.

        Args:
            obj: the object.
    """
    return dir(obj)

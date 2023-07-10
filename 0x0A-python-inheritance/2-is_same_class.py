#!/usr/bin/python3
"""This module defines the is_same_class function."""


def is_same_class(obj, a_class):
    """Returns True if an object is exactly an instance of a class.

        Args:
            obj: the object to check.
            class: the class to check against.
    """
    return type(obj) is a_class

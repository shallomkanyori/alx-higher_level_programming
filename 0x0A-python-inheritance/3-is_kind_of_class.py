#!/usr/bin/python3
"""This module defines the is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class.

        Args:
            obj: the object to check.
            a_class: the class to check.
    """
    return isinstance(obj, a_class)

#!/usr/bin/python3
"""This module defines the inherits_from function."""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a subclass of a class.

        Args:
            obj: the object to check.
            a_class: the class to check against.
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)

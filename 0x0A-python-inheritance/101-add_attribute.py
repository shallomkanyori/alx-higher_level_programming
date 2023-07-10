#!/usr/bin/python3
"""This module defines the add_attribute function."""


def add_attribute(obj, name, value):
    """Adds an attribute to an object if possible.

        Args:
            obj: the object to add the new attribute to.
            name: the name of the new attribute.
            value: the value of the new attribute.

        Raises:
            TypeError: if the object can't have new attributes.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    obj.__setattr__(name, value)

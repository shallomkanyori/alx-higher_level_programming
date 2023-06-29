#!/usr/bin/python3
"""This module defines the function add_integer().

    Functions:

        add_integer(a, b)"""


def add_integer(a, b=98):
    """Returns a + b.
        a (int or float): first number.
        b (int or float): second number. Defaults to 98."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

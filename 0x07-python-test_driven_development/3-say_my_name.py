#!/usr/bin/python3
"""This module defines the say_my_name function.

    Functions:

        say_my_name(first_name, last_name)"""


def say_my_name(first_name, last_name=""):
    """Prints an introduction string with the given names.

        Args:
            first_name (string): the first name.
            last_name (string): the last name. Default to an empty string."""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")

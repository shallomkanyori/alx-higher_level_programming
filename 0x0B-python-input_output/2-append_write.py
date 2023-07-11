#!/usr/bin/python3
"""This module defines the append_write function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file.

        Args:
            filename (str): the name of the file.
            text (str): the string to write to the file.

        Returns:
            (int): the number of characters added.
    """
    chars_added = 0

    with open(filename, "a", encoding="utf-8") as f:
        chars_added = f.write(text)

    return chars_added

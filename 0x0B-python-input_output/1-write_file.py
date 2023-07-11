#!/usr/bin/python3
"""This module defines the write_file function."""


def write_file(filename="", text=""):
    """Writes a string to a text file.

        Args:
            filename (str): the name of the file.
            text (str): the string to write to the file.

        Returns:
            (int): the number of characters written.
    """
    chars_written = 0

    with open(filename, "w", encoding="utf-8") as f:
        chars_written = f.write(text)

    return chars_written

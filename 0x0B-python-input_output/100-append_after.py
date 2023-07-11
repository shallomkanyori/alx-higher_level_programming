#!/usr/bin/python3
"""This module defines the append_after function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file after each line containing string.

        Args:
            filename (str): the name of the file.
            search_string (str): the string to search for.
            new_string (str): the string to add to the file.
    """
    with open(filename, "r+", encoding="utf-8") as f:
        lines = f.readlines()

        for i, line in enumerate(lines):
            if search_string in line:
                lines[i] = line + new_string

        f.seek(0)
        f.truncate()  # clear file

        f.writelines(lines)

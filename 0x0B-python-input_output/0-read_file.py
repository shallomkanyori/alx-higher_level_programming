#!/usr/bin/python3
"""This module defines the read_file function."""


def read_file(filename=""):
    """Reads text from a file and prints it to stdout.

        Args:
            filename (string): the name of the file.
    """
    with open(filename, encoding="utf_8") as f:
        print(f.read(), end="")

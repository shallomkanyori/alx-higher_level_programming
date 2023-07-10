#!/usr/bin/python3
"""This module defines the MyList class."""


class MyList(list):
    """Defines a subclass of list."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        res = self[:]
        res.sort()
        print(res)

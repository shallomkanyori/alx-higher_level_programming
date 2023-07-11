#!/usr/bin/python3
"""This module defines the pascal_triangle function."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle of n.

        Args:
            n (int): the number of rows in the Pascal triangle.
    """
    res = []

    if (n <= 0):
        return res

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(res[i - 1][j - 1] + res[i - 1][j])

        res.append(row)

    return res

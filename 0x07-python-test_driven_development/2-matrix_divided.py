#!/usr/bin/python3
"""This module defines the matrix_divided() and check_matrix() functions.

    Functions:

        check_matrix(matrix)
        matrix_divided(matrix, div)"""


def check_matrix(matrix):
    """Returns true if the matrix is a list of lists of ints and/or floats."""
    if type(matrix) is not list:
        return False

    for row in matrix:
        if type(row) is not list:
            return False

        if not all(isinstance(x, (int, float)) for x in row):
            return False

    return True


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number.

        Args:
            matrix (list of lists of int): the matrix.
            div (int or float): the  number to divide by."""

    if not check_matrix(matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        + "integers/floats")

    row_len = len(matrix[0]) if matrix else 0

    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(x / div, 2) for x in row] for row in matrix]

    return result

#!/usr/bin/python3
"""This module defines the matrix_mul function.

    Functions:

        check_matrices(m_a, m_b)
        matrix_mul(m_a, m_b)"""


def check_matrices(m_a, m_b):
    """Checks matrices for valid multiplication.

        Args:
            m_a (list of lists of ints and/or floats): the first matrix.
            m_b (list of lists of ints and/or floats): the first matrix."""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if not all(type(row) is list for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(type(row) is list for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(x, (int, float)) for row in m_a for x in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(x, (int, float)) for row in m_b for x in row):
        raise TypeError("m_b should contain only integers or floats")

    row_len_a = len(m_a[0])
    if not all(len(row) == row_len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    row_len_b = len(m_b[0])
    if not all(len(row) == row_len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if row_len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

        Args:
            m_a (list of lists of ints and/or floats): the first matrix.
            m_b (list of lists of ints and/or floats): the first matrix."""
    check_matrices(m_a, m_b)  # check for and raise errors when necessary

    result = [
                [sum(a * b for a, b in zip(row, col)) for col in zip(*m_b)]
                for row in m_a]

    return result

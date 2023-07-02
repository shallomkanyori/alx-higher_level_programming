#!/usr/bin/python3
"""This module defines the lazy_matrix_mul function.

    Functions:

        lazy_matrix_mul(m_a, m_b)"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using numpy.

        Args:
            m_a (list of lists of ints or floats): the first matrix.
            m_b (list of lists of ints or floats): the second matrix."""
    return np.matmul(m_a, m_b)

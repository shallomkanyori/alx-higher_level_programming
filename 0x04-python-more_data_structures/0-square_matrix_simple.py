#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Returns a matrix consisting of the square of all integers of a matrix"""
    if matrix:
        return [[x ** 2 for x in row] for row in matrix]

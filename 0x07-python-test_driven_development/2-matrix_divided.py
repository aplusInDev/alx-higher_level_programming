#!/usr/bin/python3
"""
Module to divide a matrix
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix.

    Args:
        matrix : Argument
        div : Argument

    """
    ErrMsg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(matrix) is list:
        length = len(matrix[0])
        for row in matrix:
            if type(row) is not list:
                raise TypeError(ErrMsg)
            if len(row) != length:
                raise TypeError(
                    'Each row of the matrix must have the same size')
            for element in row:
                if not isinstance(element, (int, float)):
                    raise TypeError(ErrMsg)
    else:
        raise TypeError(ErrMsg)
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round((element / div), 2))
        new_matrix.append(new_row)
    return new_matrix

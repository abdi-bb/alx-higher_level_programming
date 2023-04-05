#!/usr/bin/python3

'''
module name: '2-matrix_divided'
functions inside the module:
    matrix_divided(matrix, div)
'''


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix: a list of lists of integers or floats representing the matrix.
        div: a number (integer or float) to divide the matrix elements by.

    Returns:
        A new matrix with all elements of the input matrix divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: if the matrix is not a list of lists of integers or floats,
                  or if each row of the matrix is not of the same size.
                  The error message will be
                  "matrix must be a matrix (list of lists) of integers floats"
                  or "Each row of the matrix must have the same size".
        TypeError: if div is not a number (integer or float).
                  The error message will be "div must be a number".
        ZeroDivisionError: if div is equal to 0.
                  The error message will be "division by zero".
    """
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for lst in matrix:
        if type(lst) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(lst)
        elif size != len(lst):
            raise TypeError("Each row of the matrix must have the same size")
        for i in lst:
            if type(i) is not int and type(i) is not float:
                msg1 = 'matrix must be a matrix (list of lists)'
                msg2 = ' of integers/floats'
                msg = msg1 + msg2
                raise TypeError(msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix

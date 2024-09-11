#!/usr/bin/python3
"""
This module contains the function matrix_divided.

Usage:
    Use the function to divide all elements of a matrix
    (list of lists) by a given divisor (int or float).
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix.

    Parameters:
        matrix (list of lists): A matrix where each element is an integer
                                or a float. Raises a TypeError
                                if this condition is not met.
        div (int or float): The number to divide each element of the matrix by.
                            Raises a TypeError if not an int or float.
                            Raises a ZeroDivisionError if equal to 0.

    Returns:
        new_matrix (list of lists): A new matrix with the result of the
                                    division, rounded to 2 decimal places.
                                    The size of the new matrix is the same
                                    as the original.

    Raises:
        TypeError: If the matrix contains non-numerical elements, if the matrix
                   rows are not of the same size, or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    reference_size = 0
    mat_err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    size_err_msg = "Each row of the matrix must have the same size"
    try:
        if not isinstance(div, (int, float)) or isinstance(div, bool):
            raise TypeError("div must be a number")

        if div == 0:
            raise ZeroDivisionError("division by zero")

        if not matrix:
            raise TypeError(mat_err_msg)

        for row in matrix:
            if not row:
                raise TypeError(mat_err_msg)
            if reference_size == 0:
                reference_size = len(row)
            elif reference_size != len(row):
                raise TypeError(size_err_msg)
            for dividend in row:
                if (not isinstance(dividend, (int, float)) or 
                        isinstance(dividend, bool)):
                    raise TypeError(mat_err_msg)

        new_matrix = []
        for row in matrix:
            new_col = []
            for dividend in row:
                new_col.append(round(dividend / div, 2))
            new_matrix.append(new_col)

        return new_matrix
    except TypeError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)

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
    if not matrix:  # Check if matrix is empty
        raise TypeError(mat_err_msg)

    # Check the type of div
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check and create an new divised array
    new_matrix = []
    for row in matrix:
        if not row:  # Check if row is empty
            raise TypeError(mat_err_msg)
        if reference_size == 0:  # Get the size of a row if not
            reference_size = len(row)
        elif reference_size != len(row):  # Compare size of all rows
            raise TypeError(size_err_msg)
        new_col = []
        for num in row:
            if not isinstance(num, (int, float)) or isinstance(num, bool):
                raise TypeError(mat_err_msg)
            new_col.append(round(num / div, 2))  # Add divided number
        new_matrix.append(new_col)  # Add row in new list

    return new_matrix

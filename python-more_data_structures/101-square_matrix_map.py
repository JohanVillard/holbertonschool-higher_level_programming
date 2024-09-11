#!/usr/bin/python3


def square_matrix_map(matrix=[]):
    """
    Computes the square value of all integers of a matrix using 'map'.

    Parameters:
        matrix (list of lists): Contains numbers.

    Returns:
        The function returns the squared numbers of matrix.
    """
    return list(map(lambda x: list(map(lambda y: (y**2), x)), matrix))

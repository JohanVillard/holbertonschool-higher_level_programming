#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """
    Compute the square value of all integers of a matrix.

    Parameters:
    matrix (list of lists): A 2D list (matrix) where each element is an integer.

    Returns:
    list of lists: A new matrix with the square of each integer from the original matrix.
    """
    # Map each array which map each element in it
    new_matrix = list(map(lambda x: list(map(lambda y: (y**2), x)), matrix))

    return new_matrix

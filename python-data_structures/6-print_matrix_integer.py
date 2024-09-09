#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """
    Print a matrix of integers.

    Description:
        This function takes a matrix (a list of lists) of integers and prints
        it to the console. Each row of the matrix is printed on a new line,
        with elements in each row separated by spaces. If the matrix is emptyor
        or contains only an empty list, it prints an empty line.

    Parameters:
        matrix (list of lists): A 2D list representing the matrix of integers.
                                Default is an empty matrix ([[]]).

    Returns:
        None: This function doesn't return anything; it prints the matrix to
              the console.
    """
    for row in matrix:
        for element in row:
            if element != row[-1]:
                print("{:d}".format(element), end=" ")
            else:
                print("{:d}".format(element), end="")
        print()

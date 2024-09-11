#!/usr/bin/python3
"""
This module contains the function print_square().

Usage:
    Enter the size (int) to print a square.
    The size must be more than 0.
"""


def print_square(size):
    """
    Print a square with the character #.

    Parameters:
        size (int): is the size length of the square.

    Returns:
        None: Don't return any value.
    """
    not_int_msg = "size must be an integer"
    try:
        if not isinstance(size, (int, float)) or isinstance(size, bool):
            raise TypeError(not_int_msg)
        if isinstance(size, float) and size < 0:
            raise TypeError(not_int_msg)
        if size < 0:
            raise ValueError("size must be >= 0")

        hash = "#"
        for row in range(size):  # Print square
            print("{:s}".format(hash * size))

    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

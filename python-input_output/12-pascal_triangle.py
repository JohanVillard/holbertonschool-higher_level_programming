#!/usr/bin/python3
"""This module defines a 'pascal_triangle' function."""


def pascal_triangle(n):
    """
    Return a list of lists representing the Pascal's triangle of n.

    Parameter:
        n (int): The number of lists in the list.

    Returns:
        list of lists: Return a Pascal's triangle of n,
                       if n <= 0, return an empty list.
    """
    row = []
    for i in range(n):
        col = []
        for j in range(i + 1):
            # First number or Last Number, always 1
            if not col or j == i:
                col.append(1)
            else:
                col.append(row[i - 1][j - 1] + row[i - 1][j])
        row.append(col)

    return row

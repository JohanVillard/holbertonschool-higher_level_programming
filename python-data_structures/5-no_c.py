#!/usr/bin/python3


def no_c(my_string):
    """
    Remove all characters c and C from a string.

    Description:
        This function creates a new string with all characters from the input
        string, except for lowercase 'c' and uppercase 'C'.

    Parameters:
        my_string (str): The input string to be processed.

    Returns:
        str: A new string with all 'c' and 'C' characters removed.
    """
    new_string = ""
    for char in my_string:
        if char != "c" and char != "C":
            new_string += char

    return new_string

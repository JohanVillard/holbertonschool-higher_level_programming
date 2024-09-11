#!/usr/bin/python3
"""
This module contains the function `add_integer`.

The `add_integer` function adds two integers, where floating-point numbers
are converted to integers. If the provided arguments are not integers or
floats, a `TypeError` is raised.

Usage:
    To use this module, import it and call the `add_integer` function with
    two arguments. The function will return the sum of the two arguments
    after converting them to integers.
"""


def add_integer(a, b=98):
    """
    Add 2 integers or floats.

    Parameters:
        a (int, float): Is the first number to add. If the input is not the
                        specified type, a 'TypeError' will raise.
                        If a is a float, it must be cast to int.
        b (int, float): Is the first number to add. If the input is not the
                        specified type, a 'TypeError' will raise.
                        If b is a float, it must be cast to int.
    Returns:
        sum (int): Is the result of the additiion of a and b.
    """
    int_err_msg = "must be an integer"
    try:
        if not isinstance(a, (int, float)):
            raise TypeError("a {:s}".format(int_err_msg))
        if not isinstance(b, (int, float)):
            raise TypeError("b {:s}".format(int_err_msg))

        # Cast float into integer if necessary
        if isinstance(a, float):
            a = int(a)
        if isinstance(b, float):
            b = int(b)

        return a + b

    except TypeError as e:
        print(e)  # Display the custom error message without traceback

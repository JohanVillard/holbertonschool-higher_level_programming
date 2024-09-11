#!/usr/bin/python3
"""
This module contains the function `say_my_name`.

Usage:
    Import this module and call `say_my_name`
    with a first name and an optional last name.
"""


def say_my_name(first_name, last_name=""):
    """
    Print "My name is <first_name> <last_name>".

    This function prints a formatted string that includes the provided first
    and last names. If only the first name is provided, the last name will
    be omitted in the output.

    Parameters:
        first_name (str): The first name to be included in the output.
                          Must be a non-empty string.
        last_name (str, optional): The last name to be included in the output.
                                   Defaults to an empty string.
                                   Must be a string.

    Raises:
        TypeError: If `first_name` is not a string or is empty.
                   If `last_name` is not a string.

    Returns:
        None: This function does not return a value.
              It prints the formatted string directly.
    """
    try:
        if not isinstance(first_name, str) or not first_name:
            raise TypeError("first_name must be a string")
        elif not isinstance(last_name, str):
            raise TypeError("last_name must be a string")

        print("My name is {:s} {:s}".format(first_name, last_name))
    except TypeError as e:
        print(e)

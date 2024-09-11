#!/usr/bin/python3
"""
This module contains the function `text_indentation`.

Usage:
    Import this module and call `text_indentation` with a string argument.

"""


def text_indentation(text):
    """
    Print text with indentation after each occurrence of '.', '?', and ':'.

    This function takes a string and adds two new lines after each of the
    specified characters ('.', '?', ':'). It also ensures that there is no
    extra space at the beginning or end of each printed line.

    Parameters:
        text (str): The text to be indented and printed. Must be a string.

    Raises:
        TypeError: If `text` is not a string.

    Returns:
        None: This function does not return a value.
        It prints the formatted text directly.
    """
    try:
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        line = ""
        for char in text:
            if char in ".?:":
                print("{:s}{:s}\n".format(line.lstrip(), char))
                line = ""
            else:
                line += char

        if line:  # Print last line if exist
            print(line.lstrip(), end="")
    except TypeError as e:
        print(e)

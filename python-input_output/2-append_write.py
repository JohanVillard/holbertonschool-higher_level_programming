#!/usr/bin/python3
"""This module defines the 'append_write' function."""


def append_write(filename="", text=""):
    """
    Append text in a file.

    Parameters:
        filename (str): the name of the file to which the text is added.
        text (str): The text to append in the file.

    Returns:
        int : Thefunction returns the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

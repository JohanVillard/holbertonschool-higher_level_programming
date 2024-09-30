#!/usr/bin/python3
"""This module defines a 'write_file' function."""


def write_file(filename="", text=""):
    """
    Write a string into a file.

    Parameters:
        filename (str): The name of the file into write.
        text (str): The text to write in the file.

    Returns:
        int: Returns the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

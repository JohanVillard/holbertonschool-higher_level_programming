#!/usr/bin/python3
"""This module defines a function 'read_file'."""


def read_file(filename=""):
    """
    Read a file.

    Parameter:
        filename (str): The name of file to read.

    Returns:
        str: The function returns a string in text mode.
        bytes: The function returns a bytes object in binary mode.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read())

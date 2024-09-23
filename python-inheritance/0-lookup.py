#!/usr/bin/python3
"""This module defines the function 'lookup()'."""


def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    This function returns a list of the attributes and methods
    that are available for the provided object.

    Parameters:
        obj (object): The object whose attributes and methods are to be
                      retrieved.

    Returns:
        list: A list of strings, each representing an attribute or method of
              the object.
    """
    return dir(obj)

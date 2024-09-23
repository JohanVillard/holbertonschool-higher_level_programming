#!/usr/bin/python3
"""This module defines the function 'is_kind_of_class'."""


def is_kind_of_class(obj, a_class):
    """
    Check if the obj is an instance of, or inherited from, the specified class.

    Parameters:
        obj (object): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if the object is an instance o the specified class
              or if it is an instance of a class that inherited from it.
              Otherwise False.
    """
    return isinstance(obj, a_class)

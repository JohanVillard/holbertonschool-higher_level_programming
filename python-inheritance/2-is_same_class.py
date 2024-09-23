#!/usr/bin/python3
"""This module defines the function 'is_same_class'."""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    This function checks if the type of the object matches the
    specified class exactly (not considering subclass instances).

    Parameters:
        obj (object): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if the object is an insatnce of to the specified class,
              otherwise False.
    """
    return type(obj) is a_class

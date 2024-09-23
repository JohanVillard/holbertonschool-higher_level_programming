#!/usr/bin/python3
"""This module defines the function 'inherits_from'."""


def inherits_from(obj, a_class):
    """
    Check the class inheritance without his proper class..

    This function returns True if the object is an instance of a class
    that inherited from the given class, but not if the object is
    exactly an instance of the specified class.

    Parameters:
        obj (object): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if the object is an instance of a class that
              inherited(directly or indirectly) from the specified class.
              Otherwise False.
    """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    return False

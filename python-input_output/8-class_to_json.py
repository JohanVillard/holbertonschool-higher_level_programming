#!/usr/bin/python3
"""This module defines a 'class_to_json_' class."""


def class_to_json(obj):
    """
    Return the dictionary description.

    Parameter:
        obj (obj): The object to describe.

    Returns:
        dict: Return the dictionary description with simple data structure
              (list, dictionary, string, integer and boolean)
              for JSON serialization of an object.
    """
    return obj.__dict__

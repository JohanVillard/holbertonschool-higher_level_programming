#!/usr/bin/python3
"""This module defines a 'from_json_string' function."""

import json

def from_json_string(my_str):
    """
    Return an object(Python data structure) represented by a JSON string.

    Parameters:
        my_str (str): The JSON string to convert into Python object.mro

    Returns:
        obj: Returns a Python object.
    """
    # loads s stand for string
    return json.loads(my_str)

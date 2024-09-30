#!/usr/bin/python3
"""This module defines a to_json_string' function."""

import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object.

    Parameter:
        my_obj (obj): The object to represent in JSON.

    Returns:
        str: The function return a JSON representation of an object(str).
    """
    return json.dumps(my_obj)

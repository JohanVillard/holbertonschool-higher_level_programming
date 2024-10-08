#!/usr/bin/python3
"""This module defines a 'save_to_json_file' function."""

import json


def save_to_json_file(my_obj, filename):
    """
    Write an Object to a text file, using JSON representation.

    Parameters:
        my_obj (obj): The object to write in a text file.
        filename (str): The name of the file wich the object is written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)

#!/usr/bin/python3
"""This module defines a 'load_from_json_file' function."""

import json


def load_from_json_file(filename):
    """
    Create an Object from a "JSON file".

    Parameter:
        filename (str): The name of the JSON file which the Object is created.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)

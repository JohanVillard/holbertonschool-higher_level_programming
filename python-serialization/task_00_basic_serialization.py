"""This module defines serialization/deserialization functions."""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize and save a Python dictionary to a JSON file.

    Parameters:
        data (dict): A Python dictionary with data.
        filename (str): The filename of the output JSON file.
                        If the output file already exists it should be
                        replaced.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file to as Python dictionary.

    Parameter:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: This function returns a Python dictionary with
              the serialized JSON data from the file.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)

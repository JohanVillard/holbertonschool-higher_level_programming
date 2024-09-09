#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """
    Replace or adds a key/value pair in a dictionary.

    If the key already exists in the dictionary, its value is updated.
    If the key does not exist, a new key/value pair is added.

    Parameters:
    a_dictionary (dict): The dictionary to be updated.
    key: The key to be added or updated in the dictionary.
    value: The value associated with the key.

    Returns:
    dict: The updated dictionary.
    """
    pair = {key: value}
    a_dictionary.update(pair)

    return a_dictionary

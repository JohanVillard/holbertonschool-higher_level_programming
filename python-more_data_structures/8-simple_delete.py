#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """
    Delete a key from a dictionary if it exists.

    If the key is found in the dictionary, it is removed along
    with its associated value.
    If the key is not found, the dictionary remains unchanged.

    Parameters:
    a_dictionary (dict): The dictionary from which to delete the key.
    key: The key to be deleted from the dictionary. Default is an empty string.

    Returns:
    dict: The updated dictionary with the key removed,
    or the original dictionary
          if the key does not exist.
    """
    a_dictionary.pop(key, None)

    return a_dictionary

#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2.

    Parameters:
    a_dictionary (dict): The original dictionary with integer or float values.

    Returns:
    dict: A new dictionary where each value from the original dictionary
    is multiplied by 2.
    """
    new_dict = {}
    for key in a_dictionary:
        new_dict[key] = a_dictionary[key] * 2

    return new_dict

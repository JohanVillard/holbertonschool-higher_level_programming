#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary with its keys sorted in alphabetical order.

    Parameters:
    a_dictionary (dict): The dictionary to be printed with keys sorted.

    Returns:
    None: The function prints each key-value pair,
    with the keys in sorted order.
    """
    sorted_dict = dict(sorted(a_dictionary.items()))

    for key in sorted_dict:
        print("{}: {}".format(key, sorted_dict[key]))

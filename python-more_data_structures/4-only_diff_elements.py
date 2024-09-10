#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """
    Returns a set of elements that are present in only one of the two sets.

    The function uses the symmetric difference operation (^) to find elements
    that are in either set_1 or set_2 but not in both.

    Parameters:
    set_1 (set): The first set.
    set_2 (set): The second set.

    Returns:
    set: A set containing the elements that are unique to set_1 or set_2.
    """
    return set_1 ^ set_2

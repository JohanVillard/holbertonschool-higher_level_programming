#!/usr/bin/python3


def max_integer(my_list=[]):
    """
    Find the biggest integer of a list.

    Finds the largest integer in a list.

    Parameters:
        my_list (list):
            A list of integers.
            If the list is empty, the function returns None.

    Returns:
        int or None:
            The largest integer in the list, or None if the list is empty.
    """
    # Check if the list is empty
    if not my_list:
        return None
    else:
        big_i = my_list[0]
        for i in my_list:
            if big_i < i:
                big_i = i

    return big_i

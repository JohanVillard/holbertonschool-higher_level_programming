#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    Add all unique integers in a list (each integer is added only once).

    Parameters:
        my_list (list): A list of integers, which may contain duplicates.

    Returns:
        int: The sum of all unique integers from the list.
    """
    new_array = []
    new_array = list(set(my_list))

    sum = 0
    for num in new_array:
        sum += num

    return sum

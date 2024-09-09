#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """
    Replace an element fo a list at a specific position.

    Description:
        This function attempts to replace an element of the input list at the
        specified index. If the index is negative or out of range, the list
        remains unmodified.

    Parameters:
        my_list (list): the input list of integers to be modified.
        idx (int): the index at which to replace the element.
        element (int): the new integer element to be inserted.

    Returns:
        list: the modified list if the index is valid,
        otherwise the original list.
    """
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list

#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """
    Replace an element in a list at a specific position.

    Description:
        This function creates a new list with the same elements as the input
        list, then replaces the element at the specified index with
        a new element. If the index is negative or out of range,
        a copy of the original list is returned.

    Parameters:
        my_list (list): The original list of elements.
        idx (int): The index at which to replace the element.
        element: The new element to be inserted.

    Returns:
        list: A new list with the element replaced if the index is valid,
              otherwise a copy of the original list.
    """
    new_list = list(my_list)
    if idx < 0:
        return new_list
    elif idx > len(my_list) - 1:
        return new_list
    else:
        new_list[idx] = element
        return new_list

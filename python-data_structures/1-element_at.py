#!/usr/bin/python3


def element_at(my_list, idx):
    """
    Retrieve an element from a list.

    Description:
        This function displays element at choosen index.
        If the index is negative or out of range,
        the function return none.

    Parameters:
        my_list:
            is a collection of integer.
        idx:
            is an integer that represents an index to retrieve an element
            of a list.

    Return:
        element of the list.
    """
    if idx < 0:
        return None
    elif idx > len(my_list) - 1:
        return None
    else:
        return my_list[idx]

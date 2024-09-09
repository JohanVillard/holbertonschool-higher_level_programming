#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    """
    Delete the item at a specific position in a list.

    Parameters:
        my_list (list): The list from which an element will be deleted.
        idx (int): The index of the element to be deleted. If idx is negative
                   or out of range, the list remains unchanged.

    Returns:
        list: The modified list with the element at the given index removed,
              or the original list if idx is invalid(negative or out of range).
    """
    # Compute the length of the list and create a my
    length = len(my_list)

    if idx < 0 or idx > length - 1:
        return my_list

    for i in range(length):
        # Check the index's element to delete
        if (i == idx or i > idx) and (i + 1) < length:
            my_list[i] = my_list[i + 1]

    # Delete last element
    del my_list[-1]

    return my_list

#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """
    Find all multiples of 2 in a list and returns a list of boolean values.

    Parameters:
    my_list (list): A list of integers to be checked.

    Returns:
    list: A list of boolean values where each element corresponds to whether
          the element at the same index in the input list is divisible by 2.
    """
    bool_list = []
    for num in my_list:
        if num % 2 == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)

    return bool_list

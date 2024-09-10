#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    Print x elements of a list.

    Parameters:
        my_list(list): can contain any type(integer, string, etc.).
        x(int): represents the number of elements to print.
                It can be bigger than the length of my_list.

    Returns:
        int: The number of elements successfully printed.
    """
    count = 0
    try:
        for num in my_list:
            print("{}".format(num), end="")
            count += 1
            if x == count:
                break
    except IndexError:
        pass
    print()
    return count

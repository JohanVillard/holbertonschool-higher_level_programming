#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    Replace all occurrences of an element by another in a new list.

    Parameters:
    my_list (list): The original list in which to search for occurrences
    of an element.
    search: The element to search for in the list.
    replace: The element to replace `search` with in the new list.

    Returns:
    list: A new list where all occurrences of `search` are replaced
          by `replace`.
          If `search` is not found, the original list is returned unchanged.
    """
    new_list = list(map(lambda x: replace if x == search else x, my_list))

    return new_list

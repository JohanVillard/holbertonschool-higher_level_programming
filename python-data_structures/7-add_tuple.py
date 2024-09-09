#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """
    Add 2 tuples.

    Add two tuples element-wise.

    Description:
        This function adds the corresponding elements of two tuples. If a tuple
        has fewer than 2 elements, it uses 0 for the missing elements. Only the
        first two elements of each tuple are considered.

    Parameters:
        tuple_a (tuple): The first tuple to be added.
        Defaults to an empty tuple.
        tuple_b (tuple): The second tuple to be added.
        Defaults to an empty tuple.

    Returns:
        tuple: A new tuple containing the sum of the corresponding elements
               from tuple_a and tuple_b.
               The returned tuple always has two elements.
    """
    # Transforms tuples in lists
    l_tuple_a = list(tuple_a)
    l_tuple_b = list(tuple_b)

    # Replaces missing elements by 0
    if len(l_tuple_a) < 2:
        zero_to_add = 2 - len(l_tuple_a)
        for i in range(zero_to_add):
            l_tuple_a.append(0)
    if len(l_tuple_b) < 2:
        zero_to_add = 2 - len(l_tuple_b)
        for i in range(zero_to_add):
            l_tuple_b.append(0)

    # Creates a new list
    new_list = []
    for i in range(2):
        new_list.append(l_tuple_a[i] + l_tuple_b[i])

    # Transforms into tuple
    return tuple(new_list)

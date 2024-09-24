#!/usr/bin/python3
"""This module defines a 'VerboseList' class."""


class VerboseList(list):
    """Represent a list."""

    def append(self, item):
        """
        Add an element to the list and print a message.

        Parameters:
            item (object): The element to append in the list.

        Returns:
            None: After append, print the message  'Added [item] to the list.'
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """
        Add several elements to the list and print a message.

        Parameters:
            items (object): The elements to extend in the list.

        Returns:
            None: After extend, print the message
                  'Extended the list with [items].'
        """
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """
        Remove the specified element to the list and print a message.

        Parameters:
            item (object): The elements to remove from the list.

        Returns:
            None: After remove, print the message
                  'Extended the list with [items].'
        """
        if item in self:
            print(f"Removed [{item}] from the list.")
            super().remove(item)
        else:
            print(f"{item} do not exist in the list")

    def pop(self, position=None):
        """
        Remove the element at position to the list and print a message.

        Parameters:
            position (object): The position which the element is,
                               to it remove from the list.

        Returns:
            None: After pop, print the message
                  'Extended the list with [items].'
        """
        if position is None:
            print(f"Popped [{self[-1]}] from the list.")
            super().pop(-1)
        else:
            print(f"Popped [{self[position]}] from the list.")
            super().pop(position)

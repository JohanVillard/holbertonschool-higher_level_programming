#!/usr/bin/python3
"""
Singly Linked List Module.

This module provides functionality for creating and manipulating
a singly linked list.
A singly linked list is a data structure where each element
(called a node) contains a value and a reference (or link)
to the next node in the sequence.

Available Class:
    Node:
        Available Functions:
            def data(self): Get the value of the data in the 'Node'.
            def data(self, value): Set the value of the data in the 'Node'.
            def next_node(self): Get the address of the next 'Node'.
            def next_node(self, value): Set the address of the next 'Node'.

    SinglyLinkedList:
        Available Functions:
            def sorted_insert(self, value): Insert a new 'Node' into the
            correct sorted position in the list (increasing order).
"""


class Node:
    """Define a node in a singly listed list."""

    def __init__(self, data, next_node=None):
        """
        Initialize a new node.

        Parameters:
            data (int): The value stored in the node.
            next_node (Node): Reference to the next node in the list.
            Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the value of data in the node.

        Returns:
            int: The value of the data.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the value of data in the node.

        Parameters:
            value (int): The value to be stored in the node.

        Raises:
            TypeError: If the provided value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """
        Get the reference to the next node in the list.

        Returns:
            Node or None: The reference to the next Node,
            or None if there is no next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the reference to the next node in the list.

        Parameters:
            value (Node or None): The reference to the next Node,
            or None if there is no next node.

        Raises:
            TypeError: If the value is not a Node or None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """Define an ascending sorted singly linked list."""

    def __init__(self):
        """Initialize."""
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new 'Node' into the correct sorted order.

        Parameters:
            value (int): The value to be stored in the node.
        """
        # Create a new node
        new_node = Node(value)
        # Check if the list is empty
        if self.head is None:
            self.head = new_node
        else:
            # Copy the beginning of the list
            self.curr_node = self.head

            # Check the first Node
            if value < self.curr_node.data:
                new_node.next_node = self.head
                self.head = new_node
            else:
                # Search for a greater value
                while (
                    self.curr_node.next_node is not None
                    and value > self.curr_node.next_node.data
                ):
                    self.curr_node = self.curr_node.next_node

                # Check if last Node
                if self.curr_node.next_node is None:
                    self.curr_node.next_node = new_node
                else:
                    # Link the new node
                    new_node.next_node = self.curr_node.next_node
                    self.curr_node.next_node = new_node

    def __str__(self):
        """
        Return a string representation of the singly linked list.

        Iterates through the list from the head node to the end,
        printing each node's data.
        The last node's data is printed without a newline.

        Returns:
            str: An empty string, as the actual node data is printed directly.
        """
        self.curr_node = self.head
        while self.curr_node is not None:
            if self.curr_node.next_node is not None:
                print(self.curr_node.data)
            else:
                print(self.curr_node.data, end="")
            self.curr_node = self.curr_node.next_node

        return ""

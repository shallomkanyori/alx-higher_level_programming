#!/usr/bin/python3
"""This module defines the Node and SinglyLinkedList classes"""


class Node():
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initializes the node.

        Args:
            data: the node's data.
            next_node: the next node. Defaults to None."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """int: the node's data.

        Raises:
            TypeError: if value is not an integer."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """Node: the next node.

        Raises:
            TypeError: if value is not None or a Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList():
    """Defines a singly linked list"""

    def __init__(self):
        """Initialize the singly linked list"""
        self.__head = None

    def __str__(self):
        """Print the list, one number per line"""
        res = ""
        curr = self.__head

        while curr:
            res += str(curr.data) + "\n"
            curr = curr.next_node

        res = res[:-1] if res else res  # remove extra newline

        return res

    def sorted_insert(self, value):
        """Inserts a new Node in the correct sorted position in the list.

        The list is sorted in increasing order."""

        new = Node(value)

        if not self.__head:
            self.__head = new
            return

        if value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
            return

        prev = self.__head
        while prev.next_node:
            if prev.next_node.data > value:
                break

            prev = prev.next_node

        new.next_node = prev.next_node
        prev.next_node = new

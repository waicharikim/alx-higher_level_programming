#!/usr/bin/python3
"""Provides a class for a singly linked list"""


class Node:
    """
    A class representing a node of a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node): The reference to the next node in the linked list.

    Raises:
        TypeError: If the data is not an integer or \
                if the next_node is not a Node object.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node object with the given \
                data and optional next_node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): The reference \
                    to the next node. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the data stored in the node.

        Returns:
            int: The data of the node.
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Set the data of the node.

        Args:
            value (int): The new data to be set.

        Raises:
            TypeError: If the data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """
        Get the reference to the next node.

        Returns:
            Node: The next node.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the reference to the next node.

        Args:
            value (Node): The new next_node to be set.

        Raises:
            TypeError: If the next_node is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        head (Node): The head node of the linked list.

    Methods:
        sorted_insert(self, value): Inserts a new Node into the \
                correct sorted position in the list (increasing order).
        __str__(self): Returns the string representation of the \
                linked list, displaying one node number per line.
    """

    def __init__(self):
        """
        Initialize an empty singly linked list with the head set to None.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position \
                in the list (increasing order).

        Args:
            value (int): The value to be stored in the new node.
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and \
                    current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns the string representation of the linked list.

        Returns:
            str: The string representation of the linked \
                    list, with one node number per line.
        """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node

        # Remove the last newline character
        if result:
            result = result[:-1]

        return result

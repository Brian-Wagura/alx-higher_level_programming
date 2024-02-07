#!/usr/bin/python3
""" Singly linked list module"""


class Node:
    """defines a node"""

    def __init__(self, data, next_node=None):
        """ Initialize the node with instance variables"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """gets data attribute"""

        return (self.__data)

    @data.setter
    def data(self, value):
        """sets data attribute"""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        get next_node attribute
        Returns: next node
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """set value of next node"""

        if (value is not None and
        not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initializes the singly linked list"""

        self.head = None

    def sorted_insert(self, value):
        """
        Insert in a sorted fashion
        Args:
            value: what the value will be on the node
        """
        new_node = Node(value)
        if (not self.head or self.head.data >=
        new_node.data):
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while (current.next_node and current.next_node.data <
            new_node.data):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Make the list printable"""

        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result

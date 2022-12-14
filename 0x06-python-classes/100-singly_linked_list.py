#!/usr/bin/python3
"""python script about linked-lists"""


class Node:
    """Class definintion of NOde"""

    def __init__(self, data, next_node=None):
        """initialize a new Node instance

        Args:
        self : an instance of the class
        data : an integer
        next_node: a Node object"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter"""
        return(self.__data)

    @data.setter
    def data(self, value):
        """Setter for the attribute data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter"""
        return(self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """ setter for the attribute next_node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initialize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))

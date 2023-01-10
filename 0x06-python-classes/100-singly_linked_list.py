#!/usr/bin/python3
""" 
    Define classes for a singly linked list
"""
class Node:
    def __init__(self, data, next_node=None):
        """
            initialize a new node
            
            Args:
            data (int) - The data of the new node
            next_node (node) - The next node of the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
            A Method to get the data
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
            A Method to set the data input

            Arg:
            value (int) - the data
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
        
    @property
    def next_node(self):
        """
            A method the get the next_node
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
            A method to set the next node
        """
        if ((next_node is not None) and (not isinstance(value, Node)):
                raise TypeError("next node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """
        Defines a singly linked list
    """

    def __init__(self):
        """
            Initialize a singlyLinkedList.
        """
        self.__head = None

    def sorted_insert(self, value):
        
        """
            Insert a new Node to the SinglyLinkedList.
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

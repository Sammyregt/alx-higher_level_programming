#!/usr/bin/python3
""" Define a class named square """


class Square:
    """ Representing the class """

    def __init__(self, size=0):
        """
            A constructor of the square class

        Args:
            size (int): The size of the new square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
            Returns the current sqaure area
        """
        return(self.__size * self.__size)

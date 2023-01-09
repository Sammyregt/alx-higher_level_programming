#!/usr/bin/python3
""" Define a class named square """


class Square:
    """ Representing the class """

    def __init__(self, size=0, position=(0, 0)):
        """
            A constructor of the square class

        Args:
            size (int): The size of the new square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Method to get the current size of the square """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """ Method to get the coordinates of the square """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
            Method to set the coordinates of the square object
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(isinstance(num >= 0) for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
            Returns the current sqaure area
        """
        return(self.__size * self.__size)

    def my_print(self):
        """
            Print the square in #
        """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.position[1]) if (self.position[1] > 0)]
        for i in range(self.size):
            [print(" ", end="") for j in range(self.position[0])]
            [print("#", end="") for k in range(self.size)]
            print("")

#!/usr/bin/python3
"""
A class that defines a square

"""


class Square:
    """
    This class defines a square on some conditions:
        . with a private instance variable
        . instantiating it with an optional size attribute
    """

    def __init__(self, size=0):
        """
        Initializes the class

        """

        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the area of the square

        """

        return(self.__size ** 2)

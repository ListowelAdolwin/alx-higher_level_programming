#!/usr/bin/python3


"""
A basic program with just a class

"""


class Rectangle:
    """
    An empty class

    """

    def __init__(self, width=0, height=0):
        """
        Initializes the object, Rectangle

        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        This method returns just the width

        """

        return (self.__width)
    
    @width.setter
    def width(self, value):
        """
        This checks for exceptions and then 
        sets the value of the width

        """

        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >=0")
        self.__width = value

    
    @property
    def height(self):
        """
        This returns the height of the rectangle

        """
        return (__height)


    @height.setter
    def height(self, value):
        """
        This checks and sets height to value

        """

        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value



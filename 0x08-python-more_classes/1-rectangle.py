#!/usr/bin/python3
"""Rectangle module"""

class Rectangle:
    """A Rectangle Class"""
    def __init__(self, width = 0, height = 0):
        """Constructor function definition
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        Returns: Nothing to return
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """A property width getter"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Width setter
        Args:
            value (int): The width to set
        
        Returns:
            int: the width of the class instance

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Height setter
        Args:
            value (int): The heigth to set
        
        Returns:
            int: the heigth of the class instance

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be >= 0")

        self.__height = value

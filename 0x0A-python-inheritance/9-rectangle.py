#!/usr/bin/python3
"""Module containing Rectangle definition"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class definition"""

    def __init__(self, width, height):
        """constructor

        Args:
            width (int): The width
            height (int): The height
        """
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Computes the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """The string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

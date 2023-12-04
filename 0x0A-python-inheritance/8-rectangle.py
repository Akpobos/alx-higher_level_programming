#!/usr/bin/python3
"""Module defining Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class inherits from a base class"""

    def __init__(self, width, height):
        """constructor

        Args:
            width (int): The width
            height (int): The height
        """
        super().__init__()
        BaseGeometry.integer_validator(width)
        self.__width = width
        BaseGeometry.integer_validator(height)
        self.__height = height

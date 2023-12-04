#!/usr/bin/python3
"""Module defining a Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square Class"""
    def __init__(self, size):
        """constructor
        Args:
            size (int): The size of the square
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

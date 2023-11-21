#!/usr/bin/python3
"""Contains a class Square that defines a square"""

class Square:
    """class Square that defines a square"""

    def __init__(self, size = 0):
        """Constructor
        Args:
            size (int): The size of the square instance
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

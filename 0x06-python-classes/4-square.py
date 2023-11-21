#!/usr/bin/python3
"""Contains a class Square that defines a square"""

class Square:
    """class Square that defines a square"""

    def __init__(self, size = 0):
        """Constructor
        Args:
            size (int): The size of the square instance
        """
        self.size = size

    @property
    def size(self):
        """Getter for attrivute size"""
        return (self.__size)

    @size.setter
    def size(self, size):
        """Setter for size attribute
        Args:
            size (int): The size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of the square instance"""
        return pow(self.__size, 2)

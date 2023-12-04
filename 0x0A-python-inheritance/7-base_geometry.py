#!/usr/bin/python3
"""Defines a Geometry class"""


class BaseGeometry:
    """The Base class for a Geometry"""

    def area(self):
        """Computes the area of the geometry
        Raises:
            Exception: For area not implemented
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validates a value

        Args:
            name (str): name of the value
            value (int): The value
        Raises:

            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

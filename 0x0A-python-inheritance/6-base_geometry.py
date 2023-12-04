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

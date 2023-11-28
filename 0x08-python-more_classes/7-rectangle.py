#!/usr/bin/python3
"""A Rectangle module"""

class Rectangle:
    """A rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __str__(self):
        """Function that defines a string representation of the object instance"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        
        rect = ""
        for i in range(self.__height):
            rect += str(self.print_symbol) * self.__width
            if i < (self.height - 1):
                rect += "\n"

        return (rect)

    def __repr__(self):
        """return a string representation of the rectangle to be able to recreate a new instance by using eval()"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __init__(self, width = 0, height = 0):
        """Constructor Function
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        
        Returns: Nothing
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    
    @property
    def width(self):
        """Getter for width
        Returns:
            int: The width of the rectangle
        """
        return (self.__width)
    
    @width.setter
    def width(self, value):
        """Setter for width
        Args:
            value (int): The value to set on the width
        Returns: Nothing

        Raises:
            TypeError: If value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Getter for height
        Returns:
            int: The height of the rectangle
        """
        return (self.__height)
    
    @height.setter
    def height(self, value):
        """Setter for height
        Args:
            value (int): The value to set on the height
        Returns: Nothing

        Raises:
            TypeError: If value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns the area of the rectangle instance"""
        return (self.__width * self.__height)

    def perimeter(self):
        """the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __del__(self):
        """Print the message Bye rectangle... when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

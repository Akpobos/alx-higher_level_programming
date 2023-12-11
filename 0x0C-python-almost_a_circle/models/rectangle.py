#!/usr/bin/python3
"""Module defining a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class definition"""

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def __init__(self, width, height, x = 0, y = 0, id = None):
        """Constructor
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int): x coordinate
            y (int): y coordinate
            id (int): The identifier
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter property for width
        Return:
            width (int): The width of the rectangle
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """setter function for width
        Args:
            value (int): the value to set

        Raises:
            TypeError: if not an integer
            ValueError: if less than or equals 0 
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter property for height
        Return:
            height (int): The height of the rectangle
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """setter function for height
        Args:
            value (int): the value to set

        Raises:
            TypeError: if not an integer
            ValueError: if less than or equals 0 
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter property for x
        Return:
            x (int): The x of the rectangle
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """setter function for x
        Args:
            value (int): the value to set
        Raises:
            TypeError: if not an integer
            ValueError: if less than or equals 0 
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter property for y
        Return:
            y (int): The y of the rectangle
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """setter function for y
        Args:
            value (int): the value to set

        Raises:
            TypeError: if not an integer
            ValueError: if less than or equals 0 
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of the rectangle instance
        Return:
            (int): The area
        """
        return (self.width * self.height)

    def display(self):
        """prints the rectangle"""
        for i in range(self.y):
            print("")

        for i in range(self.height):
            print(self.x * " " + self.width * "#")

    def update(self, *args, **kwargs):
        """Updates instance fields of this class
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
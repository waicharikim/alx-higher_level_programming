#!/usr/bin/python3
""" This is a rectangle class."""


class Rectangle:
    """
    Rectangle class represents a rectangle with width and height attributes.

    Attributes:
        number_of_instances (int): Class attribute to track the \
            total number of Rectangle instances.

    Args:
        width (int): The width of the rectangle (default is 0).
        height (int): The height of the rectangle (default is 0).

    Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is less than 0.

    Public Methods:
        area(self): Returns the area of the rectangle.
        perimeter(self): Returns the perimeter of the rectangle.
        __str__(self): Returns a string representation of the rectangle.
        __repr__(self): Returns a string representation to recreate \
            the rectangle using eval().
        __del__(self): Destructor method that decrements the \
                number_of_instances on instance deletion.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle \
            using the character '#'."""
        if self.width == 0 or self.height == 0:
            return ""
        rect_str = ""
        for _ in range(self.height):
            rect_str += "#" * self.width + "\n"
        return rect_str[:-1]

    def __repr__(self):
        """Return a string representation of the rectangle \
            to recreate the object."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Destructor method called on instance deletion, decrements \
            number_of_instances."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

#!/usr/bin/python3
"""A rectangle class"""


class Rectangle:
    """
    This class represents a Rectangle.

    Attributes:
        width (int): The width of the rectangle. Default is 0.
        height (int): The height of the rectangle. Default is 0.

    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.

        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width value to be set.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.

        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height value to be set.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.

        """
        return self._width * self._height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.

        """
        return 2 * (self._width + self._height) if self._width and \
            self._height else 0

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        If width or height is 0, returns an empty string.
        Otherwise, returns a string with the rectangle represented by \
            the character(s) in print_symbol.

        Returns:
            str: String representation of the rectangle.

        """
        if self._width == 0 or self._height == 0:
            return ""
        return '\n'.join([str(self.print_symbol) * self._width
                         for _ in range(self._height)])

    def __repr__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: String representation of the rectangle that can be \
                used to recreate a new instance.

        """
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        """
        Print a message when an instance of Rectangle is deleted and \
            decrement the number_of_instances.

        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare two rectangles and return the biggest based on the area.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: The rectangle with the bigger area. If both have the \
                same area value, returns rect_1.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

#!/usr/bin/python3
""" a class defining a rectangle """


class Rectangle:
    """ Attributes: (shared between all class instances,
    class fields and methods)
    __width (int): rectangle width
    __height (int): rectangle height
    """

    def __init__(self, width=0, height=0):
        """ Initialization(run once an object is created), pass
        initial values to object
        Two args: width(init) and height(init), the rectangle width
        and height respectively
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        """ public method, returns rectangle area """
        return self.__height * self.__width

    def perimeter(self):
        """ method returns rectangle perimeter
        perimeter = 0 if width or height is 0 """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    @property
    def width(self):

        """ method that gets object(rectangle) width
        returns object width(int)
        """
        return self.__width

    @width.setter
    def width(self, value):

        """ method acts as a setter, changes attributes values
        arg: value(int), new width value to be set
        raises TypeError and ValueError when value is not an integer
        and value is less than 0 respectively
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):

        """ method that gets object(rectangle) height
                returns object height(int)
        """
        return self.__height

    @height.setter
    def height(self, value):

        """ method acts as a setter, changes attributes values
        arg: value(int), new width value to be set
        raises TypeError and ValueError when value is not an integer
        and value is less than 0 respectively
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

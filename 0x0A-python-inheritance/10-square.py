#!/usr/bin/python3
"""
Rectangle subclass, BaseGeometry grandchild
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle definition
    inherits from BaseGometry
    """

    def __init__(self, width, height):
        """ Rectangle initialization """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def __str__(self):
        """ method returns rectangle description """
        text = '[' + str(self.__class__.__name__) + '] '
        text += str(self.__width) + '/' + str(self.__height)
        return (text)


class Square(Rectangle):
    """ Square class definition """

    def __init__(self, size):
        """ class initialization """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ method returns square area """
        return self.__size ** 2

    def __str__(self):
        """ method returns rectangle description """
        text = '[' + str(self.__class__.__name__) + '] '
        text += str(self.__size) + '/' + str(self.__size)
        return (text)

#!/usr/bin/python3
"""
baseclass - BaseGeometry and subclass - Rectangle
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

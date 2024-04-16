#!/usr/bin/python3
"""
BaseGeometry class definition
"""


class BaseGeometry:

    """
    public method """

    def area(self):

        """ raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """
        public method, raises TypeError and ValueError if,
        value is not an integer and value is <= 0 respectively
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

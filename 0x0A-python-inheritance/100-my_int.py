#!/usr/bin/python3
"""
MyInt class definition
"""


class MyInt(int):
    """ class inverts == and != int operators """

    def __eq__(self, value):
        """
        __eq__, defines the equality operator, '=='
        behaviour for class instances. Can customize
        how the class objects are compared for equality.
        method inverts == to !=
        """
        return self.real != value

    def __ne__(self, value):
        """
        __ne__, defines the 'not equal' (!=) operator behaviour
        for class instances.
        method inverts != to ==
        """
        return self.real == value

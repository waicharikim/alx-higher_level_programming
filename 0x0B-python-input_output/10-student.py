#!/usr/bin/python3
""" class definition """


class Student:
    """ student class definition """

    def __init__(self, first_name, last_name, age):
        """ initialization """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        method retrieve dictionary representation of an instance
        attrs - strings list
        """
        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        else:
            return self.__dict__

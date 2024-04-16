#!/usr/bin/python3
""" class definition """


class Student:
    """ student class definition """

    def __init__(self, first_name, last_name, age):
        """ initialization """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ method retrieve dictionary representation of an instance
        """
        return self.__dict__

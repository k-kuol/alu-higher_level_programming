#!/usr/bin/python3
"""Module that defines a BaseGeometry class"""


class BaseGeometry:
    """A BaseGeometry class with area and integer validation methods"""

    def area(self):
        """Raise an Exception since area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

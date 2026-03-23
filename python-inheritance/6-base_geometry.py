#!/usr/bin/python3
"""Module that defines a BaseGeometry class"""


class BaseGeometry:
    """A BaseGeometry class with area method"""
    
    def area(self):
        """Raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")
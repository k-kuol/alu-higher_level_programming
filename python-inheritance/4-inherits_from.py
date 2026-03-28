#!/usr/bin/python3
"""Module that defines a function to check inheritance"""


def inherits_from(obj, a_class):
    """Return True if object is instance of a class inherited from class"""
    return isinstance(obj, a_class) and type(obj) is not a_class

#!/usr/bin/python3
"""Module that defines a function to check class instance or inheritance"""


def is_kind_of_class(obj, a_class):
    """Return True if object is an instance of, or inherited from, class"""
    return isinstance(obj, a_class)

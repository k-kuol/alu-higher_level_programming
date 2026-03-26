#!/usr/bin/python3
"""is_same_class function module"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified class"""
    return type(obj) is a_class


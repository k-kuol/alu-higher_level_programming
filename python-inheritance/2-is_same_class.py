#!/usr/bin/python3
"""Module that defines a function to check exact class instance"""


def is_same_class(obj, a_class):
    """Return True if the object is exactly an instance of the class"""
    return type(obj) is a_class

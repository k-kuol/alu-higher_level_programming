#!/usr/bin/python3
"""Module that defines a function to check inheritance"""


def inherits_from(obj, a_class):
    """Returns True if object is an instance of a class that inherited from specified class
    
    Args:
        obj: The object to check
        a_class: The class to compare against
        
    Returns:
        True if obj inherits from a_class (but not if obj is exactly a_class), False otherwise
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
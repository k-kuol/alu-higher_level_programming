#!/usr/bin/python3
"""Module that defines a function to lookup attributes and methods"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object
    
    Args:
        obj: The object to inspect
        
    Returns:
        A list of strings representing available attributes and methods
    """
    return dir(obj)

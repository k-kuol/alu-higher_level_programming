#!/usr/bin/python3
"""Module that defines a function to convert class to JSON"""


def class_to_json(obj):
    """Return a dict with simple data structure for JSON serialization."""
    return obj.__dict__

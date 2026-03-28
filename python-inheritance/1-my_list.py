#!/usr/bin/python3
"""Module that defines a MyList class"""


class MyList(list):
    """A class that inherits from list with additional functionality"""

    def print_sorted(self):
        """Print the list, but sorted in ascending order"""
        print(sorted(self))

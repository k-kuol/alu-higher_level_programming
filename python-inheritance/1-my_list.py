#!/usr/bin/python3
"""MyList class module"""


class MyList(list):
    """A class that inherits from list with additional functionality"""
    
    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))


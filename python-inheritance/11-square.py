#!/usr/bin/python3
"""Module that defines a Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class that inherits from Rectangle"""
    
    def __init__(self, size):
        """Initialize a Square instance
        
        Args:
            size (int): The size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    
    def __str__(self):
        """Return string representation of Square
        
        Returns:
            str: String representation in format [Square] <size>/<size>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)


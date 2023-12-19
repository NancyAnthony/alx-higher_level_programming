#!/usr/bin/python3
class Square:
    """A square class"""
    def __init__(self, size=0):
        """Private instance"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        """Sizeo is an int"""

        if size < 0:
            raise ValueError('size must be >= 0')
        """Value Error"""

        self.__size = size

def area(self):
    """For the area"""

     return (self.__size * self.__size)

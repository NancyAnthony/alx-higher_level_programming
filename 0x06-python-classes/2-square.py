#!/usr/bin/python3
"""Task 2"""
class Square:
    def __init(self, size=0):
        """Theo size is zero"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        """Makes sizeo an int"""
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

#!/usr/bin/python3
"""Task 4"""
class Square:
    """A class 2square"""
     def __init__(self, size=0):
         """A func.tieon"""
         if not isinstance(size, int):
            raise TypeError('size must be an integer')
        """An error"""
         if size < 0:
            raise ValueError('size must be >= 0')
        self.___size = size
        
        @property
        def size(self):

            return self.__size
        @size.setter
        def size(self, value):

            if not isinstance(value, int):
                raise TypeError('size must be an integer')

            if value < 0:
                raise ValueError('size must be >= 0')

            self.__size = value

             def area(self):
        """Area"""

        return (self.__size * self.__size)

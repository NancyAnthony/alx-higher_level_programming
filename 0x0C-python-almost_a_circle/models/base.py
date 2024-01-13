#!/usr/bin/python3

"""The base class"""

class Base:
    """A parent class function"""

    __nb_objects = 0
    def __init__(self, id=None):
        """Instantiation methodl"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

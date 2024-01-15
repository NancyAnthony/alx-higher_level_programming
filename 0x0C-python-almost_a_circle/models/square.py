#!/usr/bin/python3
"""A mod sqr"""

from models.rectangle import Rectangle

class Square (Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """ A function that initializes a sqr instance"""


        super() .__init__size, size, x, y, id)

        @property
        def size(self):
            """A functieon that returns self"""

            return (self.width)

        @size.setter
        def size(self, value):
            """A squ function"""

            if type(value) != int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
                self.width = value
                self.height = value

                def update(self, *args, **kwargs):
                    """A function that allows multiple entry"""

                    if len(args) == 0:
                        for key, value in kwargs.items():
                            self.__setattr__(key, value)
                            return

                        try:
                            self.id = args[0]
                            self.size = args[1]
                            self.x = args[2]
                            self.y = args[3]

                         except IndexError:
                            pass

                        def __str__(self):
                            """An str function"""

                            return ("[{}] ({}) {}/{} - {}".format(type(self.__name__, self.id, self.x, self.y, self.width))

                                    def to_dictionary(self):
                                    """A dict function"""

                                    return ({'id': getattr(self, "id"), 'x': getattr(self, "x"),
                                        'size': getattr(self, "size"), 'y': getattr(self, "y")})

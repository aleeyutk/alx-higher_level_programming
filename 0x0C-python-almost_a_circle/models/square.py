#!/usr/bin/python3
"""
Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Write the class Square that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        adding the public method def update
        (self, *args, **kwargs) that assigns attributes
        """
        if args:
            for i, value in enumerate(args):
                if i == 0:
                    self.id = value
                elif i == 1:
                    self.size = value
                elif i == 2:
                    self.x = value
                elif i == 3:
                    self.y = value
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Update the class Square by adding the
        public method def to_dictionary(self):
        """

        listsq2 = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return listsq2

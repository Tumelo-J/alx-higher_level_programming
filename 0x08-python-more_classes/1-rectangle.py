#!/usr/bin/python3

class Rectangle:

    def __init__(self, width=0, height=0):
        self._Rectangle_width = width
        self._Rectangle_height = height

    @property
    def width(self):
        return self._Rectangle_width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an interger")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._Rectangle_width = value

    @property
    def height(self):
        return self._Rectangle_height

    @width.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an interger")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._Rectangle_height = value

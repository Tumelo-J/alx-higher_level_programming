#!/usr/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be and interger")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be and interger")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value

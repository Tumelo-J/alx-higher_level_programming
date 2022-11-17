#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if element in tuple_a or element in tuple_b == "":
        element = 0
    return tuple(map(lambda i, j: i + j, tuple_a, tuple_b))

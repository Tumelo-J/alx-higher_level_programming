#!/usr/bin/python3

def no_c(my_string):
    return "".join(["" if ch in "cC" else ch for ch in my_string])

#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a_dictionary if key == "" else a_dictionary.pop(key)
    return a_dictionary

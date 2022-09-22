#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list
    return [element if idx == i else el for i, el in enumerate(my_list)]

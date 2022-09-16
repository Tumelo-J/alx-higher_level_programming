#!/usr/bin/python3

def uppercase(string):

    new_str = ""
    for ch in (string):
        if ord(ch) in range(97, 123):
            new_str += chr(ord(ch) - 32)
        else:
            new_str += ch

    print("{}\n".format(new_str))


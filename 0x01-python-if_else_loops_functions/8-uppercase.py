#!/usr/bin/python3

def uppercase(str):
    for i, ch in enumerate(str):
        if ord(ch) in range(97, 123):
            str[i] = chr(ord(ch) - 32)
        else:
            str[i] = str[i]
    print("{}\n".format(str))

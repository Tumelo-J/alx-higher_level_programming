#!/usr/python3

def remove_char_at(str, n):
    strcp ="".join(["" if str.index(ch) == n else ch for ch in str])
    return strcp

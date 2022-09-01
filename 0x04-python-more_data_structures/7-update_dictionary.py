#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary.update({key: value})
    return a_dictionary
a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
print(update_dictionary(a_dictionary, 'language', "Python"))

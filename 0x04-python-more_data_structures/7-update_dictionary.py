#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    n = sorted(a_dictionary)
    for i in n:
        if i == key:
            a_dictionary[i] = value
        else:
            a_dictionary[key] = value
    return a_dictionary

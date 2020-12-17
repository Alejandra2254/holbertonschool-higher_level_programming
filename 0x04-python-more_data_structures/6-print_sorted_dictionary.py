#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    n = sorted(a_dictionary)
    for a in n:
        print("{:s}: {}".format(a, a_dictionary[a]))

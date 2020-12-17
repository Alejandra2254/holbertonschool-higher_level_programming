#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == {} or a_dictionary is None:
        return None
    m = sorted(a_dictionary.values())
    max = m[-1]
    for i in a_dictionary:
        if max == a_dictionary[i]:
            return i

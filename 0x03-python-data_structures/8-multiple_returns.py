#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return 0, None
    r = len(sentence)
    i = sentence[0]
    Tuplen = r, i
    return Tuplen

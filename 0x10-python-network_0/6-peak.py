#!/usr/bin/python3
'''module to find the peak function'''

def find_peak(list_of_integers):
    """find the peak"""
    if list_of_integers == []:
        return
    max = 0
    for n in list_of_integers:
        if n > max:
            max = n
    return (max)
    
    

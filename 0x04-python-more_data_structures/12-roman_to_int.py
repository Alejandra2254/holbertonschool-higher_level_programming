#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    if roman_string is None:
        return 0
    for n in range(len(roman_string)):
        if roman_string[n] == "M":
            number += 1000
            if roman_string[n-1] == "C" and n != 0:
                number -= 200
        if roman_string[n] == "D":
            number += 500
            if roman_string[n-1] == "C" and n != 0:
                number -= 200
        if roman_string[n] == "C":
            number += 100
            if roman_string[n-1] == "X" and n != 0:
                number -= 20
        if roman_string[n] == "L":
            number += 50
            if roman_string[n-1] == "X" and n != 0:
                number -= 20
        if roman_string[n] == "X":
            number += 10
            if roman_string[n-1] == "I" and n != 0:
                number -= 2
        if roman_string[n] == "V":
            number += 5
            if roman_string[n-1] == "I" and n != 0:
                number -= 2
        if roman_string[n] == "I":
            number += 1
    return number

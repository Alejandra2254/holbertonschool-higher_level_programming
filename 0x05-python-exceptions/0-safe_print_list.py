#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    try:
        for n in range(0, x):
            print("{}".format(my_list[n]), end="")
            j += 1
        print("")
        return j
    except IndexError:
        print("")
        return j

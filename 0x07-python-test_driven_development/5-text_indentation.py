#!/usr/bin/python3

def text_indentation(text):
    i = 0
    while i < len(text):
        print("{}".format(text[i]), end="")
        if text[i] in [".", "?", ":"]:
            print("")
            print("")
            i +=1
        i +=1

#!/usr/bin/python3
'''Handle error code'''
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    htp = requests.get(url)
    if htp.status_code == 200:
        print(htp.text)
    else:
        print("Error code: {}".format(htp.status_code))

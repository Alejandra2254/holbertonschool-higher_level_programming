#!/usr/bin/python3
'''fetches with the module requests'''
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    header = {}
    header = r.headers
    print(header['X-request-ID'])


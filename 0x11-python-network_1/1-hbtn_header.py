#!/usr/bin/python3
'''Send request to URL, display value X-request-ID found in header'''
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        body = response.read()
        header = {}
        header = response.info()
        print(header['X-request-ID'])

#!/usr/bin/python3
'''fetches with the module requests'''
import requests


if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    header = {}
    header = r.headers
    print(header['X-request-ID'])


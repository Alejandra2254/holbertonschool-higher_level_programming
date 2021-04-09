#!/usr/bin/python3
'''fetches with the module requests'''
import requests


if __name__ == "__main__":
    req = requests.get('https://intranet.hbtn.io/status')
    req = r.txt
    print('Body response:')
    print('\t- type: {}'.format(type(req)))
    print('\t- content: {}'.format(req))

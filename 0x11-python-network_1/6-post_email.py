#!/usr/bin/python3
'''fetches with the module requests'''
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    mail = requests.post(url, data={'email': sys.argv[2]})
    print(mail.text)

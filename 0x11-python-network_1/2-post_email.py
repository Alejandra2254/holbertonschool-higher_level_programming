#!/usr/bin/python3
''' takes in a URL and an email, sends a POST request
    to the passed URL with the email as a parameter, and
    displays the body of the response'''
import urllib.request
import sys

url = sys.argv[1]
value = {'email': sys.argv[2]}

data = urllib.parse.urlencode(value)
data = data.encode('ascii')  # data should be bytes
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
    print(the_page.decode('utf-8'))

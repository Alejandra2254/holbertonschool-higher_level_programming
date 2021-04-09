#!/bin/bash
#  takes in a URL as an argument, sends a GET request to the URL, 
curl -sw '%{http_code}' -o /dev/null "$1"

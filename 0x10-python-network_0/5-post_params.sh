#!/bin/bash
#  takes in a URL as an argument, sends a GET request to the URL, 
# and displays the body of the response
curl "$1" -X POST -d "email: hr@holbertonschool.com" -d "subject: I will always be here for PLD"
#!/bin/bash
#  takes in a URL as an argument, sends a GET request to the URL, 
curl "$1" -X POST -d "email: hr@holbertonschool.com" -d "subject: I will always be here for PLD"

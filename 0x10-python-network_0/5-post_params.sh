#!/bin/bash
#  takes in a URL as an argument, sends a GET request to the URL, 
curl "$1" -X POST --data "email=hr@holbertonschool.com&subject=I will always be here for PLD"

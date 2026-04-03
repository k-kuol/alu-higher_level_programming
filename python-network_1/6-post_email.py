#!/usr/bin/python3
"""Takes in a URL and email, sends POST request with email parameter"""
import requests
import sys

if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], data=data)
    print(response.text)
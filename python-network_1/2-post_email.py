#!/usr/bin/python3
"""Takes in a URL and email, sends POST request with email parameter"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('ascii')
    with urllib.request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode('utf-8'))
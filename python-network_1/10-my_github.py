#!/usr/bin/python3
"""Takes GitHub credentials and uses GitHub API to display user id"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    
    response = requests.get('https://api.github.com/user', auth=(username, password))
    
    if response.status_code == 200:
        try:
            json_response = response.json()
            print(json_response.get('id'))
        except ValueError:
            print(None)
    else:
        print(None)
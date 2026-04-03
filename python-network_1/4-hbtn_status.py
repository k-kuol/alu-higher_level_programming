#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status using requests"""
import requests

if __name__ == "__main__":
    response = requests.get('https://alu-intranet.hbtn.io/status')
    print("Body response:")
    print("    - type: {}".format(type(response.text)))
    print("    - content: {}".format(response.text))
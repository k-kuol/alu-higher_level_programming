#!/bin/bash
# Sends a GET request and displays the body of the response only for a 200 status code
if [ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" = "200" ]; then curl -s "$1"; fi

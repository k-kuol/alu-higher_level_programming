#!/bin/bash
# Sends a GET request and displays the body of the response only for a 200 status code
output=$(curl -s -w "HTTPSTATUS:%{http_code}" "$1") && [[ "$output" =~ HTTPSTATUS:200$ ]] && echo "${output%HTTPSTATUS:200}"

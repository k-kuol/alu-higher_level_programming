#!/bin/bash
# Sends a GET request and displays the body of the response only for a 200 status code
curl -s -w "%{http_code}" "$1" | awk '{a[NR]=$0} END{if(a[NR]=="200") for(i=1;i<NR;i++) print a[i]}'

#!/bin/bash
# Bash script displays size of the body of a response
curl -sI "$1" | awk -F'[\r\n]' '/Content-Length/{print $2}' | tr -d ' '

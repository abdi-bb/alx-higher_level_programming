#!/bin/bash
# Bash script that takes in a URL,
# sends a request to that URL, and displays the size of the body of the response

# Send request and store the response body in a var
response=$(curl -sI "$1")

# Extract the Content-Length from the response
cont_len=$(echo "$response" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r')

# Display the content length in bytes
echo "$cont_len"

#!/usr/bin/python3
'''
Module: '2-post_email'
Sends the POST request andbdisplays the body of the response
'''
import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]

if __name__ == '__main__':
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')

    print(body)

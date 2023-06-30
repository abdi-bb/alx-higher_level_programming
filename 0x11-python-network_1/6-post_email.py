#!/usr/bin/python3
'''
Module: '6-post_email'
POST request and displaying body response
'''

import requests
from sys import argv

if __name__ == '__main__':
    with requests.get(argv[1], argv[2]) as response:
        body = response.text

    print(f'Your email is: {argv[2]}')

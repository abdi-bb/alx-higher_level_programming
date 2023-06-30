#!/usr/bin/python3
'''
Module: '100-github_commits'
'''

import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])
    response = requests.get(url)
    try:
        json_response = response.json()
        for i in range(10):
            print("{}: {}".format(json_response[i].get(
                'sha'), json_response[i].get('commit').get(
                    'author').get('name')))
    except ValueError:
        print("None")

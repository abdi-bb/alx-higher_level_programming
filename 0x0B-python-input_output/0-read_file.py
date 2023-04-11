#!/usr/bin/python3

'''
Module: '0-read_file'
Functions:
    read_file
'''


def read_file(filename=""):
    '''Reads from a file and prints it to stdout.

    Args:
        filename (str): the file to be opened
    '''
    with open(filename, encoding='utf-8') as f:
        data = f.read()
        print(data)

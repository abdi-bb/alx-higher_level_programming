#!/usr/bin/python3

'''
module: '2-append_write'
funcs:
    append_write
'''


def append_write(filename="", text=""):
    '''
    Appends to a file
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        data = f.write(text)
    return data

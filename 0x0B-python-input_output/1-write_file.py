#!/usr/bin/python3

'''
module: '1-write_file'
funcs:
    write_file
'''


def write_file(filename="", text=""):
    '''
    writes a string to a file
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        data = f.write(text)
    return data

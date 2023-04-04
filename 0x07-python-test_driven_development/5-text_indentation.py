#!/usr/bin/python3
'''
This is a '5-test_indentation' module, containing
'text_indentation(text)' function.
'''


def text_indentation(text):
    '''splits a text into lines'''
    if type(text) is not str:
        raise TypeError('text must be a string')
    flag = 0
    for i in text:
        if flag == 0:
            if i == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if i == '?' or i == '.' or i == ':':
                print(i)
                print()
                flag = 0
            else:
                print(i, end='')

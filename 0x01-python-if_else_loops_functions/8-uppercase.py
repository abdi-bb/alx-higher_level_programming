#!/usr/bin/python3
def uppercase(str):
    for item in str:
        ord(item)
        if item >= 97:
            item = item - 32
        print('{}'.format(chr(item)), end='')
    print('')

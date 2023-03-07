#!/usr/bin/python3
def uppercase(str):
    for item in str:
        ord(item)
        item = item - 32
        print('{}'.format(chr(item)), end='')
    print('')

#!/usr/bin/python3
def uppercase(str):
    for item in str:
        if ord(item) >= 97 and ord(item) <= 122:
            item = ord(item) - 32
        print('{}'.format(chr(item)), end='')
    print('')

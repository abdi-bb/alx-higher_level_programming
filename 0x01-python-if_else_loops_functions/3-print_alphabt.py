#!/usr/bin/python3
ascii_number = 97
while ascii_number <= 122:
    if chr(ascii_number) != 'q' and chr(ascii_number) != 'e':
        print('{}'.format(chr(ascii_number)), end='')
    ascii_number += 1

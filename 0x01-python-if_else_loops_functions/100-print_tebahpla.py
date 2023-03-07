#!/usr/bin/python3
for item in range(122, 64, -1):
    if item % 2 != 0:
        item -= 32
    print('{}'.format(chr(item)), end='')

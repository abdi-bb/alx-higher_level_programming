#!/usr/bin/python3

'''
Module name: '101-stats'
Functions:
    stats
'''


import sys

status_codes = {}
total_size = 0
count = 0

try:
    for line in sys.stdin:
        count += 1
        split_line = line.split()

        if len(split_line) == 7:
            file_size = int(split_line[6])
            status_code = int(split_line[5])

            total_size += file_size

            if status_code not in status_codes:
                status_codes[status_code] = 1
            else:
                status_codes[status_code] += 1

        if count % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(status_codes.keys()):
                print("{}: {}".format(code, status_codes[code]))

        if count % 50 == 0:
            status_codes = {}

except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

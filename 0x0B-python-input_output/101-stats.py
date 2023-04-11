#!/usr/bin/python3

'''
Module name: '101-stats'
Functions:
    stats
'''

import sys

total_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
line_count = 0

try:
    for line in sys.stdin:
        words = line.split()
        if len(words) > 6:
            status_code = words[8]
            file_size = words[9]
            total_size += int(file_size)
            if status_code in status_codes:
                status_codes[status_code] += 1
            line_count += 1
        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for code, count in sorted(status_codes.items()):
                if count > 0:
                    print("{}: {}".format(code, count))
            print("")

except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count)))

#!/usr/bin/python3

'''
Module name: '101-stats'
Functions:
    stats
'''


import sys

status_counts = {"200": 0, "301": 0, "400": 0, "
        401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

total_file_size = 0

line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()

        file_size = int(parts[-1])
        status_code = parts[-2]

        total_file_size += file_size
        if status_code in status_counts:
            status_counts[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print(f"File size: {total_file_size}")
            for code in sorted(status_counts.keys()):
                if status_counts[code] > 0:
                    print(f"{code}: {status_counts[code]}")

except KeyboardInterrupt:
    print(f"\nFile size: {total_file_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

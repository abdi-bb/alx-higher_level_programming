#!/usr/bin/python3

'''
Module name: '101-stats'
Functions:
    stats
'''

import sys
import signal


def signal_handler(signal, frame):
    print_stats()
    sys.exit(0)

def print_stats():
    total_file_size = sum(file_sizes)
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_codes.keys()):
        print(f"{status_code}: {status_codes[status_code]}")

file_sizes = []
status_codes = {}

signal.signal(signal.SIGINT, signal_handler)

for i, line in enumerate(sys.stdin):
    try:
        ip_address, _, _, _, status_code, file_size = line.strip().split()
        file_size = int(file_size)
        file_sizes.append(file_size)
        status_codes[status_code] = status_codes.get(status_code, 0) + 1
        if i % 10 == 9:
            print_stats()
    except ValueError:
        pass

print_stats()


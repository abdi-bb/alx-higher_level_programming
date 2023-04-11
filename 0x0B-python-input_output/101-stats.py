#!/usr/bin/python3

'''
Module name: '101-stats'
Functions:
    stats
'''


import sys
import signal


def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

total_file_size = 0
status_code_counts = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
        }


def print_stats():
    print(f"File size: {total_file_size}")
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{code}: {count}")


for i, line in enumerate(sys.stdin):
    ip, _, _, status_code, file_size = line.split()[0],
    line.split()[8], line.split()[10],
    line.split()[11], line.split()[12]
    total_file_size += int(file_size)
    status_code_counts[int(status_code)] += 1
    if (i+1) % 10 == 0:
        print_stats()

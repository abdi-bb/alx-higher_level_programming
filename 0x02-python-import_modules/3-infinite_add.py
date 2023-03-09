#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    arg_numbers = len(argv)
    sum = 0
    for item in range(1, arg_numbers):
        sum += int(argv[item])
    print(sum)

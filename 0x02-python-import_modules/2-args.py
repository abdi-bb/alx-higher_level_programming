#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    arg_numbers = len(argv) - 1
    if arg_numbers == 0:
        print("0 arguments.")
    elif arg_numbers == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_numbers))
    for item in range(arg_numbers):
        print("{}: {}".format(item + 1, argv[item + 1]))

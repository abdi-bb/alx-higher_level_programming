#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    arg_numbers = len(argv) 
    if arg_numbers == 1:
        print('0 arguments.')
    elif arg_numbers == 2:
        print('1 argument:')
    else:
        print('{} arguments:'.format(arg_numbers - 1))
    for item in range(1, arg_numbers):
        print('{}: {}'.format(item, argv[item]))

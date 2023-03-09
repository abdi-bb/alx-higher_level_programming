#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    from calculator_1 import add, sub, mul, div

    arg_numbers = len(argv)
    a = argv[1]
    b = argv[4]
    operator = argv[3]

    if arg_numbers != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    else:
        if operator == '+':
            print('{} + {} = {}'.format(a, b, add(a, b)))
            exit(0)
        elif operator == '-':
            print('{} - {} = {}'.format(a, b, sub(a, b)))
            exit(0)
        elif operator == '*':
            print('{} * {} = {}'.format(a, b, mul(a, b)))
            exit(0)
        elif operator == '/':
            print('{} / {} = {}'.format(a, b, div(a, b)))
            exit(0)
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)

#!/usr/bin/python3
def print_last_digit(number):
    return print(f'{abs(number) % 10}', end='') or abs(number) % 10


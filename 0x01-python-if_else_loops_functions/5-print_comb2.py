#!/usr/bin/python3
for item in range(0, 100):
    if item == 99:
        print(f'{item // 10}{item % 10}')
    else:
        print(f'{item // 10}{item % 10}', end=', ')


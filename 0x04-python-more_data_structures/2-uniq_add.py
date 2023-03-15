#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set(my_list)
    new_list = list(new_set)
    sum = 0
    for i in new_list:
        sum += i
    return sum


if __name__ == '__main__':
    uniq_add(my_list=[])

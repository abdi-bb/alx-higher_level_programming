#!/usr/bin/python3
from functools import reduce


def uniq_add(my_list=[]):
    result = set(my_list)
    result = list(result)
    result = reduce(lambda x, y: x + y, result)
    return result


if __name__ == '__main__':
    uniq_add(my_list=[])

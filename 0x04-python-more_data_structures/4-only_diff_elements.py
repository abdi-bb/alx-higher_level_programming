#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    li = list(((set_1.union(set_2)) - (set_1.inersection(set_2))))
    return li


if __name__ == '__main__':
    only_diff_elements(set_1, set_2=)

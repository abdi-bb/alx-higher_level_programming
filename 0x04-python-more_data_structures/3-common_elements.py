#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_set = list(set_1.intersection(set_2))

    return common_set


if __name__ == '__main__':
    common_elements(set_1, set_2)

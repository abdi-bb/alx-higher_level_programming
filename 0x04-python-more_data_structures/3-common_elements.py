#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_set = set_1.intersection(set_2)
    # for i in set_1:
        # if i in set_2:
            # common_set.append(i)
    return common_set


if __name__ == '__main__':
    common_elements(set_1, set_2)

#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    while my_list[count] and count < x:
        try:
            print('{:d}'.format(int(my_list[count]), end='')
                count += 1
        except (TypeError, IndexError):
            pass
    print()
    return count

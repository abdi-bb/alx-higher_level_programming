#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            dividend = my_list_1[i]
        except IndexError:
            print("out of range")
            dividend = 1
        try:
            divisor = my_list_2[i]
        except IndexError:
            print("out of range")
            divisor = 1
        try:
            division_result = dividend / divisor
            if division_result < 1:
                division_result = 0
        except ZeroDivisionError:
            print("division by 0")
            division_result = 0
        except TypeError:
            print("wrong type")
            division_result = 0
        result.append(division_result)
    return result

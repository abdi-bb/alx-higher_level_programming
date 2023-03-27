#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            x = my_list_1[i] if i < len(my_list_1) else 0
            y = my_list_2[i] if i < len(my_list_2) else 0
            if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
                raise TypeError("wrong type")
            elif y == 0:
                raise ZeroDivisionError("division by 0")
            else:
                result.append(x / y)
        except TypeError as e:
            print(e)
            result.append(0)
        except ZeroDivisionError as e:
            print(e)
            result.append(0)
        except IndexError as e:
            print("out of range")
            result.append(0)
    return result
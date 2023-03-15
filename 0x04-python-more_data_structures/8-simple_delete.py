#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary[key] != None:
        del a_dictionary[key]
    return a_dictionary


if __name__ == '__main__':
    simple_delete(a_dictionary, key="")

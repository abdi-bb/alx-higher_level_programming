#!/usr/bin/python3

if __name__ = '__main__':
    import hidden_4

    funcs = dir(hidden_4)
    for items in funcs:
        if items[:2] != '__':
            print(items)

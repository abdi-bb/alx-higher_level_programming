#!/usr/bin/env python3
'''
Module: '6-peak'
'''

def find_peak(list_of_integers):
    '''Returns a peak from a list of integers'''
    if not list_of_integers:
        return
    else:
        for i in range(len(list_of_integers) - 1):
            if list_of_integers[i] > list_of_integers[i + 1]:
                list_of_integers[i], list_of_integers[i + 1] = list_of_integers[i + 1], list_of_integers[i]

        return list_of_integers[i + 1]

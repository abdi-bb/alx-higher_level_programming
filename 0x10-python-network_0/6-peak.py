#!/usr/bin/env python3
'''
Module: '6-peak'
'''


def find_peak(list_of_integers):
    '''Returns a peak from a list of integers'''
    if not list_of_integers:
        return

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]

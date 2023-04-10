#!/usr/bin/python3

'''
module name: '1-my_list'
contained functions:
    MyList.print_sorted
'''


class MyList(list):
    '''Represents MyList'''
    def print_sorted(self):
        '''
        prints the sorted list
        '''
        print(sorted(self))

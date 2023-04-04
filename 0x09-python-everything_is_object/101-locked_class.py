#!/usr/bin/python3

'''Define a class LockedClass.'''


class LockedClass:
    '''Represent LockedClass'''
    def __setattr__(self, name, value):
        '''Sets attribute

        Args:
            name (str): name
            value (str): new name

        '''
        if ((name != 'first_name') and (not hasattr(self, 'first_name'))):
            raise AttributeError("'LockedClass' object has no attribute '{
                    }'".format(name))
        else:
            self.__dict__[name] = value

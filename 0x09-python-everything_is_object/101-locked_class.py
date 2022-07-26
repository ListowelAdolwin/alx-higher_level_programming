#!/usr/bin/python3
"""
Create a locked class

"""


class LockedClass:
    """
    A class that prevents the instanciation
    of attributes except for first_name

    """

    __slots__ = ['first_name']

    def __init__(self, first_name=''):
        """
        Initializes first_name
        """

        self.first_name = first_name

#!/usr/bin/python3
"""Class Square"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """Init class"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

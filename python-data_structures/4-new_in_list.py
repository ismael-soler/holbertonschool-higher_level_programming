#!/usr/bin/python3
from operator import ne


def new_in_list(my_list, idx, element):

    if idx < 0 or idx >= len(my_list):
        return my_list

    newList = my_list.copy()
    newList[idx] = element
    return newList

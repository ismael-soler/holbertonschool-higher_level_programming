#!/usr/bin/python3
"""" returns if the object is an instance of a  class """


def inherits_from(obj, a_class):
    """ checks the condition"""
    return isinstance(obj, a_class) and type(obj) is not a_class

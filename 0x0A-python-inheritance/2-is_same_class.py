#!/usr/bin/python3
""" Checks if an object is an instance of a class"""

def is_same_class(obj, a_class):
    """Function that checks if an object is a class instance"""
    return True if type(obj) == a_class else False

#!/usr/bin/python3

def safe_print_integer(value):
    """prints integer.

    Args:
        value (any): can be any type (integer, string, etc.)

    Return:
        A boolean
    """
    try:
        print("{:d}".format(value))
        return (True)
    except:
        return (False)

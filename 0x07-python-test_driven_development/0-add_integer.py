#!/usr/bin/python3
"""Add Integer Module"""

def add_integer(a, b=98):
    """A function that adds two integers
    Args:
        a (int, float): First integer
        b (int, float): Second integer

    Returns:
        int: The addition of both integers

    Raises:
        TypeError: If the parameters are not of expected types
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return (a + b)

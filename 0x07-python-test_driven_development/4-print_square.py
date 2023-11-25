#!/usr/bin/python3
"""Print Square Module"""

def print_square(size):
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    if isinstance(size, float):
        size = int(size)

    [print("#" * size) for i in range(size)]

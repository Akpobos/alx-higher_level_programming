#!/usr/bin/python3
def weight_average(my_list=[]):
    if not len(my_list):
        return (0)
    total = 0
    div = 0
    for s in my_list:
        total += s[0] * s[1]
        div += s[1]
    return (total / div)

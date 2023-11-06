#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length = len(my_list)

    if length == 0:
        return

    new_list = []
    for i in range(length):
        new_list.append(my_list[i] % 2 == 0)
    return new_list

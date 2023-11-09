#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    highest = {"key": "", "value": 0}
    for k, v in a_dictionary.items():
        if v > highest["value"]:
            highest = {"key": k, "value": v}
    return (highest["key"])

#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 0
    length = len(argv) - 1
    if length > 0:
        for j in range(length):
            i += int(argv[j + 1])
    print("{}".format(i))

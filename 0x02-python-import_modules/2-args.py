#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = len(sys.argv) - 1
    text = "arguments."
    if length > 0:
        if length == 1:
            text = text[:-2] + ":"
        else:
            text = text[:-1] + ":"
    print("{} {}".format(length, text))
    if length > 0:
        for i in range(length):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))

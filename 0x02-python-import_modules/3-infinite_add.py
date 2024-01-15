#!/usr/bin/python3
import sys


def addition():
    """ Function that print addition to all arguments"""
    result = 0

    # Looping through the argument inputed
    for i in sys.argv[1:]:
        result += int(i)

    print(result)


if __name__ == "__main__":
    addition()

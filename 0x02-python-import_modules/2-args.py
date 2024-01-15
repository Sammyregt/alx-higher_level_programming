#!/usr/bin/python3
import sys


def print_arguments():

    num_args = len(sys.argv) - 1  # Excluding the script name

    # print the number of arguments
    if num_args == 0:
        print("{} arguments.".format(num_args))
    elif num_args == 1:
        print("{} argument:".format(num_args))
    else:
        print("{} arguments:".format(num_args))

    # print the list of arguments
    for i in range(1, num_args + 1):
        print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    print_arguments()

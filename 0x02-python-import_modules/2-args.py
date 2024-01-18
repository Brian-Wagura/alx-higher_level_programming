#!/usr/bin/python3
import sys

if __name__ == '__main__':
    args = sys.argv[1:]
    num_args = len(args)

    if num_args == 0:
        print("Number of argument(s): 0.")
    elif num_args == 1:
        print("{} argument:".format(num_args))
        for i, arg in enumerate(args, start=1):
            print("{}: {}".format(i, arg))
    else:
        print("{} arguments:".format(num_args))
        for i, arg in enumerate(args, start=1):
            print("{}: {}".format(i, arg))

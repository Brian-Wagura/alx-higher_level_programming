#!/usr/bin/python3
import sys

if __name__ == '__main__':
    num = len(sys.argv) - 1

    if num == 1:
        print("{} argument.".format(num))
    elif num == 2:
        print("{} arguments:".format(num))
    else:
        print("{} arguments:".format(num))

    for i in range(1, num):
        print("{}:{}".format(i, sys.argv[i]))

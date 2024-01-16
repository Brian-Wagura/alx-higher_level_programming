#!/usr/bin/python3
for i in range(25, -1, -1):
    print("{0}{1}".format(chr(122 - 2*i), chr(89 - 2*i)), end="")

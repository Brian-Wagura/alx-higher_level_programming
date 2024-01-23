#!/usr/bin/python3
def magic_calculation(a, b):
    add = magic_calculation_102.__dict__['add']
    sub = magic_calculation_102.__dict__['sub']
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)

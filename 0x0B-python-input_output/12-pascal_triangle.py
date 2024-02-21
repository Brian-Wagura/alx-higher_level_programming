#!/usr/bin/python3
"""
Defines a Pascal's triangle
"""


def pascal_triangle(n):
    """
    Represents Pascal's traingle of size n
    Returns: a list of lists of integers representing the Pascal’s triangle
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

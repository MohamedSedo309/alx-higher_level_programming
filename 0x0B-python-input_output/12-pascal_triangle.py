#!/usr/bin/python3

"""
Create a function def pascal_triangle(n):
that returns a list of lists of integers
representing the s triangle of n
"""


def pascal_triangle(n):
    """create Pascal's Triangle class of size n.

    Returns a list of lists of integers making the triangle
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        triangl = triangles[-1]
        tmp = [1]
        for i in range(len(triangl) - 1):
            tmp.append(triangl[i] + triangl[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return trianglesPascal

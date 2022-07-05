#!/usr/bin/python3
""" Pascal triangle """


def pascal_triangle(n):
    """ Pascal triangle """
    if n <= 0:
        return []

    tri = [[1]]
    while len(tri) != n:
        t = tri[-1]
        x = [1]
        for i in range(len(t) - 1):
            x.append(t[i] + t[i + 1])
        x.append(1)
        tri.append(x)
    return tri

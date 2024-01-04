#!/usr/bin/python3
"""
script for the function def
"""


def pascal_triangle(n):
    "function to implement the pascal triangle"
    if (n <= 0):
        return ([])

    list = [1]

    pascal_list = []
    pascal_list.append(list)

    if (n == 1):
        return (pascal_list)

    for i in range(2, n+1):
        new_list = []
        for j in range(len(list)):
            if (j == 0):
                new_list.append(0 + list[0])
            if (j == len(list) - 1):
                new_list.append(0 + list[len(list) - 1])
            else:
                new_list.append(list[j] + list[j + 1])
        list = new_list
        pascal_list.append(new_list)

    return (pascal_list)

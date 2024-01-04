#!/usr/bin/python3

def pascal_triangle(n):
    if (n <= 0):
        return ([])

    list = [1]
    if (n == 1):
        return (list)

    pascal_list = []
    pascal_list.append(list)
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

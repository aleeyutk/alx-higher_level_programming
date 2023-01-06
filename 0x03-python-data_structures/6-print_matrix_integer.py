#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    for i in matrix:
        for n in i:
            if n == i[-1]:
                print("{:d}".format(n))
            else:
                print("{:d}".format(n), end=" ")

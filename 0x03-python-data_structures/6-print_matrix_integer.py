#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for vector in matrix:
        for number in vector:
            print("{:d}".format(number), end=" ")
        print("\n")

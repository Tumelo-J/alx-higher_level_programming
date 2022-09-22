#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for vector in matrix:
        for i, number in enumerate(vector):
            print("{:d}".format(number), end=" " if (i + 1) % len(vector) else "\n")

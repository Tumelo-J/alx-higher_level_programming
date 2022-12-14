#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
        return
    for vector in matrix:
        columns = len(vector)
        for i, number in enumerate(vector):
            str_ = "{:d}".format(number)
            print(str_, end="\n" if not (i + 1) % columns else " ")

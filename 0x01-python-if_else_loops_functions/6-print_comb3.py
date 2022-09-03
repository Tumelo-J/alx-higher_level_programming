#!/usr/bin/python3
number = 0
inc = 2
while number <= 89:
    if number % 10 == 0 and number not in [0, 1]:
        number += inc
        inc += 1
    print("{:02d}".format(number), end=", " if number != 89 else "\n")
    number += 1

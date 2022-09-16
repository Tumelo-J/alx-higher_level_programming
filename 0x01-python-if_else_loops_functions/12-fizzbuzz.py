#!/usr/bin/python3

def fizzbuzz():
    for n in range(1, 101):
        if (n % 3 == 0 and n % 5 == 0):
            print("FizzBuzz", end=" ")
        elif not n % 3:
            print("Fizz", end=" ")
        elif not n % 5:
            print("Buzz")
        else:
            print(n, end=" ")

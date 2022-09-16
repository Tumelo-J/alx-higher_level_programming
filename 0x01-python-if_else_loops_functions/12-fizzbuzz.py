#!/usr/bin/python3

def fizzbuzz():
    for n in range(1, 101):
        if not (n % 3 and n % 5):
            print("FizzBuzz", end=" ")
        elif not n % 3:
            print("Fizz", end=" ")
        elif not n % 5:
            print("Buzz")
        else:
            print(n, end=" ")

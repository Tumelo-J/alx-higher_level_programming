#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as c1

    a = 10
    b = 5

    print(f"{a} + {b} = {c1.add(a, b)}")
    print(f"{a} - {b} = {c1.sub(a, b)}")
    print(f"{a} * {b} = {c1.mul(a, b)}")
    print(f"{a} / {b} = {c1.div(a, b)}")

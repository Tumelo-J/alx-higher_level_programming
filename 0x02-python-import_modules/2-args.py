#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n_args = len(sys.argv) - 1
    if n_args > 1:
        print(f"{n_args} arguments:")
        [print(f"{i}: {sys.argv[i]}") for i in range(1, n_args + 1)]
    elif n_args == 1:
        print(f"{n_args} argument:")
        print(f"1: {sys.argv[1]}")
    else:
        print("0 arguments.")

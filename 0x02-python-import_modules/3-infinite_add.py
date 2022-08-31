#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    s = sum([int(item) for item in sys.argv[1:]])
    print(s)

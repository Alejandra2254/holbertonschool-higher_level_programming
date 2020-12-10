#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg = len(argv)
    n = 1
    num = 0
    if arg == 2:
        print("1 argument.")
    else:
        print("{:d} arguments.".format(arg - 1))
    while arg != n:
        n += 1
        print("{:d}: {:s}".format(n - 1, str(argv[n - 1])))

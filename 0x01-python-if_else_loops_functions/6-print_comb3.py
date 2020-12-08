#!/usr/bin/python3
for n in range(0, 10):
    for j in range(0, 10):
        if n < j and n != 8:
            print('{:d}{:d}, '.format(n, j), end='')
        if n < j and n == 8:
            print('{:d}{:d}'.format(n, j))

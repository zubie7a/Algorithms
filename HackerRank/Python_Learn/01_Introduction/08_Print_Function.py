# https://www.hackerrank.com/challenges/python-print
from __future__ import print_function
if __name__ == '__main__':
    # For a given n, print all the numbers 1234567...n without string methods.
    n = int(raw_input())
    arr = [i for i in range(1, n + 1)]
    print(*arr, sep="")

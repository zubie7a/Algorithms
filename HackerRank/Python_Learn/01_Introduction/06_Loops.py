# https://www.hackerrank.com/challenges/python-loops
from __future__ import print_function
if __name__ == '__main__':
    n = int(raw_input())
    arr = [i**2 for i in range(n)]
    print(*arr, sep="\n")

# https://www.hackerrank.com/challenges/python-arithmetic-operators
from __future__ import print_function
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(*[a + b, a - b, a * b], sep="\n")

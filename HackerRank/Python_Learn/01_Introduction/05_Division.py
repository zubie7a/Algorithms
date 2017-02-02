# https://www.hackerrank.com/challenges/python-division
from __future__ import division, print_function
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    # // is integer division, / is float division, from Python 3.0
    print(*[a//b, a/b], sep="\n")
# https://www.hackerrank.com/challenges/symmetric-difference
from __future__ import print_function
n = int(raw_input())
setA = set(map(int, raw_input().split()))
m = int(raw_input())
setB = set(map(int, raw_input().split()))
# Print the symmetric difference of two sets.
setC = setA ^ setB
print(*sorted(setC), sep="\n")

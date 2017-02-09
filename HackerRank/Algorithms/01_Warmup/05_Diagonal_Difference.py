# https://www.hackerrank.com/challenges/diagonal-difference
n = int(raw_input())
d1, d2 = 0, 0
# Print the absolute difference of the sum of the diagonals
# on an n*n matrix.
for i in range(n):
    line = raw_input().split()
    d1 += int(line[i])
    d2 += int(line[-(i+1)])
print abs(d1 - d2)

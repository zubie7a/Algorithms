# https://www.hackerrank.com/challenges/ctci-array-left-rotation
from __future__ import print_function
# Do a left rotation of an array.
n, k = map(int, raw_input().split())
nums = map(int, raw_input().split())
# Input:
# 5 4
# 1 2 3 4 5
# Output:
# 5 1 2 3 4
arr = [0 for i in range(len(nums))]

k %= n
for i in range(len(nums)):
    arr[(n - k + i) % n] = nums[i]
    
print(*arr, sep=" ")

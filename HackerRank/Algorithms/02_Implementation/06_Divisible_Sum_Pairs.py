# https://www.hackerrank.com/challenges/divisible-sum-pairs
n, k = map(int, raw_input().split())
nums = map(int, raw_input().split())
res = 0
# In a list of numbers, print the amount of n_i, n_j such
# that i < j and both numbers are evenly divisible by k.
for i in range(n):
    for j in range(i + 1, n):
        res += ((nums[i] + nums[j]) % k) == 0
print res

# https://www.hackerrank.com/challenges/ctci-lonely-integer

# X^X == 0
# Y^0 == Y (1^0 == 1, 0^0 == 0, 1^1 == 0, 0^1 == 1)
# X^Y^X == Y
# This is because XOR is commutative, to that'd be equal to
# (X^X)^Y
# Applying this  to all numbers will cause all duplicates by
# pairs to cancel out, and leave just the one happening once.
def findLonely(nums):
    # Reduce will apply a function to a cumulative value
    # and the next value from an iterable.
    return reduce(lambda x,y: x^y, nums)

# n: 9
# nums: 4 9 95 93 57 4 57 93 9
# find the integer that occurs only once.
n = int(raw_input())
nums = map(int, raw_input().split())
print findLonely(nums)

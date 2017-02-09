# https://www.hackerrank.com/challenges/mini-max-sum
# A list of numbers.
nums = map(int, raw_input().split())
# The sum of all those numbers.
total = sum(nums)
minN, maxN = float('inf'), float('-inf')
# Find the lowest possible sum, and the highest possible sum
# of all the numbers in the list, but the condition is that
# one number must be skipped.
for num in nums:
    # So keep finding the minimum and the maximum sum by
    # substracting each number of the list from the total sum.
    minN = min(minN, total - num)
    maxN = max(maxN, total - num)
print minN, maxN

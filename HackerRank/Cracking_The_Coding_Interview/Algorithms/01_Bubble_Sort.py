# https://www.hackerrank.com/challenges/ctci-bubble-sort
n = int(raw_input())
nums = map(int, raw_input().split())
swaps = 0
# Bubble sort: iterate N times, swapping elements shifting the
# bigger ones to the right.
for i in xrange(n):
    for j in xrange(n - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            swaps += 1

print "Array is sorted in %d swaps." % swaps
print "First Element: %d" % nums[0]
print "Last Element: %d" % nums[-1]
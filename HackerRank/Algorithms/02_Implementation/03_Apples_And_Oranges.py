# https://www.hackerrank.com/challenges/apple-and-orange
# A house has boundaries [s, t] on a line.
s, t = map(int, raw_input().split())
# Two trees have locations a and b on a line.
a, b = map(int, raw_input().split())
# m apples fall from tree a, n oranges fall from tree b.
m, n = map(int, raw_input().split())
# The distances the fruits fell off from their respective trees.
# A negative distance means falling to the left, a positive one
# means falling to the right.
apples = map(int, raw_input().split())
oranges = map(int, raw_input().split())
# For each apple check if it landed in the house range.
fallA = [s <= a + apples[i] <= t for i in range(m)]
# For each orange check if it landed in the house range.
fallB = [s <= b + oranges[j] <= t for j in range(n)]
print sum(fallA)
print sum(fallB)

# https://www.hackerrank.com/challenges/sock-merchant
from collections import Counter
n = int(raw_input())
# For n socks, there will be n colors identified by
# an integer id, which may be repeated colors.
colors = Counter(map(int, raw_input().split()))
# Print how many pairs can be formed with these colors.
print sum([count/2 for count in colors.values()])

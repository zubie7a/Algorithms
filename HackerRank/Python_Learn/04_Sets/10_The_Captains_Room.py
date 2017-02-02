# https://www.hackerrank.com/challenges/py-the-captains-room
k = int(raw_input())
vals = map(int, raw_input().split())
uniq = set(vals)
# K: 5
# Values: 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
# All values happen 5 times, except for one which only happens once.
# Which is the unique one?
# ...
# k * sum(uniq): the sum of all distinct numbers if they all happened k times.
# sum(vals): the real sum of all numbers, all happen k times except one.
# The difference should be the "unique" value, (k - 1) times.
# Divide by (k - 1) to obtain that value.
room = (k * sum(uniq) - (sum(vals))) / (k - 1)
print room

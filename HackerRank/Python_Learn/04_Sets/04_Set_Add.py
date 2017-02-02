# https://www.hackerrank.com/challenges/py-set-add
n = int(raw_input())
setZ = set([])
# Add elements to a set.
for i in range(n):
    setZ.add(raw_input())
print len(setZ)

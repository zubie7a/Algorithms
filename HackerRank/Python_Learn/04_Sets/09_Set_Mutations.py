# https://www.hackerrank.com/challenges/py-set-mutations
n = int(raw_input())
setA = set(map(int, raw_input().split()))
m = int(raw_input())
for i in range(m):
    line = raw_input().split()
    if line[0] == "update":
        setB = set(map(int, raw_input().split()))
        setA |= setB
    if line[0] == "intersection_update":
        setB = set(map(int, raw_input().split()))
        setA &= setB
    if line[0] == "symmetric_difference_update":
        setB = set(map(int, raw_input().split()))
        setA ^= setB
    if line[0] == "difference_update":
        setB = set(map(int, raw_input().split()))
        setA -= setB
print sum(setA)

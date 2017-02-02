# https://www.hackerrank.com/challenges/py-set-intersection-operation
n = int(raw_input())
setA = set(map(int, raw_input().split()))
m = int(raw_input())
setB = set(map(int, raw_input().split()))
# print len(setA & setB)
print len(setA.intersection(setB))

# https://www.hackerrank.com/challenges/no-idea
n, m = map(int, raw_input().split())
arr = map(int, raw_input().split())
setA = set(map(int, raw_input().split()))
setB = set(map(int, raw_input().split()))
# Add 1 per value from array in setA, Substract 1 per value from array in setB.
happiness = sum([(arr[i] in setA) - (arr[i] in setB) for i in range(n)])
print happiness
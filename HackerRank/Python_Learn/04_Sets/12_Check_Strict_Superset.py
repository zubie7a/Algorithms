# https://www.hackerrank.com/challenges/py-check-strict-superset
setA = set(map(int, raw_input().split()))
n = int(raw_input())
# Check if setA is a strict superset of all the inputted sets.
print all([set(map(int, raw_input().split())) < setA for _ in range(n)])

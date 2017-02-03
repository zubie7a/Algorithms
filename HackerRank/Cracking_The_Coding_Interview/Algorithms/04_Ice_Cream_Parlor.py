# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor
from __future__ import print_function
from collections import defaultdict

for _ in xrange(int(raw_input())):
    m, n = int(raw_input()), int(raw_input())
    costs = map(int, raw_input().split())
    d = defaultdict(lambda: [])
    for i in range(n):
        # Each cost value will have associated a list of incremental ids.
        d[costs[i]].append(i + 1)
    
    for (costA, idsA) in d.items():
        # costB + costA must be equal to m.
        costB = m - costA
        # Since its a defaultdict, if costB doesn't exist, then returns [].
        idsB = d[costB]
        # If result has one element and costs are distinct.
        if len(idsB) == 1 and costA != costB:
            print(*sorted(idsA + idsB), sep=" ")
            break
        # If result has two elements and costs are equal.
        elif len(idsB) == 2 and costA == costB:
            print(*sorted(idsB), sep=" ")
            break

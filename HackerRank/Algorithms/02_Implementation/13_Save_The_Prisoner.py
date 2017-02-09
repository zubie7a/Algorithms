# https://www.hackerrank.com/challenges/save-the-prisoner
t = int(raw_input())
for _ in xrange(t):
    n, m, s = map(int, raw_input().split())
    # s-1: converting to 0-indexed.
    # m-1: because the first candy will be eaten by (s-1)
    # add those two to see the position where the poisoned
    # candy will land.
    # mod n: because it may wrap around.
    # +1: converting back from 0-indexed to 1-indexed.
    print (((s-1) + (m-1)) % n) + 1

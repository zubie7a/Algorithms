# https://www.hackerrank.com/challenges/ctci-recursive-staircase

# For a given length, store the amount of combinations possible
# from there onwards, so that it doesn't have to be computed
# again, in case another combination has a segment with this
# same length which is sure to have the same amount of combs.
cache = {}

# n: the remaining length of the staircase.
def combinations(n):
    if n == 0: # arrived just at the end of staircase.
        return 1 
    if n < 0: # exceeded the length, not valid.
        return 0
    if not cache.get(n):
        # Jump in the staircase by 1, 2 or 3 length leaps.
        amount = sum([combinations(n - i) for i in xrange(1,4)])
        cache[n] = amount
    return cache[n]
    
for _ in range(int(raw_input())):
    print combinations(int(raw_input()))

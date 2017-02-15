# https://codefights.com/arcade/intro/level-4/xYXfzQmnhBvEKJwXP
from collections import Counter
def areSimilar(A, B):
    c = Counter([])
    # Two arrays are similar if they can be formed by swapping at
    # most one element. Figure out if two arrays are similar.
    for i in range(len(A)):
        a, b = A[i], B[i]
        if a != b:
            a, b = sorted([a, b])
            c[(a,b)] += 1
    if len(c.items()) == 0:
        return True
    return max(c.values()) == 2 and len(c.values()) == 1

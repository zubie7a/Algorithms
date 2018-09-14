# https://app.codesignal.com/arcade/intro/level-4/xYXfzQmnhBvEKJwXP
from collections import Counter

def areSimilar(A, B):
    c = Counter([])
    # Two arrays are similar if they can be formed by swapping at
    # most one element. Figure out if two arrays are similar.
    for i in range(len(A)):
        # Get the elements at the same position in both arrays.
        a, b = A[i], B[i]
        # If the values are different...
        if a != b:
            a, b = sorted([a, b])
            # Store them as a unique different tuple.
            c[(a, b)] += 1
    # If there were no different tuples, they are similar.
    if len(c.items()) == 0:
        return True

    # If there were tuples, there should be at most one,
    # occurring at most twice (because of the two elements
    # that could've been switched)
    return max(c.values()) == 2 and len(c.values()) == 1

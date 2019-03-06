# https://app.codesignal.com/arcade/code-arcade/well-of-integration/xYXfzQmnhBvEKJwXP
def areSimilar(a, b):
    # Two arrays are called similar if one of them can be obtained by swapping at
    # most one pair of elements in the other. Are `a` and `b` similar?

    # Store the indices where stuff is different respectively.
    diff = []
    for idx in range(len(a)):
        if a[idx] != b[idx]:
            diff.append(idx)

    # If everything is equal then no swaps are necessary.
    if len(diff) == 0:
        return True

    # Now check that there's only a couple places where stuff isn't equal.
    # If more than 2 or just 1, there can't be a single-swap.
    if len(diff) != 2:
        return False

    idx_1, idx_2 = diff
    return a[idx_1] == b[idx_2] and a[idx_2] == b[idx_1]

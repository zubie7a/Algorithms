# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/hBw5BJiZ4LmXcy92u/
def countSumOfTwoRepresentations2(n, l, r):
    # Check how much possible combinations of values strictly
    # between l and r inclusive can be added up to n.
    pairs = set([])
    for value1 in range(l, r + 1):
        value2 = n - value1
        if l <= value2 and value2 <= r:
            # Put stuff in a set to keep only ordered unique occurrences.
            value1, value2 = list(sorted([value1, value2]))
            pairs.add((value1, value2))

    return len(pairs)

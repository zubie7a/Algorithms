# https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/6SLJChm9N3fEgr2R7/solutions
def equalPairOfBits(n, m):
    # Same as the position of rightmost different pair of bits, but when
    # we negate the mutually exclusive, we are instead turning on equal
    # values on both sides, but the rest of the logic applies the same.
    return ~(m ^ n) & ~(~(m ^ n) - 1)

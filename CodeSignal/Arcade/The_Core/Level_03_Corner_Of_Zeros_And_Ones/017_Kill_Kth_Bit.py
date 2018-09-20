# https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/b5z4P2r2CGCtf8HCR
def killKthBit(n, k):
    # Use bit operators to turn off the k-th bit from the right.
    # First create a value with the bit at the position turned on
    # and everything else off. Then flip that value so all bits
    # are 1 except the one in position. Then, 'bitwise and' with
    # this value will leave all bits untouched except the one in
    # the desired position.
    return n & ~(1 << (k - 1))

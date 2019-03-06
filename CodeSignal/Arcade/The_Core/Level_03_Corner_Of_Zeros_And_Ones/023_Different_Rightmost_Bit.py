# https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/whz5JzszYTdXW6aNA/
def differentRightmostBit(n, m):
    # Whats the value of the different rightmost bit?
    # Regular string operations:
    # 1. Do n XOR m, so the resulting value will have ones only in the positions
    # where the bits are mutually exclusive.
    # 2. Convert to a binary string and invert it so we can count from left, which
    # in binary we do that anyway because we count from right but starting with the
    # index 0 at the right, so if we invert the string and keep counting 0 from the
    # left is the same.
    # 3. Find the location of the first one (first different bit), and return 2 to
    # the power of that index.
    return 2 ** bin(n ^ m)[2:][::-1].find("1")
    # Now interesting bitwise operations:
    # 1. Do the mutually exclusive bits to turn on bits at differing positions.
    #
    #  30 = 0011110
    #  78 = 1001110
    #  ------------
    #       1010000
    #
    # 2. Now substract 1 to the mutual exclusive value. From the right, all the
    # values that were the same will be 0 in the mutual exclusive, and the first
    # different will be 1, so it will have a form of 1[0]* and substracting one
    # from that will cause the rightmost different bit to be turned off and all
    # the following equal ones to be turned on.
    #
    #  (":" is the split point of rightmost different)
    #  10:10000 - 1 = 10:01111
    #
    # 3. Now negate that value. The different bit will again be on, everything
    # to its right will be off, but now everything to the left of the different
    # bit will be the opposite of the mutual exclusive.
    #
    #   ~1001111 = 0110000
    #
    # 4. The result of `logical and` with the original mutual exclusive will be
    # a value in which all values are 0s, but there will be a 1 at the rightmost
    # differing position. So with all 0s to the right they will be turned off with
    # 'bitwise and', and with all opposite of the mutually exclusive to the left
    # they will also be turned off with 'bitwise and'.
    #
    #    1010000
    #    0110000
    #    -------
    #    0010000 = 16
    #
    return (n ^ m) & ~((n ^ m) - 1)

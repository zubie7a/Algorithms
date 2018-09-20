# https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/dShYZZT4WmvpmfpgB/
import re

def swapAdjacentBits(n):
    # With regexes and string operators:
    # 1. Convert string to binary, then fill up to 32 bit digits with 0s.
    # 2. Split by pairs of elements.
    # 3. Flip each pair of elements.
    # 4. Join that together in a string.
    # 5. Convert back to int.
    return int("".join(map(lambda x: x[::-1], re.findall(r'.{2}', bin(n)[2:].zfill(32)))), 2)
    # Now this is even more interesting and bit wise:
    # 1. 5 in binary is 0101, so 5 in hex 0x5 is 0x0101.
    # 2. 10 in binary is 1010, so 10/A in hex 0xA is 0x1010.
    # 3. Notice them that 0x555555555 and 0xAAAAAAAAA are values which binary
    # representations are alternating 1s and 0s.
    # 4. Rightshifting n by 1, and then 'bitwise and' will cause bits in even
    # positions of n to be compared with 0s in even positions of mask and 1s
    # in odd positions of mask, making them "on" at odd positions if the bits
    # at even positions of n were 1, but turning off always the bits at odd
    # positions of n.
    #  
    # n =    01101100000(1) rightshift
    # 0x5... 10101010101
    #        -----------
    # b1 =   00101000000
    #
    # 4. Leftshifting n by 1, and then 'bitwise and' will cause bits in odd
    # positions of n to be compared with 0s in odd positions of mask and 1s
    # in even positions of mask, making them "on" at even positions if the
    # bits at odd positions of n were 1, but turning off always the bits at
    # even positions of n.
    #
    #
    # n =    011011000001(0) leftshift
    # 0xA... 010101010101 0
    #        --------------
    # b2 =   010001000001 0
    #
    # 6. When we apply 'bitwise or' to these two values, we've effectively
    # merge those two previous values, one in which odd positions have the
    # values from even positions of n and even positions are cleared, and
    # another in which even positions have the values from odd positions of
    # n and odd positions are cleared.
    #
    # b1 =   --00101000000 
    # b2 =   0100010000010
    #        -------------
    #        0100111000010
    #       bits are swapped!
    #        0011011000001
    #
    return (n >> 1) & 0x555555555 | (n << 1) & 0xAAAAAAAAA

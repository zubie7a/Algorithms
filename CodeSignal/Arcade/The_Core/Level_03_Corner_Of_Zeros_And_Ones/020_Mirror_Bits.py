# https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/e3zfPNTwTa9qTQzcX
def mirrorBits(a):
    # Reverse the order of the bits in a given integer.
    # 1. Convert to a binary string with bin(), but mind that it
    # will start with "0b" so remove that.
    # 2. Reverse the string.
    # 3. Convert the result back to int giving source base as 2.
    return int("".join(reversed(bin(a)[2:])), 2)

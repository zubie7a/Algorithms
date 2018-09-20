# https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/9nSj6DgqLDsBePJha
def secondRightmostZeroBit(n):
    # Iterate up to log2(n) (num binary digits) then rightshift by that length
    # and check if last digit is a 0, if so store the index.
    return 2 ** [i for i in range(math.ceil(math.log(n, 2))) if (n>>i) % 2 == 0][1]
    # The same but doing the length with string operations.
    return 2 ** [i for i in range(len(bin(n)[2:])) if (n>>i) % 2 == 0][1]
    # Now everything is using string operations.
    return 2 ** (int([i for i in range(len(bin(n))) if bin(n)[::-1][i] == '0'][1]))

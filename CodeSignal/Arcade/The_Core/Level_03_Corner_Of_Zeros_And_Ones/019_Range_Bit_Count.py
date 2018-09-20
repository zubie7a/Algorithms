# https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/eC2Zxu5H5SnuKxvPT
def rangeBitCount(a, b):
    # 0 <= a <= b. Construct an array of integers from a to b inclusive.
    # Count the amount of 1s in such array's values binary representations.
    binaries = [ "{:b}".format(i) for i in range(a, b + 1) ]
    # In nested loops, for every binary string iterate over its characters, then
    # convert such characters into ints and add them up, first will return the
    # sum for each individual string, and then all sums will be added for total.
    ones = sum([ sum([ int(char) for char in binary ]) for binary in binaries ])

    # Much simpler way, make use of bin operator and count function over strings:
    ones = sum([ bin(num).count("1") for num in range(a, b + 1)])

    return ones

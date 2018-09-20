# https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/KeMqde6oqfF5wBXxf
def arrayPacking(arr):
    # You are given an array of up to four non-negative integers, all less than
    # 256 (so they fit in 8 bits). Pack these integers into one number M (so max
    # 64 bits) occupying the bits from the start.

    # The more manual way: convert to binary string, concatenate them and then convert
    # back to base 10 integer at the end.
    # value = ""
    # for num in arr:
    #    value = "{0:08b}".format(num) + value
    # return int(value, 2)

    # The bitwise way: use bit operators to shift every number further to the left
    # and then 'bitwise or' to turn those bits on, effectively concatenating them.
    value = 0
    for i in range(len(arr)):
        num = arr[i]
        num <<= (i * 8)
        value |= num

    return value

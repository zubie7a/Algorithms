# https://app.codesignal.com/arcade/code-arcade/list-forest-edge/3LmZafR9wMCWpdgra
import math

def isSmooth(arr):
    # An array is smooth if its first and last elements are the same as middle.
    # Middle is the middle element if length is odd, and the sum of the two
    # middle elements if the length is even.
    middle = arr[len(arr) // 2]
    if len(arr) % 2 == 0:
        middle += arr[len(arr) // 2 - 1]

    return arr[0] == middle and middle == arr[-1]

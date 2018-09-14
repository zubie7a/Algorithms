# https://app.codesignal.com/arcade/intro/level-8/3AgqcKrxbwFhd3Z3R
def extractEachKth(input_array, k):
    # Remove every k-th element from the array (1-indexed).
    # arr = input_array[:]
    # return [arr[i] for i in range(len(arr)) if (i+1) % k != 0]
    # Now, with some python wizardry...
    del input_array[k-1::k]
    return input_array

# https://codefights.com/arcade/intro/level-8/3AgqcKrxbwFhd3Z3R
def extractEachKth(inputArray, k):
    # Remove every k-th element from the array (1-indexed).
    # arr = inputArray[:]
    # return [arr[i] for i in range(len(arr)) if (i+1) % k != 0]
    del inputArray[k-1::k]
    return inputArray
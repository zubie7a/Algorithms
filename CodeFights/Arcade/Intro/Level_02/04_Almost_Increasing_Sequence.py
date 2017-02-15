# https://codefights.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG
def almostIncreasingSequence(sequence):
    outOfPlace = 0
    # Check if a sequence can be made strictly increasing by
    # removing at most one element from it.
    for i in range(1,len(sequence)):
        if sequence[i] <= sequence[i-1]:
            outOfPlace += 1
    return outOfPlace <= 1

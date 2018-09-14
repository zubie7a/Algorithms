# https://app.codesignal.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG
def almostIncreasingSequence(sequence):
    out_of_place = 0
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            out_of_place += 1
        if i+2 < len(sequence) and sequence[i] >= sequence[i + 2]:
            out_of_place += 1

    return c < 3

# https://codefights.com/arcade/intro/level-2/bq2XnSr5kbHqpHGJC
def makeArrayConsecutive2(statues):
    statues = sorted(statues)
    res = 0
    # Make elements of the array be consecutive. If there's a
    # gap between two statues heights', then figure out how
    # many extra statues have to be added.
    for i in range(1, len(statues)):
        res += statues[i] - statues[i-1] - 1
    return res

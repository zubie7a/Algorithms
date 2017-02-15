# https://codefights.com/arcade/intro/level-5/EEJxjQ7oo7C5wAGjE
def arrayMaximalAdjacentDifference(inputArray):
    maxDiff = float('-inf')
    for i in range(len(inputArray) - 1):
        diff = abs(inputArray[i] - inputArray[i+1])
        maxDiff = max(maxDiff, diff)
    return maxDiff

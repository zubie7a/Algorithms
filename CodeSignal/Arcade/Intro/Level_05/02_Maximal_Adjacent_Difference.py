# https://app.codesignal.com/arcade/intro/level-5/EEJxjQ7oo7C5wAGjE
def arrayMaximalAdjacentDifference(input_array):
    # Find the maximal absolute difference between any to adjacent elements.
    max_diff = float('-inf')
    for i in range(len(input_array) - 1):
        diff = abs(input_array[i] - input_array[i + 1])
        max_diff = max(max_diff, diff)

    return max_diff

# https://codefights.com/arcade/intro/level-8/Rqvw3daffNE7sT7d5
def arrayMaxConsecutiveSum(input_array, k):
    # Given an array of integers, find the maximal possible sum of some of
    # its k consecutive elements.
    sums = [0] + input_array[:]
    # sums = [sums[i] + sums[i - 1] for i in range(1, len(input_array))]
    # First, cache the total sums up to a certain point. Then to find a
    # sum between a range, substract the accumulate up to the range points.
    for i in range(1, len(sums)):
        sums[i] += sums[i - 1]
    max_k_sum = float('-inf')
    # Iterate over the cache'd sums...
    for i in range(k, len(sums)):
        # Checking whats the max sum between each possition and the accumulate
        # k positions earlier, meaning the summing values in between.
        max_k_sum = max(max_k_sum, sums[i] - sums[i - k])

    return max_k_sum

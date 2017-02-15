# https://codefights.com/arcade/intro/level-8/Rqvw3daffNE7sT7d5
def arrayMaxConsecutiveSum(inputArray, k):
    sums = [0] + inputArray[:]
    # sums = [sums[i] + sums[i-1] for i in range(1, len(inputArray))]
    for i in range(1, len(sums)):
        sums[i] += sums[i-1]
    maxSum = float('-inf')
    for i in range(k,len(sums)):
        maxSum = max(maxSum, sums[i]-sums[i-k])
    return maxSum

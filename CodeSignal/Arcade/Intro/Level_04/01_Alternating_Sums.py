# https://app.codesignal.com/arcade/intro/level-4/cC5QuL9fqvZjXJsW9
from functools import reduce

def alternatingSums(nums):
    n = len(nums)
    # Create a list of tuples in which the first element will only
    # contain the weights of the even positions and the second element
    # will only contain the weights of the odd positions.
    res = [(nums[i]*(not (i % 2)), nums[i]*(i % 2)) for i in range(n)]
    # Now accumulate up all the tuples, thus only weights from even
    # positions will be summed with each other, same for odd positions.
    res = reduce(lambda x, y: (x[0]+y[0], x[1]+y[1]), res)

    # Convert the final tuple to a list.
    return list(res)

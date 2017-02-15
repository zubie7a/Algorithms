# https://codefights.com/arcade/intro/level-4/cC5QuL9fqvZjXJsW9
def alternatingSums(nums):
    n = len(nums)
    # Add the odd-index items and the even-index items.
    res = [(nums[i]*(not (i % 2)), nums[i]*(i % 2)) for i in range(n)]
    res = reduce(lambda x, y: (x[0]+y[0], x[1]+y[1]), res)
    return list(res)

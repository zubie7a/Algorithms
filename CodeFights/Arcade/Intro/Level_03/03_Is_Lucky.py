# https://codefights.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ
def isLucky(n):
    # Find whether a number is lucky, that is, the sum of the
    # left half is equal to the sum of the right half.
    n = str(n)
    left, right = 0, 0
    for i in range(len(n)//2):
        left += int(n[i])
    for i in range(len(n)//2, len(n)):
        right += int(n[i])
    return left == right

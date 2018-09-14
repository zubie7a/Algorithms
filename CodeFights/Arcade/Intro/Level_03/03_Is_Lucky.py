# https://app.codesignal.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ
def isLucky(n):
    # Find whether a number is lucky, that is, the sum of the
    # left half is equal to the sum of the right half.
    # Convert the number to string for easy splitting.
    n = str(n)
    mid = len(n) // 2
    left, right = n[:mid], n[mid:]
    left_sum = sum(map(int, left))
    right_sum = sum(map(int, right))
    # return left_sum == right_sum
    return sum([int(i) for i in n[:mid]]) == sum(int(i) for i in n[mid:])

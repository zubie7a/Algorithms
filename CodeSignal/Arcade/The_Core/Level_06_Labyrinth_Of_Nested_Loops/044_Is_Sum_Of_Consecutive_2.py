# https://app.codesignal.com/arcade/code-arcade/labyrinth-of-nested-loops/EQSjA5PRfyHueeNkj
def isSumOfConsecutive2(n):
    # Find the number of ways to express n as a sum of some (at least two)
    # consecutive positive integers.
    # e.g. isSumOfConsecutive2(9) == 2, 2+3+4==9, 4+5==9.

    # count = 0
    # for i in range(0, n):
    #    for j in range(i, n):
    #        if sum(range(i, j)) == n:
    #            count += 1
    # return count

    combinations = set([])
    # Consecutive values that add up to a certain number have the number divided by the
    # amount of values at their center.
    # e.g. 9/3 ~ 2, [3], 4
    #      9/2 ~ 4, [4.5], 5
    for i in range(2, n + 1):
        # Find the value at the center.
        m = n//i
        v = []
        # Find the values at both sides of the centers.
        for j in range(i):
            if i % 2 == 0:
                value = m - i//2 + 1 + j
            else:
                value = m - i//2 + j
            if value > 0:
                v.append(value)
        # Check if all values add up to original value.
        if sum(v) == n:
            combinations.add(",".join(map(str, v)))

    # Return possible amount of combinations of consecutive numbers that add up to n.
    return len(combinations)

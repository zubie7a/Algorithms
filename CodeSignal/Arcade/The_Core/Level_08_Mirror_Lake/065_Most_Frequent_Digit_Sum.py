# https://app.codesignal.com/arcade/code-arcade/mirror-lake/RpoP4Aqa5mbmC8koC
from collections import Counter

def mostFrequentDigitSum(n):
    def digit_sum(num):
        return sum(map(int, str(num)))

    digit_sums = []
    # Keep substracting from a number its own digit sum until
    # it reaches 0, it's guaranteed to do so.
    while n != 0:
        d_sum = digit_sum(n)
        digit_sums.append(d_sum)
        n -= d_sum

    # The count of how many times a digit-sum has appeared.
    counter = Counter(digit_sums)

    # Maybe overkill, just iterate over the original counter and store
    # the largest key with the largest count.
    # -------
    # Now reverse this map to go from counts of occurrences => sum.
    # reverse_counter = {}
    # for key in counter.keys():
    #    value = counter[key]
    #    if value not in reverse_counter:
    #        reverse_counter[value] = []
    #    reverse_counter[value].append(key)
    #
    # max_count = max(counter.values())
    # max_key = sorted(reverse_counter[max_count])[-1]

    max_count = -1
    max_key = -1
    for key, value in counter.items():
        if value > max_count:
            max_key = key
            max_count = value
        elif value == max_count:
            max_key = max(key, max_key)

    return max_key

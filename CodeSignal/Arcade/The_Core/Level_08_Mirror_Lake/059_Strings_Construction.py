# https://app.codesignal.com/arcade/code-arcade/mirror-lake/chW9F8bCgxYJBcgj3
from collections import Counter

def stringsConstruction(a, b):
    # How many strings equal to `a` can be constructed using
    # letters from the string `b`? Each letter can be used
    # only once and in one string only.
    # Let's find the count of characters in each string.
    counts_a = Counter(a)
    counts_b = Counter(b)
    # Now for each character in the first string check how
    # many times it occurs on the second string. The lowest
    # multiple is the bound of how many times you can create
    # the first string based on characters from the second.
    min_times = 2**22
    for key in counts_a.keys():
        count_a = counts_a[key]
        count_b = 0
        if key in counts_b:
            count_b = counts_b[key]
        times = count_b//count_a
        min_times = min(min_times, times)

    # return min_times
    # You can also call count directly on the string!
    return min([b.count(char)//a.count(char) for char in a])

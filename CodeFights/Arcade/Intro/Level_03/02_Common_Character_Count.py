# https://codefights.com/arcade/intro/level-3/JKKuHJknZNj4YGL32
from collections import Counter
def commonCharacterCount(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    common = 0
    # Given two strings, find the amount of common characters
    # between both. This is the min count of a given character
    # ocurring at both. If it doesn't occur, then value is 0
    # and min will be 0.
    for item in c2.items():
        key = item[0]
        common += min(c2[key], c1[key])
    return common

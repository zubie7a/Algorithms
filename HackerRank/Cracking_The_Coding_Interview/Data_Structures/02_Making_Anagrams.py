# https://www.hackerrank.com/challenges/ctci-making-anagrams
from collections import Counter

def number_needed(a, b):
    # Given two strings, how to turn them into anagrams?
    # Get a count of characters per string. Add to the amount
    # of deletions the difference between the count of a char
    # in one string and then the count in the other (including
    # zero counts). Then remove that char from both strings,
    # And do the same with the other string (as a char may be
    # present in one and not the other).
    ca = Counter(list(a))
    cb = Counter(list(b))
    deletions = 0
    for (key, countA) in ca.items():
        countB = cb[key]
        deletions += abs(countA - countB)
        ca[key] = 0
        cb[key] = 0
    for (key, countB) in cb.items():
        countA = ca[key]
        deletions += abs(countA - countB)
        ca[key] = 0
        cb[key] = 0
    return deletions
            
a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)

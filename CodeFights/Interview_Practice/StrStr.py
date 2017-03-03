# https://codefights.com/interview/zRR9siWo5JjNWj3xX
# Strstr: Amazon, Microsoft, Facebook.
# Find pattern in text, non-naive way or not using
# built-in functions like t.find(p) or t.index(p)
def strstr(t, p):
    table = {}
    # For a substring of pattern p of length 1, the longest
    # prefix that is the same suffix that doesn't include
    # the pattern is 0.
    table[1] = 0
    # i will hold the longest prefix==suffix found for a 
    # substring of the pattern.
    m, i = len(p), 0
    # From 2 to the length of the pattern (inclusive).
    for j in range(2, m + 1):
        # Remember to turn these back into 0-index for
        # accessing string positions.
        # p[i + 1] != p[j] ~> p[i] != p[j - 1] 
        while i > 0 and p[i] != p[j - 1]:
            i = table[i]
        if p[i] == p[j - 1]:
            i += 1
        table[j] = i
    # Now that the KMP table has been calculated, find the
    # first position where the pattern occurs in the text.
    n, i = len(t), 0
    for j in range(1, n + 1):
        while i > 0 and p[i] != t[j - 1]:
            i = table[i]
        if p[i] == t[j - 1]:
            i = i + 1
        if i == m:
            return (j - m)
    # If it wasn't found, return -1.
    return -1

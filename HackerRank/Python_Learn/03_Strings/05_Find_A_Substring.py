# https://www.hackerrank.com/challenges/find-a-string
def count_substring(s1, s2):
    # Count occurrences of s2 inside s1
    count = 0
    limit = len(s1) - len(s2) + 1
    # At every position of s1
    for i in range(limit):
        st = ""
        # Start accumulating a string up to the length of s2
        for j in range(len(s2)):
            st += s1[i + j]
        # If that string is equal to s2, then its a match.
        if st == s2:
            count += 1
    return count

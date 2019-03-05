# https://app.codesignal.com/arcade/code-arcade/mirror-lake/EeKpdMQXpBkgWjcvt
from collections import Counter

def constructSquare(s):
    # Given a string `s` of alphabetical characters, substitute
    # them consistently with digits in such a way that the result
    # is a number which is a square.
    # First, lets precompute a bunch of squares.
    squares_by_length = {}
    # Strings can have 10 characters, so this means 10 digits, so we need
    # squares all the way up to 9999999999.
    for i in range(100000):
        num_str = str(i**2)
        length = len(num_str)
        if not(length in squares_by_length):
            squares_by_length[length] = []
        # Store squares according to the length they take.
        squares_by_length[length].append(num_str)

    # Now lets do the usual substitution validation
    s_length = len(s)
    for square in reversed(squares_by_length[s_length]):
        # Build counters of unique charaters and unique digits.
        count_s = Counter(s)
        count_n = Counter(square)
        # Now the ordered values have to be exactly the same in content.
        if sorted(count_s.values()) == sorted(count_n.values()):
            return int(square)

    return -1

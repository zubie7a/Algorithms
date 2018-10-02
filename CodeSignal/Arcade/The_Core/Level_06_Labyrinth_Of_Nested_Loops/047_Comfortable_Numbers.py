# https://app.codesignal.com/arcade/code-arcade/labyrinth-of-nested-loops/pNfGgNk46YZ4c4RW5
def comfortableNumbers(l, r):
    # A number a feels comfortable with number b if a != b and b lies
    # in the segment [a - s(a), a + s(a)] where s(x) is sum of x digits.
    # How many pairs (a, b) are there such that a < b, both a and b lie
    # on the segment [l, r] and each number feels comfortable with the
    # other? (a comfortable with b and b comfortable with a).
    def s(val):
        return sum([int(digit) for digit in str(val)])

    def in_range(left, right, val):
        return left <= val and val <= right

    comfortable_pairs = 0
    # For every a in the given range...
    for a in range(l, r + 1):
        # The bounds of comfortableness of a, but remember to restrict them
        # with the actual global bounds l and r.
        # Low a won't be calculated because even if a can be comfortable
        # with a smaller value, problem wants b to be larger.
        low_a = a + 1 # max(a - s(a), l)
        high_a = min(a + s(a), r) + 1
        # Lets iterate for b's within the range of comfortableness, meaning
        # a is comfortable with all those b's, but are those with a?
        for b in range(low_a, high_a):
            low_b = max(b - s(b), l)
            high_b = min(b + s(b), r) + 1
            if in_range(low_b, high_b, a):
                comfortable_pairs += 1

    return comfortable_pairs

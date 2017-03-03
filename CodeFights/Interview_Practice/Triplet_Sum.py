# https://codefights.com/interview/MZnrYnavhHmYEwZs8
# Triplet Sum: Samsung, Amazon.
# Add triplets to see if they add to a certain value, in O(n^2).
from collections import Counter
def tripletSum(x, a):
    # Hashmap with count of value occurrences.
    m = Counter(a)
    for i in range(len(a)):
        # First value.
        _b = a[i]
        for j in range(i + 1, len(a)):
            # Second value.
            _a = a[j]
            # The value we want to find.
            diff = x - _b - _a
            # If check that the occurrences of the expected
            # value are separate from the current two values
            # used to find it.
            if m[diff] > (_b == diff) + (_a == diff):
                return True 
    return False
        

# https://codefights.com/interview/qAL6AiSejoJZRNyox
# Sum Of Two: Google.
from collections import Counter
def sumOfTwo(a, b, v):
    # Check if there's any element from a and any element
    # from b that add up to a v value.
    cb = Counter(b)
    for _a in a:
        diff = v - _a
        if cb[diff] > 0:
            return True
    return False

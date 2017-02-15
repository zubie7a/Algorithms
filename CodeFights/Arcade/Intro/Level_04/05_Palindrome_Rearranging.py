# https://codefights.com/arcade/intro/level-4/Xfeo7r9SBSpo3Wico
from collections import Counter
def palindromeRearranging(inputString):
    # A string can only be rearranged into a palindrome if:
    # All characters occurs an even amount of times.
    # And maybe just one occurss an odd amount of times.
    c = Counter(inputString)
    res, oddOccurrs = True, False
    for key, value in c.items():
        if value % 2 == 1:
            if oddOccurrs == False:
                oddOccurrs = True
            else:
                res = False
    return res

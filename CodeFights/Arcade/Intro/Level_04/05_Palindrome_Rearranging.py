# https://app.codesignal.com/arcade/intro/level-4/Xfeo7r9SBSpo3Wico
from collections import Counter

def palindromeRearranging(input_string):
    # A string can only be rearranged into a palindrome if:
    # * All characters occurs an even amount of times.
    # * And maybe just one occurrs an odd amount of times.
    c = Counter(input_string)
    res, odd_occurrs_once = True, False
    for key, value in c.items():
        if value % 2 == 1:
            if odd_occurrs_once == False:
                odd_occurrs_once = True
            else:
                res = False

    return res

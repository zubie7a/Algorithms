# 266 - Palindrome Permutation (Easy)
# https://leetcode.com/problems/palindrome-permutation/
from collections import Counter

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Check if characters in a string can form a palindrome.
        # All values have to happen by multiples of 2, or just one
        # happening an odd amount of times.
        odds = filter(lambda x: x % 2 == 1, Counter(list(s)).values())
        return len(odds) <= 1
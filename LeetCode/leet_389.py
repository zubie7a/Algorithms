# https://leetcode.com/problems/find-the-difference/
from collections import Counter

# From two strings s, t, find out the extra character added to t.
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counterS = Counter(list(s))
        counterT = Counter(list(t))
        finalCounter = counterT - counterS
        return str(finalCounter.keys()[0])
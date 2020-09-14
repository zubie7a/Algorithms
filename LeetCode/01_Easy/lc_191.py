# 191 - Number of 1 Bits (Easy)
# https://leetcode.com/problems/number-of-1-bits/

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        # To convert from integer base 10 to binary string and back.
        # >>> format(5, "b")
        # '101'
        # >>> "{0:b}".format(5)
        # '101'
        # >>> int("101", 2)
        # 5
        return sum([int(digit) for digit in format(n, "b")])

# 202 - Happy Number (Easy)
# https://leetcode.com/problems/happy-number/

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # A happy number is a number whose sum of the squares of its
        # digits applied repeatedly ends up in 1. It is not happy if
        # it will just loop forever.
        # Let's build a cache table, to make sure we are not looping.
        cache = {}
        # Another unhappy-detection is if we find out a number we had already visited.
        def recursive_happiness(n):
            # This is a happy number.
            if n == 1:
                return True
            # This is not a happy number, there's a loop.
            if cache.get(n):
                return False

            cache[n] = 1
            sum_squares = sum([ int(digit)**2 for digit in str(n) ])
            return recursive_happiness(sum_squares)

        return recursive_happiness(n)

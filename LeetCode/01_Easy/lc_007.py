# 007 - Reverse Integer (Easy)
# https://leetcode.com/problems/reverse-integer/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Store the sign separately.
        sign = 1 if x >= 0 else -1
        # Remove the sign.
        x = abs(x)
        # Reverse the number-string, convert back to number, apply sign.
        r_x = sign * int(str(x)[::-1])
        # Check that the reversed number doesn't overflow/underflow int.
        if r_x < -2**31 or (2**31 - 1) < r_x:
            r_x = 0

        return r_x

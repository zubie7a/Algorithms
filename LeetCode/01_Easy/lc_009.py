# 009 - Palindrome Number (Easy)
# https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # Negative numbers are not palindromes because of the sign.
        if x < 0:
            return False
    
        # Convert number to string
        str_x = str(abs(x))
        # Check that the number-string is same as reversed.
        return str_x == str_x[::-1]

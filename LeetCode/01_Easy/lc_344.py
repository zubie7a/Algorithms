# 344 - Reverse String (Easy)
# https://leetcode.com/problems/reverse-string/
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # DO NOT iterate over the string appending character by
        # character, this seems to be REALLY EXPENSIVE. Reverse it
        # and then join it.
        return "".join(reversed(list(s)))
        
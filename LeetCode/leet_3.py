# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        positions = defaultdict(lambda: -1)
        # Where the starting index of the longest substring goes.
        startIndex = 0
        # The current max length of the longest substring.
        maxLength = 0
        for i in range(len(s)):
            # If the current starting index is behind the current lastest
            # position of a character, advance the starting position to the
            # next character after that character.
            if startIndex <= positions[s[i]]:
                startIndex = positions[s[i]] + 1
            # Increase the max length because so far nothing that previously
            # existed has been found.
            else:
                maxLength = max(maxLength, i - startIndex + 1)
            positions[s[i]] = i
        return maxLength
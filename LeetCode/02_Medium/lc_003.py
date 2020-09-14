# 003 - Longest Substring Without Repeating Characters (Medium)
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        positions = defaultdict(lambda: -1)
        # A moving index of the current substring.
        start_idx = 0
        # The length of the longest substring.
        max_length = 0

        for idx in range(len(s)):
            char = s[idx]
            # If the current character has a previous recorded
            # position and the starting index is behind that,
            # then we have to move the starting index to the
            # position right after the current character.
            if start_idx <= positions[char]:
                start_idx = positions[char] + 1  
            # Otherwise, increase the length of the max substring.
            else:
                max_length = max(max_length, idx - start_idx + 1)

            # Store the current index as the latest position where
            # the current character has been seen.
            positions[char] = idx

        return max_length

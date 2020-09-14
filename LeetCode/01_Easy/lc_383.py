# 383 - Ransom Note (Easy)
# https://leetcode.com/problems/ransom-note/
from collections import Counter

class Solution(object):
    def canConstruct(self, ransom_note, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Is it possible to build a certain ransom note starting from the letters in a magazine?
        counter_ransom = Counter(ransom_note)
        counter_magazine = Counter(magazine)
        valid = all(counter_magazine[char] >= counter_ransom[char] for char in list(ransom_note))
        return valid

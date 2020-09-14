# 205 - Isomorphic Strings (Easy)
# https://leetcode.com/problems/isomorphic-strings/

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Check if the characters from s can be replaced consistently to
        # obtain the string in t. This is like a substitution cipher.

        # Traverse both strings, and try to create a substitution dictionary.
        # If an inconsistency is found, then this substitution can not be done.
        # We can assume that `s` and `t` have the same length.

        # Substitution dictionaries for both directions.
        subs_s, subs_t = {}, {}

        for idx in range(len(s)):
            char_s, char_t = s[idx], t[idx]
            # Every unique char in s must map to unique chars
            # in t, and viceversa, a 1-to-1 mapping.
            if subs_s.get(char_s) and subs_s.get(char_s) != char_t:
                # If we already registered a mapping for a character in
                # s and it is not the expected character in t...
                return False
            if subs_t.get(char_t) and subs_t.get(char_t) != char_s:
                # If we already registered a mapping for a character in
                # t and it is not the expected character in s...
                return False
            subs_s[char_s] = char_t
            subs_t[char_t] = char_s

        return True

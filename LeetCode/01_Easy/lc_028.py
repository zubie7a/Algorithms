# 028 - Implement strStr() (Easy)
# https://leetcode.com/problems/implement-strstr/

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if needle == "":
            return 0

        # Build the initial prefix-suffix table with the length of the needle.
        lps = [0 for _ in range(len(needle))]

        # We'll always start comparing with position 0.
        idx_needle_j = 0
        # ... but start from position 1, by default position 0 will have value 0.s
        # This loop takes O(len(needle)).
        for idx_needle_i in range(1, len(needle)):
            char_i = needle[idx_needle_i]
            char_j = needle[idx_needle_j]
            if char_i == char_j:
                # Store the index of the matching character + 1, and advance the initial index.
                lps[idx_needle_i] = idx_needle_j + 1
                idx_needle_j += 1
            else:
                # Move j to the index of the value of the previous character, until it either
                # matches or goes back all the way to the start.
                while idx_needle_j != 0:
                    idx_needle_j = lps[idx_needle_j - 1]
                    # And do the same previous operations at new position.
                    char_i = needle[idx_needle_i]
                    char_j = needle[idx_needle_j]
                    if char_i == char_j:
                        lps[idx_needle_i] = idx_needle_j + 1
                        idx_needle_j += 1
                        break

        idx_needle = 0
        idx_haystack = 0
        # This loop takes O(len(haystack)).
        while idx_haystack < len(haystack):
            char_haystack = haystack[idx_haystack]
            char_needle = needle[idx_needle]
            if char_haystack == char_needle:
                idx_needle += 1
            else:
                # Look in the prefix-suffix table how further back we want to go,
                # because it is redundant to check for existing prefix-suffixes.
                if idx_needle > 0:
                    idx_needle = lps[idx_needle - 1]
                    # Step back the haystack index so that the next iteration we compare
                    # again with the current character with the character at the new
                    # needle index.
                    idx_haystack -= 1

            if idx_needle == len(needle):
                return idx_haystack - idx_needle + 1

            # Keep advancing the index of the haystack.
            idx_haystack += 1

        # Meaning no index was found.
        return -1

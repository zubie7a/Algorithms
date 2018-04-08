# https://leetcode.com/problems/shortest-word-distance/
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Find the shortest separation between two words in an array,
        # such words are guaranteed to happen but also may happen more
        # than once. Also the two words are distinct.
        i1, i2 = -1, -1
        minDist = 1<<31
        for index in xrange(len(words)):
            word = words[index]
            if word == word1:
                i1 = index
            if word == word2:
                i2 = index
            if i1 != -1 and i2 != -1:
                minDist = min(minDist, abs(i1 - i2))
        return minDist
            
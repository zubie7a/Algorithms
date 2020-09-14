# 014 - Longest Common Prefix (Easy)
# https://leetcode.com/problems/longest-common-prefix/

class PrefixTree(object):
    def __init__(self, string=""):
        # Initialize empty dict of children nodes.
        self.children = {}
        self.terminal = False

    def insert(self, string):
        char = string[0]
        # With the key of the first character of the string, create a new
        # prefix tree that starts with the rest of the string, or if it's
        # a path that already exists, just insert into it.
        if char not in self.children:
            self.children[char] = PrefixTree()
        
        if len(string[1:]) > 0:
        	# Insert from the next position onwards.
            self.children[char].insert(string[1:])
        else:
            # If the string has finished being consumed, mark this node as a
            # terminal node.
            self.terminal = True

    # Recursively go down the prefix tree as long as there's only one path
    # to go (meaning it's a shared prefix) and no string has been fully
    # consumed.
    def traverse(self, acum=""):
        if len(self.children) == 1:
            key = list(self.children.keys())[0]
            child = self.children[key]

            # A string finished here, so we can't find longer prefixes.
            if self.terminal == True:
                return acum + key

            return child.traverse(acum + key)
        else:
            return acum

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        base_tree = PrefixTree()
        for string in strs:
            # Input strings can have length 0. If any string is empty then we
            # can't find any common prefix at all.
            if len(string) > 0:
                base_tree.insert(string)
            else:
                return ""

        return base_tree.traverse()

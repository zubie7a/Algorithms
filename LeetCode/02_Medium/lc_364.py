# 364 - Nested List Weight Sum II (Medium)
# https://leetcode.com/problems/nested-list-weight-sum-ii/

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    # Find the max depth, so that when the usual DFS is done, the inverse
    # depth is calculated.
    def findMaxDepth(self, nestedList, depth):
        if len(nestedList) == 0:
            return 0
        nextDepth = depth + 1
        for NI in nestedList:
            if NI.isInteger():
                continue
            else:
                depth = max(depth, self.findMaxDepth(NI.getList(), nextDepth))
        return depth
    # The usual DFS but instead of multiplying by real depth, do it with the
    # inverse which needs to have beforehand the max depth.
    def dfs(self, nestedList, depth, maxDepth):
        if len(nestedList) == 0:
            return 0
        acum = 0
        for NI in nestedList:
            if NI.isInteger():
                acum += NI.getInteger() * (maxDepth - depth + 1)
            else:
                acum += self.dfs(NI.getList(), depth+1, maxDepth)
        return acum
        
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        maxDepth = self.findMaxDepth(nestedList, 1)
        return self.dfs(nestedList, 1, maxDepth)
        
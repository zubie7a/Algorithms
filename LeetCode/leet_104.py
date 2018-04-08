# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Find the max depth of a binary tree.
class Solution(object):
    def maxDepth(self, root, depth=1):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return depth - 1
        
        left = self.maxDepth(root.left, depth + 1)
        right = self.maxDepth(root.right, depth + 1)
        return max(left, right)
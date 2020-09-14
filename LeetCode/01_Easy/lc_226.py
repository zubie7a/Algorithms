# 226 - Invert Binary Tree (Easy)
# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# I can invert the binary tree please hire me Google! :-)
# Sometimes I have nostalgia remembering the past internships ;u;
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        # temp_node = root.left
        # root.left = self.invertTree(root.right)
        # root.right = self.invertTree(temp_node)
        # return root
        # You can choose whether to do it mutating the original object
        # like above, or creating a new tree altogether!
        new_left = self.invertTree(root.right)
        new_right = self.invertTree(root.left)
        return TreeNode(root.val, new_left, new_right)

# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree
""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check_binary_search_tree_(root):
    # To check if its a binary search tree, do an inorder search
    # and compare it with the same list but sorted.
    def inOrder(node):
        arr = []
        if node is None:
            return []
        arr.extend(inOrder(node.left))
        arr.append(node.data)
        arr.extend(inOrder(node.right))
        return arr
    arr = inOrder(root)
    # So, check that the traversal array is sorted, and check that
    # all elements are unique by using a set (a tree with repeated
    # elements can not be a BST).
    return arr == sorted(arr) and len(set(arr)) == len(arr)

# 083 - Remove Duplicates from Sorted List (Easy)
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def remove_recursively(head, node, prev_node=None):
            # No more elements in the list, return the original pointer.
            if node is None:
                return head

            # No previous value, continue the recursion.
            if prev_node is None:
                return remove_recursively(head, node.next, node)
            else:
                if prev_node.val == node.val:
                    # Remove the current node and continue with recursion while preserving
                    # the old previous node until finding a different value.
                    prev_node.next = node.next
                    return remove_recursively(head, node.next, prev_node)
                # Otherwise just continue with recursion.
                return remove_recursively(head, node.next, node)

        return remove_recursively(head, head)

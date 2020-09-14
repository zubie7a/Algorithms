# 082 - Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

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
        duplicates = {}
        def reduce_recursively(head, node, prev_node=None):
            # No more elements in the list, return the original pointer.
            if node is None:
                return head

            # No previous value, continue the recursion.
            if prev_node is None:
                return reduce_recursively(head, node.next, node)
            else:
                if prev_node.val == node.val:
                    # Remove the current node and continue with recursion while preserving
                    # the old previous node until finding a different value.
                    prev_node.next = node.next
                    duplicates[prev_node.val] = 1
                    return reduce_recursively(head, node.next, prev_node)
                # Otherwise just continue with recursion.

                return reduce_recursively(head, node.next, node)

        def remove_recursively(head, node, prev_node=None):

            if prev_node is None:
                prev_node = node

            if node is None:
                return head

            # If the value of the current node is duplicated.
            if duplicates.get(node.val):
                prev_node.next = node.next
                return remove_recursively(head, node.next, prev_node)

            return remove_recursively(head, node.next, node)

        # This will reduce to unique ocurrences, but register separately the repeated values.
        reduce_recursively(head, head)
        # After reusing the solution to the reduction problem, go through the list removing
        # nodes that are labeled as duplicated previously.
        remove_recursively(head, head)

        # The removing doesn't remove the value at the head so manually check if the
        # head (if defined) has a duplicated value, if so return whatever is next.
        if head and duplicates.get(head.val):
            return head.next

        return head

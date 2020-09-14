# 206 - Reverse Linked List (Easy)
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def recursive_reverse(node, reverse=None):
            # If original list has been consumed, just return the reversed list.
            if node is None:
                return reverse

            # Put aside everything after the current node.
            next_node = node.next

            # If there's no reverse cumulatively generated list so far, start it.
            if reverse is None:
                # Make the head of the reversed list so far the current node.
                reverse = node
                # Erase the pointer after the current node.
                reverse.next = None
            else:
                # Puf after the current node the reversed list so far.
                node.next = reverse
                # Make the head of the reversed list so far the current node.
                reverse = node

            # Make the current node the previous next node.
            node = next_node
            # Return tail-recursively.
            return recursive_reverse(node, reverse)

        return recursive_reverse(head)

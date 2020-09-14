# 021 - Merge Two Sorted Lists (Easy)
# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # Merge two lists in place. Take a base list to splice
        # the other list into it.
        # l1 will be the base list to splice nodes into.
        # l2 will be the list we'll remove nodes from.

        # Store the reference to the start of l1.
        res = l1

        # Edge case, when any starts empty, return the other..
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        # While there's still a l2 to remove stuff from...
        while l2 is not None:
            # Let's assume the lower value is in l1, doesn't really matter
            # if we switch this.
            cur_l1, cur_l2 = sorted([l1.val, l2.val])
            l1.val, l2.val = cur_l1, cur_l2
            # Assume the next l1 value is really large, unless there's actually
            # a next value.
            nex_l1 = 2<<31
            if l1.next is not None:
                nex_l1 = l1.next.val

            # If the current value of the node of l2 is in-between
            # the current value of the node of l1 and the next value
            # of l1, then splice the current l2 node!            
            if cur_l1 <= cur_l2 and cur_l2 <= nex_l1:
                l2_temp = l2.next
                l2.next = l1.next
                l1.next = l2
                l2 = l2_temp
            else:
                l1 = l1.next

        return res

# Recursive solution:
# O(m + n) time, as well as space because of the stack frames created.
# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         if l1 is None:
#             return l2
#         elif l2 is None:
#             return l1
#         elif l1.val < l2.val:
#             l1.next = self.mergeTwoLists(l1.next, l2)
#             return l1
#         else:
#             l2.next = self.mergeTwoLists(l1, l2.next)

#             return l2
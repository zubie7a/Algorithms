# 002 - Add Two Numbers (Medium)
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        # A node to store the answer and a node to keep appending nodes to.
        res_node, cur_node = None, None

        # Loop while either linked list has still something to consume.
        while l1 is not None or l2 is not None:

            # If a linked list has been exhausted just assign value 0.
            val_1   = l1.val if l1 is not None else 0
            val_2   = l2.val if l2 is not None else 0

            val_res = (val_1 + val_2) + carry
            # The values have been consumed so advance the linked lists.
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

            carry = 1 if val_res > 9 else 0
            val_res %= 10

            if res_node is None:
                # Initialization of the first node.
                res_node = ListNode(val_res)
                cur_node = res_node
            else:
                # Keep advancing nodes in the result linked list.
                new_node = ListNode(val_res)
                cur_node.next = new_node
                cur_node = new_node

        # If there's a carry at the end, add a new node with that carry.
        if carry == 1:
            cur_node.next = ListNode(1)

        # The original node reference was never advanced, this is from start.
        return res_node

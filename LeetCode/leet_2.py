# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # The pointer to hold the answer.
        res = ListNode(-1)
        # The sliding pointer.
        cur = res
        carry = 0
        # When either number is finished, stop.
        while l1 is not None and l2 is not None:
            num1 = l1.val
            num2 = l2.val
            num3 = num1 + num2 + carry
            carry = num3 / 10
            num3 %= 10
            node = ListNode(num3)
            # Advance both number digits pointers.
            l1 = l1.next
            l2 = l2.next
            # Store in the result the currently computed node.
            cur.next = node
            # Advance the sliding pointer.
            cur = cur.next
        # If there was any number with digits left, append to solution.
        if l1 is not None:
            cur.next = l1
        if l2 is not None:
            cur.next = l2
        # We may still have a carry pending, so apply the carry until
        # no carry is left (may be a carry with lots of 99999 remainding!)
        # Keep moving the sliding pointer at each step. The carry starts
        # applying at the next node, so if there's no next node, create
        # it with a 0 value!
        while carry == 1:
            if cur.next is None:
                cur.next = ListNode(0)
            cur = cur.next
            cur.val += carry
            carry = cur.val / 10
            cur.val %= 10
        return res.next
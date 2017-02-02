# https://www.hackerrank.com/challenges/ctci-linked-list-cycle
"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    # Base case: the head is None or the next element is None.
    if head is None or head.next is None:
        # There's no loop then.
        return False
    # We'll have two pointers, the current one which advances by one step,
    # and the next one which advances by two steps.
    cur = head
    nex = head.next
    while True:
        # When either element is None it means the end has been reached.
        if cur is None or nex is None:
            return False
        # If there's an overlap, its because the next element, advancing
        # by two steps, entered a "lap" and took over the current element,
        # indicating there was a loop.
        if cur == nex:
            return True
        # Advance both pointers by one step.
        cur = cur.next
        nex = nex.next
        # If the more advanced one has reached an end, it means no loop.
        if nex is None:
            return False
        # Advance the more advanced one once again, and repeat the cycle.
        nex = nex.next

# https://leetcode.com/problems/moving-average-from-data-stream/
from collections import deque

class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        # Max amount of values to store.
        self.size = size
        # Deque to store values (a queue also does it). When a
        # problem says something about windows, use de/queues.
        self.dq = deque([])
        # The acum of values so far. If a value is dropped from
        # the deque, then substract it from this acum. Then the
        # acum is divided by the total amount of values so that
        # the running average is found.
        self.acum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        # Append the value and update the acum.
        self.dq.append(val)
        self.acum += val
        # If the capacity was exceeded...
        if len(self.dq) > self.size:
            # Remove the last value and substract it from acum.
            left = self.dq.popleft()
            self.suma -= left
        # Now calculate the average for current window! Remember to
        # use float since this division in Python2 is integer div.
        return float(self.suma)/len(self.dq)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
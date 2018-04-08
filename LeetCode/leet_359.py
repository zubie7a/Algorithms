# https://leetcode.com/problems/logger-rate-limiter/
from collections import defaultdict

class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # From timestamp to log messages.
        self.logs = defaultdict(lambda: -1)
        
    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if self.logs[message] != -1:
            if timestamp - self.logs[message] + 1 <= 10:
                return False
        self.logs[message] = timestamp
        return True
        
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
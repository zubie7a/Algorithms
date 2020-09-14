# 460 - LFU Cache (Hard)
# https://leetcode.com/problems/lfu-cache/
# Implement a Least Frequently Used cache. GODDAMN I almost died.

from collections import OrderedDict, defaultdict

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # From key to value.
        self.dic = {}
        # Times a key has been used.
        self.count = {}
        # Keys grouped by amount of usage.
        # e.g. from a key 2 (as in two times used), get the keys that have been
        # used that much times.
        self.reverse = defaultdict(lambda: OrderedDict())
        # Capacity of the LFU.
        self.cap = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # If the key exists. Make sure to put "is not None" otherwise a 0 Value
        # will make the condition evaluate to False.
        if self.dic.get(key) is not None:
            # Update the amount of times key has been used.
            prevCount = self.count[key]
            newCount = prevCount + 1
            self.count[key] = newCount
            # Delete the key from the previous grouping of times used.
            del self.reverse[prevCount][key]
            # If that grouping is now empty, erase it too.
            if len(self.reverse[prevCount]) == 0:
                del self.reverse[prevCount]
            # Insert key into the new grouping of times used.
            self.reverse[newCount][key] = True
            # Return the value associated to this key.
            return self.dic[key]
        # If the key doesn't exists, just return -1.
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # Check that the value exists, so that it will be updated.
        if self.dic.get(key) is not None:
            # Times used previously.
            prevCount = self.count[key]
            # New amount of times used.
            newCount = prevCount + 1
            # Set the new amount.
            self.count[key] = newCount
            # Delete the key from the previous grouping of times used.
            del self.reverse[prevCount][key]
            # If that grouping is now empty, erase it too.
            if len(self.reverse[prevCount]) == 0:
                del self.reverse[prevCount]
            # Insert key into the new grouping of times used.
            self.reverse[newCount][key] = True
            # Now update the value associated to this key.
            self.dic[key] = value
        # If the value doesn't exists...
        else:
            # If capacity will be exceeded, erase the currently least used one.
            if len(self.dic) == self.cap and len(self.reverse) > 0:
                # Because the "reverse" (from count to keys) dict groups keys
                # by accessed amount, lets get the least amount of uses.
                leastAmount = sorted(self.reverse.keys())[0]
                # Now, because this is an OrderedDict, lets get the least freq
                # used key by accessing with the leastAmount of uses value.
                leastKey = (self.reverse[leastAmount].keys())[0]
                # Delete that number from the grouping of keys used that times.
                del self.reverse[leastAmount][leastKey]
                # If there are no more keys for this count, delete the count.
                if len(self.reverse[leastAmount]) == 0:
                    del self.reverse[leastAmount]
                # Delete the individual amount of uses for the LFU key.
                del self.count[leastKey]
                # Delete the LFU key and its value.
                del self.dic[leastKey]
            # Now, insert the new key, with a single usage (the insertion).
            if len(self.dic) + 1 <= self.cap:
                self.dic[key] = value
                self.count[key] = 1
                self.reverse[1][key] = True

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.set(key,value)
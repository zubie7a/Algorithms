# 146 - LRU Cache (Medium)
# https://leetcode.com/problems/lru-cache/

# Implement a LRU (Least Recently Used) cache. It has an initialization (with as
# capacity) and two operations, get and set. Any time an element is retrieved,
# set or updated, it has become the most recently used. If there's a lot of elements
# exceeding the LRU capacity, then start removing the least recently used ones.

# If you feel OrderedDict is like cheating, you can use a dict + deque :-)
# So the order is kept while inserting keys on the deque, but values are on the dict.
from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = OrderedDict()
        self.cap = capacity

    def get(self, key):
        """
        :rtype: int
        """
        try:
            # Least Recently Used, does that mean that once its retrieved
            # it has to be put on top again?
            val = self.dic[key]
            del self.dic[key]
            self.dic[key] = val
            return val
        except:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        try:
            # If the value exists, lets update it and put it back on front.
            del self.dic[key]
            self.dic[key] = value
        except:
            self.dic[key] = value
        
        # If the cap is exceeded, lets erase the element at the back.
        if len(self.dic) > self.cap:
            keys = self.dic.keys()
            del self.dic[keys[0]]
        
# Using Dictionary + Deque
from collections import deque

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.deq = deque([])
        self.dic = {}
        self.cap = capacity
        

    def get(self, key):
        """
        :rtype: int
        """
        try:
            val = self.dic[key]
            self.deq.remove(key)
            self.deq.append(key)
            return val
        except:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        try:
            self.deq.remove(key)
        except:
            None
        self.deq.append(key)
        self.dic[key] = value
        
        # If the cap is exceeded, lets erase the element at the back.
        if len(self.dic) > self.cap:
            key = self.deq.popleft()
            del self.dic[key]
        
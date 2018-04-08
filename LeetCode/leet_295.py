# https://leetcode.com/problems/find-median-from-data-stream/
import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lower = []
        self.higher = []
        
    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        # By default put into left. Negative values is so that the heap
        # will be a max-heap, because by default it is a min-heap and I don't
        # know how else to make it a max-heap :-)
        if len(self.lower) == 0:
            heapq.heappush(self.lower, -num)
        # If lower is equal len than higher, if value is to be put in lower,
        # then just put it there, if its to be put in higher, then move down
        # one value from higher and then put new value in there.
        elif len(self.lower) == len(self.higher):
            topleft = -heapq.heappop(self.lower)
            topright = heapq.heappop(self.higher)
            if num < topright: 
                heapq.heappush(self.lower, -topleft)
                heapq.heappush(self.lower, -num)
                heapq.heappush(self.higher, topright)
            else:
                heapq.heappush(self.lower, -topleft)
                heapq.heappush(self.lower, -topright)
                heapq.heappush(self.higher, num)
        # If higher is empty, then put new value in there only if its greater
        # than value in lower, otherwise move value from lower to higher and
        # then put new value in lower.
        elif len(self.higher) == 0:
            topleft = -heapq.heappop(self.lower)
            if num > topleft:
                heapq.heappush(self.lower, -topleft)
                heapq.heappush(self.higher, num)
            else:
                heapq.heappush(self.lower, -num)
                heapq.heappush(self.higher, topleft)
        # If lower is greater length than higher, and both are not zero-len,
        # then decide where to put new value so to both sides lenght are equal.
        else:
            topleft = -heapq.heappop(self.lower)
            topright = heapq.heappop(self.higher)
            if num > topleft:
                heapq.heappush(self.higher, num)
                heapq.heappush(self.higher, topright)
                heapq.heappush(self.lower, -topleft)
            else:
                heapq.heappush(self.lower, -num)
                heapq.heappush(self.higher, topright)
                heapq.heappush(self.higher, topleft)

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        # If odd total len, then the value on lower heap
        # If even total len, avg of both heaps.
        res = []
        if len(self.lower) > 0:
            res.append(-heapq.heappop(self.lower))
        if len(self.higher) > 0:
            res.append(heapq.heappop(self.higher))
        if len(res) > 0:
            heapq.heappush(self.lower, -res[0])
        if len(res) > 1:
            heapq.heappush(self.higher, res[1])
        if len(res) > 0:
            if len(self.lower) > len(self.higher):
                return float(res[0])
            else:
                return (res[0] + res[1])/float(2)
        return -0.0

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
import heapq
# https://www.hackerrank.com/challenges/ctci-find-the-running-median
n = int(raw_input())
# Find the running median of a list of numbers by using two heaps.

# Heap to store the lower half of the numbers.
# By default, these are min heaps, so to have a max heap, lets insert negated
# values so that the highest positive values will become the lowest negative
# and viceversa.
maxHeap = []
# Heap to store the upper half of the numbers.
minHeap = []

for i in xrange(n):
    val = int(raw_input())
    # By default, always insert first in the maxHeap.
    if len(maxHeap) == 0:
        heapq.heappush(maxHeap, -val)
    # If the length of the minHeap is less than the length of the maxHeap,
    # Figure out whether to put the new element in which heap, according
    # to if its less or greater than the top value of the maxHeap, so that
    # both heaps are balanced in amount of values.
    elif len(maxHeap) > len(minHeap):
        # Get out the top value from the maxHeap.
        mx = -heapq.heappop(maxHeap)
        # Compare it to the new value to figure out where to put both.
        if mx >= val:
            heapq.heappush(maxHeap, -val)
            heapq.heappush(minHeap, mx)
        else:
            heapq.heappush(maxHeap, -mx)
            heapq.heappush(minHeap, val)
    # If both heaps have are balanced, take the top elements from both, and
    # figure where to put the 3 values, by giving preference to the left heap
    # to become unbalanced.
    else:
        # Get out the top values from both heaps.
        mx = -heapq.heappop(maxHeap)
        mn = heapq.heappop(minHeap)
        # Figure out where to put all three values.
        # <= or >= because mn and mx could be the same value.
        if val <= mn:
            heapq.heappush(maxHeap, -val)
            heapq.heappush(maxHeap, -mx)
            heapq.heappush(minHeap, mn)
        elif val >= mx:
            heapq.heappush(maxHeap, -mx)
            heapq.heappush(maxHeap, -mn)
            heapq.heappush(minHeap, val)
    
    # If both heaps are balanced, the median is the average of the max
    # element to the left, and the min element to the right.
    if len(maxHeap) == len(minHeap):
        mx = -heapq.heappop(maxHeap)
        mn = heapq.heappop(minHeap)
        print "%.1f" % ((mx + mn) / 2.0)
        heapq.heappush(maxHeap, -mx)
        heapq.heappush(minHeap, mn)
    # If the heaps are unbalanced, the maxHeap has one more element than
    # the minHeap, the median is then the top element of the maxHeap.
    else:
        mx = -heapq.heappop(maxHeap)
        print "%.1f" % mx
        heapq.heappush(maxHeap, -mx)
  
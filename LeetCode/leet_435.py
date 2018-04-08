# https://leetcode.com/problems/non-overlapping-intervals/
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# How many intervals have to be erased from a list so that all
# remaining intervals are not overlapping?
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        sortIntervals = sorted(intervals, key=lambda x: x.end)
        end = -1<<31
        erased = 0
        # Sort intervals by "end" key, and check that each interval's
        # "start" is no lesser than the previously biggest "end" found.
        # Those that are lesser then are overlapping.
        for intv in sortIntervals:
            if intv.start >= end:
                end = intv.end
            else:
                erased += 1
        return erased

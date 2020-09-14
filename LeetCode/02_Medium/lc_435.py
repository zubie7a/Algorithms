# 435 - Non Overlapping Intervals (Medium)
# https://leetcode.com/problems/non-overlapping-intervals/

# How many intervals have to be erased from a list so that all
# remaining intervals are not overlapping?
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        sortIntervals = sorted(intervals, key=lambda x: x[1])
        end = -1<<31
        erased = 0
        # Sort intervals by "end" key, and check that each interval's
        # "start" is no lesser than the previously biggest "end" found.
        # Those that are lesser then are overlapping.
        for intv in sortIntervals:
            if intv[0] >= end:
                end = intv[1]
            else:
                erased += 1
        return erased

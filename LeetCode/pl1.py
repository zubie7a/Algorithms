# https://leetcode.com/problems/range-sum-query-immutable/
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.arr = []
        acum = 0
        self.arr.append(0)
        for i in range(len(nums)):
            acum += nums[i]
            self.arr.append(acum)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.arr[j+1] - self.arr[i]

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
"""
    Given nums = [-2, 0, 3, -5, 2, -1]

    sumRange(0, 2) -> 1
    sumRange(2, 5) -> -1
    sumRange(0, 5) -> -3

    Time complexity : O(1) time per query, O(n) time pre-computation. Since the
    cumulative sum is cached, each sumRange query can be calculated in O(1)
    time. Space complexity : O(n).
"""
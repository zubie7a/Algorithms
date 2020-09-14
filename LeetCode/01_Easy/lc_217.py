# 217 - Contains Duplicate (Easy)
# https://leetcode.com/problems/contains-duplicate/

from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(Counter(nums).keys()) != len(nums)
        return len(set(nums)) != len(nums)